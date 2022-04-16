<template>
  <div class="container">
     <MainView />
     <SideBar />
  </div>
</template>
<script>
import MainView from '@/components/MainView.vue'
import SideBar from '@/components/SideBar.vue'
export default {
  name: 'AirConditioner',
  components: {MainView, SideBar},
  mounted() {
    this.$store.dispatch('fetchProfiles')
  }
}
</script>
