const cam = document.getElementById('cam')

const startVideo = () => {
    navigator.mediaDevices.enumerateDevices()
    .then(devices => {
        if (Array.isArray(devices)) {
            devices.forEach(device => {
                if (device.kind == 'videoinput') {
                    console.log(device) // mostrar no console os dispositivos de video conectado
                    if(device.label.includes('HD')) { //escolhendo a camera certa
                        navigator.getUserMedia(
                            {video: {
                                deviceId: device.deviceId
                            }},
                            stream => cam.srcObject = stream,
                            error => console.error(error)
                        )                       
                    }
                }
            })
        }
    })
}

const folderNames = ['Adriano Nobre', 'Geovani Lopes', 'Matheus Castiglioni', 'Adevan Neves'];

const loadLabels = async () => {
    const descriptionsPromises = folderNames.map(async (folderName) => {
      const descriptions = [];
      for (let i = 1; i <= 5; i++) {
        const img = await faceapi.fetchImage(`/assets/lib/face-api/labels/${folderName}/${i}.jpg`);
        const detections = await faceapi
          .detectSingleFace(img)
          .withFaceLandmarks()
          .withFaceDescriptor();
        descriptions.push(detections.descriptor);
      }
      return new faceapi.LabeledFaceDescriptors(folderName, descriptions);
    });
  
    return Promise.all(descriptionsPromises);
  };


Promise.all([    
    faceapi.nets.tinyFaceDetector.loadFromUri('/assets/lib/face-api/models'), // detectar rostos
    faceapi.nets.faceLandmark68Net.loadFromUri('/assets/lib/face-api/models'), // desenhar os tracos do rosto
    faceapi.nets.faceRecognitionNet.loadFromUri('/assets/lib/face-api/models'), // reconhecimento do rosto - quem sou eu?
    faceapi.nets.faceExpressionNet.loadFromUri('/assets/lib/face-api/models'), // detectar expressoes
    faceapi.nets.ageGenderNet.loadFromUri('/assets/lib/face-api/models'), // detectar idade/ genero
    faceapi.nets.ssdMobilenetv1.loadFromUri('/assets/lib/face-api/models'), // desenhar o quadrado em volta do rosto
]).then(startVideo)


cam.addEventListener('play', async () => {
    const canvas = faceapi.createCanvasFromMedia(cam)
    const canvasSize = {
        width: cam.width,
        height: cam.height
    }
    const labels = await loadLabels()
    faceapi.matchDimensions(canvas, canvasSize)
    document.body.appendChild(canvas)
    setInterval(async () => {
        const detections = await faceapi
            .detectAllFaces(
                cam, 
                new faceapi.TinyFaceDetectorOptions()
                )
            .withFaceLandmarks() // detectar as linhas do rosto
            .withFaceExpressions() // detectar as expressoes
            .withAgeAndGender() // detectar idade e sexo
            .withFaceDescriptors()   
        const resizedDetections = faceapi.resizeResults(detections, canvasSize)
        const faceMatcher = new faceapi.FaceMatcher(labels, 0.5)
        const results = resizedDetections.map(d =>
            faceMatcher.findBestMatch(d.descriptor)
        )
        //console.log(detections)
        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
        faceapi.draw.drawDetections(canvas, resizedDetections) // desenhar deteccao de rosto
        //faceapi.draw.drawFaceLandmarks(canvas, resizedDetections) // desenhar as linhas do rosto
        faceapi.draw.drawFaceExpressions(canvas, resizedDetections) // desenhar as expressoes
        resizedDetections.forEach(detection => {                    // desenhar idade e sexo
            const {age, gender, genderProbability} = detection
            const ageInt = parseInt(age, 10)
            new faceapi.draw.DrawTextField([
                `${ageInt} years`,
                `${gender} (${parseInt(genderProbability * 100, 10)})`
            ], detection.detection.box.topRight).draw(canvas)
        })
        results.forEach((result, index) => {
            const box = resizedDetections[index].detection.box
            const { label, distance } = result
            new faceapi.draw.DrawTextField([
                `${label} (${parseInt(distance * 100, 10)})`
            ], box.bottomRight).draw(canvas)
        })
    }, 0.1)
})