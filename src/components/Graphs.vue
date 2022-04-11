<template>
    <h1>{{name}}</h1>
    <h1>{{this.chartdata}}</h1>
    <Line/>
</template>

<script>
// import VueCharts from 'vue-chartjs'
import Line from 'vue-chartjs'

export default {
  name: 'Graph',
  extends: Line,
  props: {
      name: String,
      graphData: Object
  },
  components: Line,
  data: () => ({
    loaded: false,
    chartdata: Object
  }),
  async created () {
    this.loaded = false

    try {
      // const { lineData } = await fetch(`http://localhost:5000/graphs/${this.name}`)
      // const lineData = await this.graphData
      this.chartdata = await this.graphData
      console.log("MOUNTED GRAPH COMP GOT:")
      console.log(this.chartdata)

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>