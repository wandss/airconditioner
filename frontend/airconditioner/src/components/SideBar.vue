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
              v-for="item in $store.state.sideBar.items"
              :key="item" @click="handleChange(item)"
              :label="item">
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
  data () {
    return {
    }
  },
  methods: {
    handleChange (item) {
    // USE Objects.indexOf with state.options
    // or state.modes instead of label
      if (this.$store.state.sideBar.label === 'Modes') {
        this.$store.commit('setControl',
          { mode: item })
      } else {
        this.$store.commit('setControl',
          { option: item })
      }
    }
  }
}
</script>

<style>
.p-1 {
  padding: 1em;
}
</style>
