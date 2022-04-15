import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
      temperature: 16,
      modes: ['Cool', 'Fan', 'Dry', 'Auto'],
      options: ['Quiet', 'Two Steps', 'Fast', 'Comfort', 'Single User'],
      power: false,
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
      }
  },
  actions: {
  },
  modules: {
  }
})
