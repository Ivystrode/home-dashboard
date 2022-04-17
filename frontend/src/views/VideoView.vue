<template>
    <!-- <div id="vid" class="main-container flex flex-row flex-grow justify-center m-2"> -->
    <div id="vid" class="video-container">

      <VideoFeeds :cameras="cameras" />

    </div>
      
</template>

<script>
import VideoFeeds from '../components/VideoFeeds.vue'

export default {
  name: "VideoView",
  components: {
    VideoFeeds
  },
  methods: {
    async fetchCameras() {
      console.log("getting cameras")
      const res = await fetch("http://localhost:5000/get/cameras")
      const data = await res.json()
      console.log(data)
      return data
    },
  },
    data() {
      return {
        cameras: []
      }
    },
    async created(){
      console.log("video view")
      this.cameras = await this.fetchCameras()
      console.log(this.cameras)
      console.log("end video fiew")
    }
}


</script>

<style scoped>
.camera-unit {
  border-style: hidden;
  border-width: 2px;
  border-radius: 3%;
  border-color: rgb(3, 43, 43);
  text-align: center;
}

.vid {
  /* border-top-left-radius: 3%;
  border-top-right-radius: 3%; */
  border-radius: 3%;
}

.unit-details {
  color: rgb(252, 228, 193);
}

.video-container {
  min-height: 100vh;
}

</style>