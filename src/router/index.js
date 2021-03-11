

import Vue from "vue";
import VueRouter from "vue-router";


Vue.use(VueRouter);
function loadView (view) {
  return () =>
    import(/* webpackChunkName: "view-[request]" */ `@/views/${view}.vue`)
}

const routes = [
  {
    path: "/",
    name: "Home",
    component: loadView('Home')
  }, 
  {
    path: "/addBook",
    name: "addBook",
    component: loadView('AddBook')
  },
  {
    path: "/updateBook/:bookId",
    name: "updateBook",
    props:true,
    component: loadView('AddBook')
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
