import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store'
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
  },
  mutations: {
    // actions와 차이를 두기 위해 대문자로
    CHANGE_MESSAGE(state, newMessage){
      // console.log(state)
      // console.log(newMessage)
      state.message = newMessage
    }
  },
  actions: {
    changeMessage(context, newMessage) {
      // console.log(context.state.message)
      // console.log(newMessage)
      context.commit('CHANGE_MESSAGE', newMessage)
    }
  },
  modules: {
  }
})
