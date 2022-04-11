<template>
    <h1>DETECTIONS VIEW</h1>
    <CamDetections :camDetections="camDetections"/>
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
      const res = await fetch("http://localhost:5000/detections")
      const data = await res.json()
      console.log(data)

      return data
    },
    async fetchDetection(id) {
      const res = await fetch(`http://localhost:5000/detections/${id}`)
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
