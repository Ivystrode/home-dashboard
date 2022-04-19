<template>
    <div id="borderbox" class="flex justify-center">
        <div id="detection-card" class="rounded-lg shadow-lg bg-slate-900 max-w-sm">
            <a href="#!" data-mdb-ripple="true" data-mdb-ripple-color="light">
            <img class="rounded-t-lg text-gray-200" :src="'http://' + camera.address + ':8080/?action=stream'" onerror="this.src='https://s3.envato.com/files/236638219/No%20signal%20590x332.jpg'" alt="No video feed detected"/>
            </a>
            <div class="p-6">
            <h5 class="text-gray-200 text-xl font-medium mb-2">{{camera.name}}</h5>
            <p class="text-gray-200 text-base mb-4">
                {{camera.type}}
            </p>
            <button type="button" class=" inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out ml-4">DETECT</button>
            <button type="button" class=" inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out ml-4">RECORD</button>
            <button type="button" class=" inline-block px-6 py-2.5 bg-red-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out ml-4">REBOOT</button>
            </div>
        </div>
    </div>
</template>



<script>

// RUNNING CAMERA FEED ON/FROM RASPBERRY PI
// USE COMMAND:
// ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"
// FROM WITHIN /MJPEG-STREAMER-EXPERIMENTAL FOLDER!!

export default {
    name: "VideoFeed",
    props: {
        camera: Object
    },
    async created() {

      console.log("video feed")
      console.log(this.camera)
      console.log("end video feed")
    }
}
</script>

<style scoped>
#borderbox {
    border-style: solid;
    border-width: 5px;
    border-radius: 3%;
    height: 450px;
    border-color: rgb(68, 122, 170);
    /* min-width: 380px; */
    /* min-height: 450px; */

}
#detection-card {
    min-width: 380px;
}
</style>