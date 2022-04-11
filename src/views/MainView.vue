<template>
  <h3>MainView</h3>
  <BarChart :chartData="this.tempData" />

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
        labels: ["1","2","3"],
        datasets: [4,5,6]
      },
      co2Data:  {
        labels: [1,2,3],
        datasets: [4,5,6]
      },
    }
  },
  methods : {
  async getGraphData() {
    const res = await fetch("http://localhost:5000/graphs")
    const data = await res.json()
    this.tempData = {
      labels: data.temperature.time,
      datasets: data.temperature.level
    }
    this.co2Data = {
      labels: data.CO2.time,
      datasets: data.CO2.level
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
