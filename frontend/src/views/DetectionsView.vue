<template>
  <div class="detections-container">

      <CamDetections :camDetections="camDetections"/>
      
    <div v-if="this.loading" class="loading-spinner justify-center flex">

      <h1>LOADING DETECTIONS...</h1>
      	<div id="loading">
		      <div class="loading-dot"></div>
	      </div>

    </div>

    <!-- </div> -->
    <!-- <div v-if="this.loading" class="filler">

    </div> -->

  </div>
    
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

      // USING MONGO ATLAS
      const res = await fetch("api/get/detections") // change to /detections for using json server and /get for
      const data = await res.json()
      console.log(data)
      this.loading = false
      console.log(this.loading)
      return data
    },
  },
    data() {
        return {
            camDetections: [],
            loading: Boolean
        }
    },
    async created() {
        this.loading = true
        console.log(this.loading)
        this.camDetections = await this.fetchDetections()
    }
}
</script>

<style scoped>
.loading-spinner {
  color: white;
  margin-top: 25vh;
}
/* .filler {
  min-height: 600px;
  margin-top: 100px;
} */
.detections-container {
  min-height: 100vh;
}






body{
  margin: 0;
  overflow: hidden;
}

.drawing{
    width: 100vw;
    height: 100vh;
    position: relative;
    display: block;
    background-color: #3a3a3a;
}




/* -- Loading thingy 2 --*/
.loading-dot {
    border-radius:100%;
    height:10px;
    width:10px;
    background-color: #ffffff;
    position:absolute;
    left:0;
    right:0;
    margin:auto;
    margin-top: 50vh;
    top:0;
    bottom:0;
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
    -webkit-animation: load 3s infinite linear;
    -moz-animation: load 3s infinite linear;
    -o-animation: load 3s infinite linear;
    animation:load 3s infinite linear;
}


@-webkit-keyframes load {
  0%   {
    -webkit-transform: translate(0px,0px),rotate(0deg); 
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

  25%{
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    -40px -40px 0px 0px #ffffff,40px 40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff;
  }

  50%{
    box-shadow: 0px -40px 0px 0px #ffffff,0px 40px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,
    -40px -40px 0px 0px #ffffff,40px 40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff;
  }

  70%{
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
  }

  75%{
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    height:10px;
    width:10px;
  }

  80%{
    -webkit-transform: translate(0px,0px) rotate(360deg); 
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff;
    height:40px;
    width:40px;
  }

  85%{
    -webkit-transform: translate(0px,0px) rotate(360deg);
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff; 
    height:40px;
    width:40px;
  }

  90%{
    -webkit-transform: translate(0px,0px) rotate(360deg); 
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff; 
    height:10px;
    width:10px;
  }

  95{
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

  100%{
    -webkit-transform: rotate(360deg);
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

}

@-moz-keyframes load {
  0%   {
    -moz-transform: translate(0px,0px),rotate(0deg); 
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

  25%{
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    -40px -40px 0px 0px #ffffff,40px 40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff;
  }

  50%{
    box-shadow: 0px -40px 0px 0px #ffffff,0px 40px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,
    -40px -40px 0px 0px #ffffff,40px 40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff;
  }

  70%{
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
  }

  75%{
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    height:10px;
    width:10px;
  }

  80%{
    -moz-transform: translate(0px,0px) rotate(360deg); 
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff;
    height:40px;
    width:40px;
  }

  85%{
    -moz-transform: translate(0px,0px) rotate(360deg);
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff; 
    height:40px;
    width:40px;
  }

  90%{
    -moz-transform: translate(0px,0px) rotate(360deg); 
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff; 
    height:10px;
    width:10px;
  }

  95{
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

  100%{
    -moz-transform: rotate(360deg);
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

}

@keyframes load {
  0%   {
    transform: translate(0px,0px),rotate(0deg); 
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

  25%{
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    -40px -40px 0px 0px #ffffff,40px 40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff;
  }

  50%{
    box-shadow: 0px -40px 0px 0px #ffffff,0px 40px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,
    -40px -40px 0px 0px #ffffff,40px 40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff;
  }

  70%{
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
  }

  75%{
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    height:10px;
    width:10px;
  }

  80%{
    transform: translate(0px,0px) rotate(360deg); 
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff;
    height:40px;
    width:40px;
  }

  85%{
    transform: translate(0px,0px) rotate(360deg);
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff; 
    height:40px;
    width:40px;
  }

  90%{
    transform: translate(0px,0px) rotate(360deg); 
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff; 
    height:10px;
    width:10px;
  }

  95{
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

  100%{
    transform: rotate(360deg);
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

}
@-o-keyframes load {
  0%   {
    -o-transforms: translate(0px,0px),rotate(0deg); 
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

  25%{
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    -40px -40px 0px 0px #ffffff,40px 40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff;
  }

  50%{
    box-shadow: 0px -40px 0px 0px #ffffff,0px 40px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,
    -40px -40px 0px 0px #ffffff,40px 40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff;
  }

  70%{
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
  }

  75%{
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    height:10px;
    width:10px;
  }

  80%{
    -o-transforms: translate(0px,0px) rotate(360deg); 
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff;
    height:40px;
    width:40px;
  }

  85%{
    -o-transforms: translate(0px,0px) rotate(360deg);
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff; 
    height:40px;
    width:40px;
  }

  90%{
    -o-transforms: translate(0px,0px) rotate(360deg); 
    box-shadow: 0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,
    0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff,0px 0px 0px 0px #ffffff;
    background-color: #ffffff; 
    height:10px;
    width:10px;
  }

  95{
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

  100%{
    -o-transforms: rotate(360deg);
    box-shadow: 0px 40px 0px 0px #ffffff,0px -40px 0px 0px #ffffff,40px 0px 0px 0px #ffffff,-40px 0px 0px 0px #ffffff,
    40px 40px 0px 0px #ffffff,-40px -40px 0px 0px #ffffff,40px -40px 0px 0px #ffffff,-40px 40px 0px 0px #ffffff;
  }

}

</style>