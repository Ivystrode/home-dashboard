<template>
  <div class="chart-container text-center">
    <h1>{{title}}</h1>
    <Line :chart-data="chartData" :chart-options="chartOptions" />
  </div>
</template>

<script>
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale
);

export default {
  name: 'Graph',
  components: { Line },
  props: {
    title: String,
    chartData: {
        type: Object,
        required: true,
        responsive: true
      },
    chartOptions: {
      type: Object,
      default: () => {}
    }
  },
  mounted() {
    // console.log("mounted")
    console.log(this.chartData)
    // console.log("endmounted")
  }
}
</script>

<style scoped>
.chart-container {
  width: 60vh;
  height: 60vh;
}
Line {
  background-color: black;
}
</style>