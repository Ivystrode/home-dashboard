<template>
<div class="flex flex-row flex-wrap flex-grow mt-2">
    <div v-for="camDetection in camDetections" :key="camDetection.id" class="flex flex-row flex-wrap flex-grow justify-center mt-2">
        <CamDetection :camDetection="camDetection"/>

    </div>
</div>

</template>

<script>
import CamDetection from './CamDetection.vue'

export default {
    name: "CamDetections",
    props: {
        camDetections: Array
    },
    components: {
        CamDetection
    }
}
</script>