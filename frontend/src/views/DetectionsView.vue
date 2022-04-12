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
      const res = await fetch("http://localhost:5000/get") // change to /detections for using json server
      const data = await res.json()
      console.log(data[0]['detections'])

      return data[0]['detections']
    },
    async fetchDetection(id) {
      // I THINK THIS IS NOT USED FOR ANYTHING NOW AND WON'T WORK WITH THIS RIGHT NOW ANYWAY...
      const res = await fetch(`http://localhost:5000/get/detections/${id}`)
      const data = await res.json()
      console.log(data)

      return data
    }
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