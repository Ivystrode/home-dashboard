<template>
    <div class="main-container flex flex-row flex-wrap flex-grow mt-2 justify-center">
      <CamDetections :camDetections="camDetections"/>
    </div>
    
</template>

<script>
import CamDetections from '../components/CamDetections.vue'

export default {
    name: "DetectionsView",
    components: {
        CamDetections
    },
    methods: {
    async fetchDetections() {
      console.log("Getting detections")

      // USING MONGO ATLAS
      const res = await fetch("http://localhost:5000/get/detections") // change to /detections for using json server and /get for
      const data = await res.json()
      console.log(data)
      return data
    },
  },
    data() {
        return {
            camDetections: []
        }
    },
    async created() {
        this.camDetections = await this.fetchDetections()
    }
}
</script>

<style scoped>
</style>