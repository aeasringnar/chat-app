<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  margin-top: 0px;
}
html,body{
  height: 100%;
  width: 100%;
}
#app{
  width: 100%;
  height: 100%;
  overflow: hidden;
  overflow-y: scroll;
  background-color: #FFFFFF;
  margin:0;
  padding: 0;
}
#app::-webkit-scrollbar {
    display: none;
}
</style>
