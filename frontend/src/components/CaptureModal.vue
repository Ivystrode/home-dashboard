<template>
    <div class="fixed inset-0 bg-gray-600 bg-opacity-75 overflow-y-auto h-full w-full" id="my-modal">
        <div id="the-modal" class="relative top-20 mx-auto p-5 w-3/4 shadow-lg rounded-md bg-slate-900">
            <div class="mt-3 text-center">

                <img :src="'http://' + modalData[0].address + ':8080/?action=snapshot'" class="inline">
                <p class="text-2xl leading-6 font-medium text-gray-200 mt-3">
                    <span class="font-bold">Name:</span> {{modalData[0].name}}
                </p>
                <p class="text-2xl leading-6 font-medium text-gray-200 mt-3">
                    <span class="font-bold">Unit Type:</span> {{modalData[0].type}}
                </p>
                <p class="text-2xl leading-6 font-medium text-gray-200 mt-3">
                    <span class="font-bold">Status:</span> {{modalData[0].status}}
                </p>

                <div class="items-center px-4 py-3">

                    <button @click="$emit('close-modal')" id="ok-btn"
                    class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out ml-4 mt-2">DOWNLOAD
                    </button>

                    <button @click="$emit('close-modal')" id="ok-btn"
                    class=" inline-block px-6 py-2.5 bg-red-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg transition duration-150 ease-in-out ml-4 mt-2">DISCARD
                    </button>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CaptureModal',
    props: {
        modalData: Object
    },
    emits: [
        'close-modal'
    ]
}
</script>

<style scoped>
#the-modal {
    border-style: solid;
    border-width: 5px;
    border-radius: 3%;
    border-color: rgb(68, 122, 170);
    max-width: 750px;
    /* min-width: 95vw; */
    
}
</style>