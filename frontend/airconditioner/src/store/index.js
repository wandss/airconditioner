import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
      temperature: 16,
      options: ['Quiet', 'Two Steps', 'Fast', 'Comfort', 'Single User'],
      power: false,
      sideBar: {
          open: false,
          overlay: true,
          fullheight: true,
          fulwidth: true,
          right: true,
          label: '',
          type: 'is-light',
          items: [],
      },
      profiles: [],
  },
  getters: {
  },
  mutations: {
      increaseTemperature(state, payload) {
          state.temperature ++
      },
      decreaseTemperature(state, payload) {
          state.temperature --
      },
      setPower(state, payload) {
          state.power = !state.power
      },
      setSideBar(state, payload) {
          Object.assign(state.sideBar, payload)

      },
      setProfiles(state, payload) {
          state.profiles = payload
      }

  },
  actions: {
    fetchProfiles(context) {
        axios.get('http://billie:8000/api/v1/control/profiles')
         .then(resp=>{
             context.commit('setProfiles', resp.data)
         })
        .catch(error=>console.log(error))
    },
    sendCommand(context, payload) {
        axios.put('http://billie:8000/api/v1/control/', payload)
        .then(resp=>{
            console.log(resp.data)
            context.commit('setPower')
        })
        .catch(error=>console.log(error))
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
