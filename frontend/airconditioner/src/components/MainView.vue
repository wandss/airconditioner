<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">
        AIR Conditioner Name Here
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
        <h1 id="background">
          Background
        </h1>
        <h1 id="temperature" >
          {{ $store.state.temperature }} C
        </h1>
        <section>
          <b-button size="is-default"
          @click="$store.commit('decreaseTemperature', '')"
          :disabled="$store.state.temperature==16?true:false">
          <fa-icon icon="angle-down" />
           Down 
          </b-button>
          <b-button size="is-default"
          @click="$store.commit('increaseTemperature', '')"
          :disabled="$store.state.temperature==30?true:false"
          >
           Up
          <fa-icon icon="angle-up" />
          </b-button>
        </section>
        <br>
        <br>
        <time datetime="2016-1-1">
          {{ time }}
        </time>
      </div>
    </div>
    <footer class="card-footer">
      <section class="card-footer-item">
       <b-field>
         <b-switch type="is-success" @input="$store.commit('setPower')"
         :value="$store.state.power" >
           Power 
         </b-switch>
       </b-field>
      </section>
      <section class="card-footer-item">
       <b-field>
         <b-switch type="is-default">
           Swing
         </b-switch>
       </b-field>
      </section>
    </footer>
    <footer class="card-footer">
      <section class="card-footer-item">
      <a href="#" class="card-footer-item">Save</a>
      <a href="#" class="card-footer-item">Modes</a>
      <a href="#" class="card-footer-item">Settings</a>
      </section>
    </footer>
  </div>
</template>
<script>
export default {
  name: 'MainVIew',
  data() {
    return {
      interval: null,
      time: null,
    }
  },
  beforeDestroy() {
    clearInterval(this.inverval)
  },
  created() {
     // update the time every second
    this.interval = setInterval(() => {
      // Concise way to format time according to system locale.
      // In my case this returns "3:48:00 am"
      this.time = Intl.DateTimeFormat(navigator.language, {
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric' }).format()
    }, 1000)
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
