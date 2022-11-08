<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <h2>{{ messageLength }}</h2>
    <h3>{{ doubleLength }}</h3>
    <input type="text" @keyup.enter="chagneMessage" v-model="inputData">
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      inputData: null,
    }
  },
  computed : {
    message() {
      return this.$store.state.message
    },
    messageLength() {
      return this.$store.getters.messageLength
    },
    doubleLength() {
      return this.$store.getters.doubleLength
    }
  },
  methods: {
    chagneMessage() {
      this.$store.dispatch('changeMessage', this.inputData)
      this.inputData = null
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
