import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
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
    }
  },
  getters: {
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
    setSideBar (state, payload) {
      Object.assign(state.sideBar, payload)
    },
    setControl (state, payload) {
      Object.assign(state.control, payload)
    }
  },
  actions: {
    sendCommand (context, payload) {
      axios.put('http://billie:8000/api/v1/control/', payload)
        .then(resp => {
          console.log(resp.data)
          context.commit('setPower')
        })
        .catch(error => console.log(error))
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
