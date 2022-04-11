<template>
<h1>sss</h1>
  <Bar :chart-data="chartData" :chart-options="chartOptions" />
  <p>{{chartData}}</p>
  <h1>www</h1>
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
    chartData: {
        type: Object,
        required: true
      },
    chartOptions: {
      type: Object,
      default: () => {}
    }
  },
  mounted() {
    console.log("mounted")
  }
}
</script>
