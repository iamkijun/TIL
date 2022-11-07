import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: [],
  },
  getters: {
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state){
      // 1. 완료된 투두만 모아놓은 새로운 배열 생성
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted === true
      })
      // 2. 그 새로운 배열의 길이를 반환
      return completedTodos.length
    },
    uncompletedTodosCount(state){
      // 1. 완료된 투두만 모아놓은 새로운 배열 생성
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted === false
      })
      // 2. 그 새로운 배열의 길이를 반환
      return completedTodos.length
    },
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS(state,todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
    LOAD_TODOS(state) {
      const localStorageTodos = localStorage.getItem('todos')
      const parsedTodos = JSON.parse(localStorageTodos)
      state.todos =parsedTodos
    }
  },
  actions: {
    createTodo(context, todoTitle) {
      // Todo 객체 만들기
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      // console.log(todoItem)
      context.commit('CREATE_TODO',todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    deleteTodo(context, todoitem){
      context.commit('DELETE_TODO', todoitem)
      context.dispatch('saveTodosToLocalStorage')
    },
    updateTodoStatus(context,todoItem) {
      context.commit('UPDATE_TODO_STATUS',todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    saveTodosToLocalStorage(context) {
      const jsonTodos = JSON.stringify(context.state)
      localStorage.setItem('todos',jsonTodos)
    },
    loadTodos(context) {
      context.commit('LOAD_TODOS')
    }
  },
  modules: {
  }
})
