function startRecord(){

    const constraints = {video : {
        width : 480,
        height : 360
    }}

    navigator.mediaDevices.getUserMedia(constraints).then(stream=>{
        const videoElement = document.querySelector("video");
        videoElement.srcObject = stream;
    })
}

function takePicture(){
    const video = document.querySelector('video');
    const canvas = document.querySelector('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convert the canvas image to a data URL
    const dataURL = canvas.toDataURL();

    // Create a Blob object from the data URL
    const blob = dataURLtoBlob(dataURL);

    // Create a File object from the Blob
    const file = new File([blob], 'image.jpg', { type: 'image/jpeg' });

    // Set the value of the input type file to the File object
    const input = document.querySelector('input[type="file"]');
    const dataTransfer = new DataTransfer()
    dataTransfer.items.add(file)
    input.files = dataTransfer.files;
}

// Helper function to convert data URL to Blob
function dataURLtoBlob(dataURL) {
    const parts = dataURL.split(';base64,');
    const contentType = parts[0].split(':')[1];
    const raw = window.atob(parts[1]);
    const rawLength = raw.length;
    const uInt8Array = new Uint8Array(rawLength);
    for (let i = 0; i < rawLength; ++i) {
      uInt8Array[i] = raw.charCodeAt(i);
    }
    return new Blob([uInt8Array], { type: contentType });
  }

window.addEventListener("DOMContentLoaded", startRecord)
