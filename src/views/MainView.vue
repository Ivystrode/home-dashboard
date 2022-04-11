<template>
  <h3>MainView</h3>
  <Graph title="Linesss" :graphData="this.graphData" name="TEMP"/>

</template>

<script>
import { defineComponent } from 'vue';

// Components
// import HomePage from '../components/HomePage.vue'
import Graph from '../components/Graphs.vue'



export default defineComponent({
  name: 'MainView',

  components: {
    Graph
  },
  methods : {
  async getGraphData() {
    const res = await fetch("http://localhost:5000/graphs")
    const data = await res.json()
    console.log("MAINVIEW COMPFETCH")
    console.log(data)
    console.log("MAINVIEW COMP END")
    return data
  },
  },
  async created() {
      this.graphData = await this.getGraphData()
      console.log("mvc component get graphs:")
      console.log(this.graphData)
      // console.log(this.co2Graph)
      console.log("mvc component got graphs+")
  }
});
</script>
