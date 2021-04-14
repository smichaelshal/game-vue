import Vue from 'vue'
import App from './App.vue'

import store from './store'

import router from './router'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

Vue.use(Buefy)

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')

// npm install vuex --save
// npm install es6-promise --save

// npm install axios

// npm install buefy
// npm i element-ui -S


