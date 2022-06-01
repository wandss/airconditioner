<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">
        Samsung: {{ $store.getters.control }}
      </p>
      <button class="card-header-icon" aria-label="more options">
        <span class="icon">
          <i class="fas fa-angle-down" aria-hidden="true"></i>
          <fa-icon icon="angle-down" />
        </span>
      </button>
    </header>
    <div class="card-content">
      <div class="content" id="background">
        <h3 id="background" v-if="$store.state.roomTemperature !== null">
          Room Temperature: {{$store.state.roomTemperature}} C
        </h3>
        <h1 id="temperature" >
          {{ $store.state.control.temperature }} C
        </h1>
        <p>
          {{ $store.state.control.mode }} /
          {{ $store.state.control.option }}
        </p>
        <section>
          <b-button size="is-default"
          @click="handleControl('decreaseTemperature')"
          :disabled="$store.state.control.temperature==16?true:false">
          <fa-icon icon="angle-down" />
           Down
          </b-button>
          <b-button size="is-default"
          @click="handleControl('increaseTemperature')"
          :disabled="$store.state.control.temperature==30?true:false"
          >
           Up
          <fa-icon icon="angle-up" />
          </b-button>
        </section>
        <br>
        <br>
        <time datetime="2016-1-1">
          {{ $store.state.clock }}
        </time>
      </div>
    </div>
    <footer class="card-footer">
      <section class="card-footer-item">
       <b-field>
         <b-switch type="is-success" @input="handlePower"
         :value="$store.state.power" >
           Power
         </b-switch>
       </b-field>
      </section>
      <section class="card-footer-item">
       <b-field>
         <b-switch type="is-default" @input="handleControl('swing')"
          :value="$store.state.control.swing"
         >
           Swing
         </b-switch>
       </b-field>
      </section>
    </footer>
    <footer class="card-footer">
      <section class="card-footer-item">
      <a href="#" class="card-footer-item">Save</a>
      <a href="#" class="card-footer-item"
       @click="handleSideBar($store.state.modes, 'Modes')">
        Modes
      </a>
      <a href="#" class="card-footer-item"
       @click="handleSideBar($store.state.options, 'Options')">Options</a>
      </section>
    </footer>
  </div>
</template>
<script>
export default {
  name: 'MainVIew',
  data () {
    return {
      roomTemperatureInterval: null
    }
  },
  beforeDestroy () {
    this.$store.dispatch('stopClock')
    clearInterval(this.roomTemperatureInterval)
  },
  created () {
    this.$store.dispatch('startClock')
    this.roomTemperatureInterval = setInterval(() => {
      this.$store.dispatch('fetchRoomTemperature', this.roomTemperatureInterval)
    }, 10000)
    this.$store.dispatch('startClock')
  },
  methods: {
    handleSideBar (items, label) {
      this.$store.commit('setSideBar',
        {
          open: true,
          label: label,
          items: items
        })
    },
    handlePower () {
      const power = this.$store.state.power ? 'off' : 'on'
      this.$store.dispatch('setPower', { command: power })
    },
    handleControl (action) {
      const control = Object.assign({}, this.$store.state.control)
      if (action === 'increaseTemperature') {
        control.temperature++
      } else if (action === 'decreaseTemperature') {
        control.temperature--
      } else if (action === 'swing') {
        control.swing = !control.swing
      }
      this.$store.commit('setControl', control)
      this.$store.dispatch('updateControl',
        { command: this.$store.getters.control })
    }

  }
}
</script>
<style>
#background {
  background: rgb(2,0,36);
  background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(130,130,140,1) 46%, rgba(77,114,198,1) 100%);
  color: white;
  text-shadow: 1px 3px 4px #444;
}
#temperature {
  color: white;
  text-shadow: 9px 15px 9px #444;
  font-size: 70px;
}

</style>
