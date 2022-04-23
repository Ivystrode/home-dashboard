<template>
<div class="flex flex-row flex-wrap flex-grow mt-2">
    <div v-for="camera in cameras" :key="camera.id" class="flex flex-grow justify-center mt-2">
        <VideoFeed :camera="camera" @open-modal="$emit('open-modal', camera.id)" />

    </div>
</div>

</template>

<script>
import VideoFeed from './VideoFeed.vue'

export default {
    name: "VideoFeeds",
    props: {
        cameras: Array
    },
    components: {
        VideoFeed
    },
    emits: [
        'open-modal'
    ]
    // async mounted() {

    //   console.log("video feeds")
    //   console.log(this.cameras)
    //   console.log("end video feeds")
    // }
}
</script>