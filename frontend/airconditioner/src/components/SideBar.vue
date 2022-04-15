<template>
  <section>
    <b-sidebar
      type="is-light"
      :fullheight="fullheight"
      :fullwidth="fullwidth"
      :overlay="overlay"
      :right="right"
      v-model="open"
    >
      <div class="p-1">
        <b-menu>
          <b-menu-list :label="label">
            <b-menu-item icon="information-outline" 
              v-for="mode in
              $store.state.modes" :label="mode">
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
      open: true,
      overlay: true,
      fullheight: true,
      fullwidth: true,
      right: true,
      label: 'ADD TEXT HERE',
    };
  }
};
</script>

<style>
.p-1 {
  padding: 1em;
}
</style>
