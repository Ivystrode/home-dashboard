<template>
<h1>{{title}}</h1>
  <p>{{chartData}}</p>
  <Line :chart-data="chartData" :chart-options="chartOptions" />
  <!-- <v-card color="grey-darken-2">uuuuuuu</v-card> -->
</template>

<script>
import { Line, Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale,
  Plugin,
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
  name: 'BarChart',
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
    console.log("mounted")
    console.log(this.chartData)
    console.log("endmounted")
  }
}
</script>
