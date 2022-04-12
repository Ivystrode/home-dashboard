<template>
    <div id="vid" class="main-container flex flex-row flex-grow justify-center m-2">

      <!-- for camera in cameras - show each feed -->
      <div class="camera-unit m-3">
        <img class="vid" src="http://192.168.1.117:8081">
        <div class="unit-details">
          <p>Unit Name: HomeCam1</p>
          <p>Unit Details: Something else</p>          
        </div>
      </div>

      <div class="camera-unit m-3">
        <img class="vid" src="http://192.168.1.117:8081">
        <div class="unit-details">
          <p>Unit Name: HomeCam1</p>
          <p>Unit Details: Something else</p>          
        </div>
      </div>

    </div>
      
</template>

<script>
export default {

}
</script>

<style scoped>
.camera-unit {
  border-style: hidden;
  border-width: 2px;
  border-radius: 3%;
  border-color: rgb(3, 43, 43);
  text-align: center;
}

.vid {
  /* border-top-left-radius: 3%;
  border-top-right-radius: 3%; */
  border-radius: 3%;
}

.unit-details {
  color: rgb(252, 228, 193);
}

</style>