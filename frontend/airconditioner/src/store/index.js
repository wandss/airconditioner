import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    options: ['Quiet', 'Two Steps', 'Fast', 'Comfort', 'Single User'],
    modes: ['Cool', 'Auto', 'Dry', 'Fan'],
    power: false,
    swing: false,
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
      option: 'Quiet'
    }
  },
  getters: {
    control (state) {
      const control = state.control.mode + state.control.option + state.control.temperature
      return control[0].toLocaleLowerCase() + control.slice(1, control.length)
    }
  },
  mutations: {
    increaseTemperature (state, payload) {
      Object.assign({ temperature: state.control.temperature++ }, state.control)
    },
    decreaseTemperature (state, payload) {
      Object.assign({ temperature: state.control.temperature-- }, state.control)
    },
    setPower (state, payload) {
      state.power = !state.power
    },
    setSwing (state, payload) {
      state.swing = !state.swing
    },
    setSideBar (state, payload) {
      Object.assign(state.sideBar, payload)
    },
    setControl (state, payload) {
      Object.assign(state.control, payload)
    }
  },
  actions: {
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
      axios.put(baseUrl + '/control/', payload)
        .then(resp => {
            context.commit('setSwing') //REMOVE THIS
        })
        .catch(error => {
          console.log(error)
          console.log(payload)
          // context.commit('decreaseTemperature')
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
