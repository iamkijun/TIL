<template>
  <div id="app">
    <h1>Kijun's Vuetube</h1>
    <img alt="Vue logo" src="./assets/logo.png" style="height: 100px">
    <the-search-bar
      @input-change="onInputChange"
    />
    <video-detail/>
    <video-list
      :app-to-list="videos"
    />
  </div>
</template>

<script>
import TheSearchBar from './components/TheSearchBar.vue';
import axios from 'axios'
import VideoDetail from './components/VideoDetail.vue';
import VideoList from './components/VideoList.vue';

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoDetail,
    VideoList,
  },
  data : function() {
    return {
      inputValue : "",
      API_KEY : 'AIzaSyArVhsxNQ9qF-Ew1CLq1PX79gcT4IlW5do',
      API_URL : 'https://www.googleapis.com/youtube/v3/search',
      videos: [],
    }
  },
  methods : {
    onInputChange(inputText) {
      this.inputValue = inputText

      const params = {
        key: this.API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue,
      }

      axios({
        method: 'get',
        url: this.API_URL,
        params
      })

        .then((res)=> {
          // console.log(res)
          this.videos = res.data.items
        })
        .catch((err)=> {
          console.log(err)
        })
      // console.log(inputText)
      // console.log("자식 컴포넌트로부터 이벤트 받음")
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
