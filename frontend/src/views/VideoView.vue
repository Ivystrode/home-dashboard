<template>
    <!-- <div id="vid" class="main-container flex flex-row flex-grow justify-center m-2"> -->
    <div id="vid" class="video-container">
      <VideoFeeds :cameras="cameras" @open-modal="openModal" />
    </div>

    <div v-if="toggleModal">
      <ScreenshotModal @close-modal="closeModal" :modalData="modalData"/>
    </div>
      
</template>

<script>
import VideoFeeds from '../components/VideoFeeds.vue'
import ScreenshotModal from '../components/ScreenshotModal.vue'

export default {
  name: "VideoView",
  components: {
    VideoFeeds,
    ScreenshotModal
  },
    data() {
      return {
        cameras: [],
        modalData: {},
        toggleModal: false
      }
    },
  methods: {
    async fetchCameras() {
      console.log("getting cameras")
      const res = await fetch("api/get/cameras")
      const data = await res.json()
      console.log(data)
      return data
    },
      openModal(id) {
      console.log("open modal")
      this.toggleModal = true
      this.modalData = this.cameras.filter((camera) => camera.id === id)
      console.log(this.modalData)
    },
      closeModal() {
          this.toggleModal = false
          this.modalData = {}
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