function startRecord(){

    const constraints = {video : {
        width : 480,
        height : 360
    }}

    navigator.mediaDevices.getUserMedia(constraints).then(stream=>{
        const videoElement = document.querySelector("#foto");
        videoElement.srcObject = stream;
    }).catch(err =>{
        console.log(err);
    })

    

}

window.addEventListener("DOMContentLoaded", startRecord)
