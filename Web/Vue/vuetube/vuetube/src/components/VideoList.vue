<template>
  <div>
    <h1>Video List</h1>
    <video-list-item
      :item-to-list="listGetEvent"
    />
  </div>  
</template>

<script>
import VideoListItem from './VideoListItem.vue'
export default {
  name : 'VideoList',
  components : {
    VideoListItem,
  },
  props : {
    appToList : Array,
  }
  ,
  methods: {
    listGetEvent: function() {
      console.log("자식 컴포넌트에서 발생한 이벤트!")
    },
  }
}
</script>

<style>

</style>