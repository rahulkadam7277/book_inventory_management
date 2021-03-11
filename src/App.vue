
<template>
  <div id="app">
    <div id="loader-wrapper" v-if="isPageLoaderEnabled">
      <div id="loader" />
    </div>
    <div class="wrapper">
    <div id="nav">
     <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
    </div>
    <router-view />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  computed:{
    ...mapGetters(['isPageLoaderEnabled'])
  }
  
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; 
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}


// Loader

.vh-100 {
  height: 100vh;
}
#loader-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
  background: #fbf8f89c;
}
#loader {
  display: block;
  position: relative;
  left: 50%;
  top: 50%;
  width: 150px;
  height: 150px;
  margin: -75px 0 0 -75px;
  border-radius: 50%;
  border: 3px solid transparent;
  border-top-color: #3498db;

  animation: spin 2s linear infinite; /* Chrome, Firefox 16+, IE 10+, Opera */

  z-index: 1001;
}

#loader:before {
  content: '';
  position: absolute;
  top: 5px;
  left: 5px;
  right: 5px;
  bottom: 5px;
  border-radius: 50%;
  border: 3px solid transparent;
  border-top-color: #e74c3c;

  animation: spin 3s linear infinite; /* Chrome, Firefox 16+, IE 10+, Opera */
}

#loader:after {
  content: '';
  position: absolute;
  top: 15px;
  left: 15px;
  right: 15px;
  bottom: 15px;
  border-radius: 50%;
  border: 3px solid transparent;
  border-top-color: #f9c922;

  animation: spin 1.5s linear infinite; /* Chrome, Firefox 16+, IE 10+, Opera */
}

@-webkit-keyframes spin {
  0% {
    transform: rotate(0deg); /* Firefox 16+, IE 10+, Opera */
  }
  100% {
    transform: rotate(360deg); /* Firefox 16+, IE 10+, Opera */
  }
}
@keyframes spin {
  0% {
    transform: rotate(0deg); /* Firefox 16+, IE 10+, Opera */
  }
  100% {
    transform: rotate(360deg); /* Firefox 16+, IE 10+, Opera */
  }
}

.loaded #loader {
  opacity: 0;

  transition: all 0.3s ease-out;
}
.loaded #loader-wrapper {
  visibility: hidden;

  transform: translateY(-100%); /* Firefox 16+, IE 10+, Opera */

  transition: all 0.3s 1s ease-out;
}

/* JavaScript Turned Off */
.no-js #loader-wrapper {
  display: none;
}
.no-js h1 {
  color: #222222;
}

body {
  background-color: #f7f8fc !important;
}
#app-loader { 
  position: fixed;
  z-index: 999;
  height: 2em;
  width: 2em;
  overflow: show;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

/* Transparent Overlay */
#app-loader:before {
  content: '';
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.8); 
}

.user-pic {
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.table-card {
  border: none !important;

  -webkit-box-shadow: 0 0.75rem 1.5rem rgba(18, 38, 63, 0.03);
  box-shadow: 0 0.75rem 1.5rem rgba(18, 38, 63, 0.03);
}
.table.b-table > tfoot > tr > th:before,
.table.b-table > thead > tr > th:before {
  display: inline-block;
  float: right;
  margin-left: 0.5em;
  width: 0.5em;
  font-size: inherit;
  line-height: inherit;
  opacity: 0.4;
  content: '↕';
}
.table.b-table > thead > tr > th:focus {
  outline: transparent;
}
.icon {
  font-size: 25px !important;
  cursor: pointer;
}

</style>
