<template>
  <!--img alt="Vue logo" src="./assets/logo.png"-->
  <!--HelloWorld msg="Welcome to Your Vue.js App"/-->
  <!--Testing the use of components with VUE -->
  <test/>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import test from './components/test.vue'

export default {
  name: 'App',
  components: {
    //HelloWorld,
    test
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
#Input1{
  margin-right: .5in;
  margin-left: .5in;
}
#Input2{
  margin-right: .25in;
}
#movie{
  padding-bottom: 15px;
  padding-top: 30px;
}
</style>
