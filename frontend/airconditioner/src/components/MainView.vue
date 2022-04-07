<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">
        AIR Conditioner Name Here
      </p>
      <button class="card-header-icon" aria-label="more options">
        <span class="icon">
          <i class="fas fa-angle-down" aria-hidden="true"></i>
        </span>
      </button>
    </header>
    <div class="card-content">
      <div class="content">
        <h1>
          Background
        </h1>
        <br>
        <br>
          <h1>
          {{ temperature }} C
          </h1>
        <section>
          <b-button size="is-default" @click="temperature--"
          :disabled="temperature==16?true:false">
           Down 
          </b-button>
          <b-button size="is-default" @click="temperature++"
          :disabled="temperature==27?true:false"
          >
           Up
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
         <b-switch type="is-success">
           Power
         </b-switch>
       </b-field>
      </section>
      <a href="#" class="card-footer-item">Save</a>
      <a href="#" class="card-footer-item">Modes</a>
      <a href="#" class="card-footer-item">Settings</a>
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
      temperature: 16,
      modes: ['Cool', 'Fan', 'Dry'],
      activeMode: 0,
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
        second: 'numeric'
      }).format()
    }, 1000)
  }
}
</script>
