<template>
  <div class="home">
    <SearchBar msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchBar from '@/components/SearchBar.vue'

export default {
  name: 'Home',
  components: {
    SearchBar
  }
}
</script>

<style lang="scss">
.home{
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

</style>