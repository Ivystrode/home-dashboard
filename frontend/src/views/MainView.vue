<template>
<div class="main-container flex flex-row flex-wrap flex-grow mt-2 justify-center">
  <Graph title="Temperature chart" :chartData="this.tempData" />
  <Graph title="CO2 Levels" :chartData="this.co2Data" />
</div>
</template>

<script>
import { defineComponent } from 'vue';

// Components
// import HomePage from '../components/HomePage.vue'
import Graph from '../components/Graph.vue'



export default defineComponent({
  name: 'MainView',

  components: {
    Graph
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
    const res = await fetch("http://localhost:5000/get") // remove the /get for using json server and use /graphs instead
    const received_data = await res.json()
    const data = received_data[0]['graphs'] // remove for using json server

    // Now do this dynamically ie for every graph in graphs add to data()
    this.tempData = {
      labels: data.temperature.time,
      datasets: [{
        label: "Temperature (C)",
        backgroundColor: '#E5747C',
        borderColor: '#E5747C',
        data:data.temperature.level
      }]
    }
    this.co2Data = {
      labels: data.CO2.time,
      datasets: [{
        label: "CO2 Level (PPM)",
        backgroundColor: '#91E0D5',
        borderColor: '#91E0D5',
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

<style scoped>
.main-container {
  text-align: center;
  margin-bottom: 10vh;
}
</style>