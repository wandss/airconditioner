<template>
  <section>
    <b-sidebar
      :type="$store.state.sideBar.type"
      :fullheight="$store.state.sideBar.fullheight"
      :fullwidth="$store.state.sideBar.fullwidth"
      :overlay="$store.state.sideBar.overlay"
      :right="$store.state.sideBar.right"
      v-model="$store.state.sideBar.open"
    >
      <div class="p-1">
        <b-menu>
          <b-menu-list :label="$store.state.sideBar.label">
            <b-menu-item icon="information-outline" 
              v-for="item in
              $store.state.sideBar.items" :label="item">
            </b-menu-item>
          </b-menu-list>
        </b-menu>
      </div>
    </b-sidebar>
  </section>
</template>

<script>
export default {
  name: 'SideBar',
  data() {
    return {
    };
  }
};
</script>

<style>
.p-1 {
  padding: 1em;
}
</style>
