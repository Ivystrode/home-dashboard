<template>
  <h3>MainView</h3>
  <BarChart title="Temperature chart" :chartData="this.tempData" />
  <BarChart title="CO2 Levels" :chartData="this.co2Data" />

</template>

<script>
import { defineComponent } from 'vue';

// Components
// import HomePage from '../components/HomePage.vue'
import BarChart from '../components/Graph.vue'



export default defineComponent({
  name: 'MainView',

  components: {
    BarChart
  },
  data() {
    return {
      tempData: {
      labels: [],
      datasets: [{
        label: String,
        data: []
      }]
    },
      co2Data: {
      labels: [],
      datasets: [{
        label: String,
        data: []
      }]
    }
    }
  },
  methods : {
  async getGraphData() {
    const res = await fetch("http://localhost:5000/graphs")
    const data = await res.json()
    this.tempData = {
      labels: data.temperature.time,
      datasets: [{
        label: "Temperature (C)",
        data:data.temperature.level
      }]
    }
    this.co2Data = {
      labels: data.CO2.time,
      datasets: [{
        label: "CO2 Level (PPM)",
        data:data.CO2.level
      }]
    }
    console.log(this.tempData)
    console.log(this.co2Data)
    return data
  },
  },
  created() {
      this.getGraphData()
  }
});
</script>
