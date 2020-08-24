<template>
  <div class="home">
    <LoadingScreen msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import LoadingScreen from "@/components/LoadingScreen.vue";
//import LoadingScreen from "../components/LoadingScreen";

export default {
  name: "home",
  components: {
    LoadingScreen,
  },
};
</script>
