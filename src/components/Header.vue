<template>
    <nav class="
        relative
        w-full
        flex flex-wrap
        items-center
        justify-between
        py-4
        bg-gray-900
        text-gray-500
        hover:text-gray-700
        focus:text-gray-700
        shadow-lg
        navbar navbar-expand-lg navbar-light
        ">
    <div class="container-fluid w-full flex flex-wrap items-center justify-between px-6">
        <button class="
            navbar-toggler
            text-gray-500
            border-0
            hover:shadow-none hover:no-underline
            py-2
            px-2.5
            bg-transparent
            focus:outline-none focus:ring-0 focus:shadow-none focus:no-underline" 
            type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="bars"
        class="w-6" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
        <path fill="currentColor"
            d="M16 132h416c8.837 0 16-7.163 16-16V76c0-8.837-7.163-16-16-16H16C7.163 60 0 67.163 0 76v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16z">
        </path>
        </svg>
        </button>
        <div class="collapse navbar-collapse flex-grow items-center" id="navbarSupportedContent">
            <p class="text-xl text-white margin-right:50" href="#">DASHBOARD</p>
            <!-- Left links -->
            <ul class="navbar-nav flex flex-col pl-0 list-style-none mr-auto">
                <li class="nav-item px-2">
                    <router-link class="nav-link text-white opacity-60 hover:opacity-80 focus:opacity-80 p-0" to="/">Home</router-link>
                </li>
                <li class="nav-item px-2">
                    <router-link class="nav-link text-white opacity-60 hover:opacity-80 focus:opacity-80 p-0" to="detections">Detections</router-link>
                </li>
            </ul>
            <!-- Left links -->
        </div>
    <!-- Collapsible wrapper -->
    </div>
    </nav>
</template>

<script>

    export default {
        name: 'Header',
        props: {
            title: String
        }
        }
</script>

<style scoped>
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
        }
</style>