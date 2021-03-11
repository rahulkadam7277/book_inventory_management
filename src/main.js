import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import BootstrapVue from "bootstrap-vue";

import "../node_modules/bootstrap/dist/css/bootstrap.css";
import "../public/assets/plugins/materialdesignicons/css/materialdesignicons.min.css";
import "../public/assets/plugins/font-awesome-4.7.0/css/font-awesome.min.css";

import Toasted from 'vue-toasted';

Vue.use(Toasted)

Vue.config.productionTip = false;

Vue.use(BootstrapVue);

// Vue.filter('getImage', function (path) {
//   if (!path) return '../assets/default.svg'
//   return "http://image.tmdb.org/t/p/w500"+path
// })

Vue.mixin({
  methods: {
    getImageLink(path) {
      if (!path) return "../assets/default.svg";
      return "http://image.tmdb.org/t/p/w500" + path;
    }
  }
});
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
