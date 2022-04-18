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

    // USING MONGODB ATLAS

    // Temperature
    console.log("get data")
    const temp_res = await fetch("api/get/temp")
    const temp_data = await temp_res.json()
    console.log(temp_data)

    let temp_times = []
    let temp_levels = []
    for (let i=0; i<temp_data.length; i++) {
      console.log(temp_data[i])
      temp_times[i] = temp_data[i]['time']
      temp_levels[i] = temp_data[i]['level']
    }
    console.log(temp_times)

    // CO2
    const co2_res = await fetch("api/get/co2")
    const co2_data = await co2_res.json()
    console.log(co2_data)
    let co2_times = []
    let co2_levels = []
    for (let i=0; i<co2_data.length; i++) {
      console.log(co2_data[i])
      co2_times[i] = co2_data[i]['time']
      co2_levels[i] = co2_data[i]['level']
    }
    console.log(temp_times)

    console.log("got data")

    // USING MONGODB LOCAL
    // const res = await fetch("http://localhost:5000/get") // remove the /get for using json server and use /graphs instead
    // const received_data = await res.json()
    // const data = received_data[0]['graphs'] // remove for using json server

    // USING JSON SERVER - TESTING ONLY
    // const res = await fetch("http://localhost:5000/graphs") // remove the /get for using json server and use /graphs instead
    // const data = await res.json()

    // Now do this dynamically ie for every graph in graphs add to data()
    this.tempData = {
      labels: temp_times,
      datasets: [{
        label: "Temperature (C)",
        backgroundColor: '#E5747C',
        borderColor: '#E5747C',
        data:temp_levels
      }]
    }
    this.co2Data = {
      labels: co2_times,
      datasets: [{
        label: "CO2 Level (PPM)",
        backgroundColor: '#91E0D5',
        borderColor: '#91E0D5',
        data:co2_levels
      }]
    }
    console.log(this.tempData)
    console.log(this.co2Data)
    return [temp_data, co2_data]
  },
  },
  created() {
      this.getGraphData()
      // console.log(t)
  }
});
</script>

<style scoped>
/* .main-container {
  text-align: center;
  margin-bottom: 10vh;
} */
</style>