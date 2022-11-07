<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>모든 Todo 개수: {{ allTodosCount }}</h2>
    <h2>완료한 Todo 개수: {{ completedTodosCount }}</h2>
    <h2>미완료한 Todo 개수: {{ uncompletedTodosCount }}</h2>
    <todo-list/>
    <todo-form/>
    <button @click="loadTodos">Todo 불러오기</button>
  </div>
</template>

<script>
import TodoForm from './components/TodoForm.vue'
import TodoList from './components/TodoList.vue'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  computed: {
    allTodosCount(){
      return this.$store.getters.allTodosCount
    },
    completedTodosCount() {
      return this.$store.getters.completedTodosCount
    },
    uncompletedTodosCount() {
      return this.$store.getters.uncompletedTodosCount
    }
  },
  methods: {
    loadTodos() {
      this.$store.dispatch('loadTodos')
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
