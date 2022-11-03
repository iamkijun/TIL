<template>
  <div>
    <input type="text" @keyup.enter="onInputKeyword">
    <video-list-item
      @list-to-item="showItems"
    />
  </div>
</template>

<script>
export default {
  name : 'TheSearchBar',
  methods : {
    onInputKeyword(event) {
      // console.log(event.target.value)
      this.$emit('input-change',event.target.value)
    }
  },
}
</script>

<style>

</style>