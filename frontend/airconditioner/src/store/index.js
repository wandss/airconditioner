import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    clockInterval: null,
    clock: '',
    options: ['Quiet', 'Two Steps', 'Fast', 'Comfort', 'Single User'],
    modes: ['Cool', 'Auto', 'Dry', 'Fan'],
    power: false,
    sideBar: {
      open: false,
      overlay: true,
      fullheight: true,
      fulwidth: true,
      right: true,
      label: '',
      type: 'is-light',
      items: []
    },
    profiles: [],
    control: {
      temperature: 16,
      mode: 'Cool',
      option: 'Quiet',
      swing: false
    },
    roomTemperature: null
  },
  getters: {
    control (state) {
      let control = state.control.mode + state.control.option + state.control.temperature
      const swing = state.control.swing ? 'swingOn' : 'swingOff'
      control = control + swing
      return control[0].toLocaleLowerCase() + control.slice(1, control.length)
    },
    roomTemp (state) {
      return state.toLocaleString()
    }
  },
  mutations: {
    setClock (state, payload) {
      state.clockInterval = setInterval(() => {
        state.clock = Intl.DateTimeFormat(navigator.language, {
          hour: 'numeric',
          minute: 'numeric',
          second: 'numeric'
        }).format()
      }, 1000)
    },
    setPower (state, payload) {
      state.power = !state.power
    },
    setSideBar (state, payload) {
      Object.assign(state.sideBar, payload)
    },
    setControl (state, payload) {
      Object.assign(state.control, payload)
    },
    setRoomTemperature (state, payload) {
      state.roomTemperature = payload
    }
  },
  actions: {
    startClock (context) {
      context.commit('setClock')
    },
    stopClock (context) {
      clearInterval(context.state.clockInterval)
    },
    setPower (context, payload) {
      const server = process.env.VUE_APP_API_SERVER_URL
      const api = process.env.VUE_APP_API_BASE
      const baseUrl = server + api
      // axios.put('http://billie:8000/api/v1/control/', payload)
      axios.put(baseUrl + '/control/', payload)
        .then(resp => {
          context.commit('setPower')
        })
        .catch(error => {
          console.log(error)
        })
    },
    setSwing (context, payload) {
      const server = process.env.VUE_APP_API_SERVER_URL
      const api = process.env.VUE_APP_API_BASE
      const baseUrl = server + api
      // axios.put('http://billie:8000/api/v1/control/', payload)
      axios.put(baseUrl + '/control/', payload)
        .then(resp => {
          context.commit('setSwing')
        })
        .catch(error => {
          console.log(error)
        })
    },
    updateControl (context, payload) {
      const server = process.env.VUE_APP_API_SERVER_URL
      const api = process.env.VUE_APP_API_BASE
      const baseUrl = server + api
      // axios.put('http://billie:8000/api/v1/control/', payload)
      console.log(payload)
      axios.put(baseUrl + '/control/', payload)
        .then(resp => {
          context.commit('setSwing') // REMOVE THIS
        })
        .catch(error => {
          console.log(error)
          console.log(payload)
          // context.commit('decreaseTemperature')
        })
    },
    fetchRoomTemperature (context, payload) {
      const server = process.env.VUE_APP_API_SERVER_URL
      const api = process.env.VUE_APP_API_BASE
      const baseUrl = server + api
      axios.get(baseUrl + '/temperature/')
        .then(resp => {
          context.commit('setRoomTemperature', resp.data.room_temperature)
        })
        .catch(error => {
          console.log(error.response)

          if (payload !== undefined && error.response.status === 404) {
            clearInterval(payload)
          }
        })
    }

    /*
    fetchPosts(context) {
       //TODO: pass the ordering Query string, dynamically through parameters
       axios.get('http://billie:8000/api/v1/blog/posts/?ordering=-create_date')
        .then(resp => {
            console.log('fetching new posts')
            context.commit('setPosts', resp.data)
        })
       .catch(error=>console.log(error))
    },
    */
  },
  modules: {
  }
})
