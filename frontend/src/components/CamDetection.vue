<template>
    <div id="borderbox" class="flex justify-center">
        <div id="detection-card" class="rounded-lg shadow-lg text-gray-200 bg-slate-900 max-w-sm">
            <a href="#!" data-mdb-ripple="true" data-mdb-ripple-color="light">
            <img class="rounded-t-lg" :src="camDetection.image" alt=""/>
            </a>
            <div id="descbox" class="p-6">
            <h5 class="text-gray-200 text-xl font-medium mb-2">{{camDetection.type}}</h5>
            <p class="text-gray-200 text-base mb-4">
                {{camDetection.detection_unit}}
            </p>
            <button type="button" class=" inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Button</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "CamDetection",
    props: {
        camDetection: Object
    },
    methods: {
        renderImage(src) {
            let img = new Image()
            img.src = 'data:image/jpeg;base64,'+src
            return img
        }
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
    /* opacity: 50%; */
    /* min-height: 450px; */

}

#borderbox:hover {
    scale: 102%;
}

#detection-card {
    opacity: 100%;
}

</style>