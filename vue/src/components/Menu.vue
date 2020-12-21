<template>
    <div class="menu">
        <b-navbar>
            <template slot="brand">
                <b-navbar-item tag="router-link" :to="{ path: '/' }">
                    <img
                        src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
                        alt="Lightweight UI components for Vue.js based on Bulma"
                    >
                </b-navbar-item>
            </template>
            <template slot="start">
                <b-navbar-item>
                    <router-link to="/">Home</router-link>
                </b-navbar-item>

                <b-navbar-dropdown :label="getUsername" v-if="getMyToken != ''">
                <b-navbar-item>
                    <router-link to="/change-password">Change Password</router-link>
                </b-navbar-item>

            </b-navbar-dropdown>
                
            </template>

            <template slot="end">
                <b-navbar-item tag="div">
                    <div class="buttons" v-if="getMyToken === ''">
                        <router-link to="/register" class="button" :class="{'is-primary': (getNamePage != '/login' && getMyToken === ''), 
                        'is-light': (getNamePage == '/login' && getMyToken === '')}">
                            <strong>Sign up</strong>
                        </router-link>
                        <router-link to="/login" class="button" :class="{'is-light': (getNamePage != '/login' && getMyToken === ''), 
                        'is-primary': (getNamePage == '/login' && getMyToken === '')}">
                            Log in
                        </router-link>
                    </div>
                    <div v-if="getMyToken != ''">
                         <a href="/" class="button is-primary" @click="logoutFun">
                            <strong>Log out</strong>
                        </a>
                    </div>
                </b-navbar-item>
            </template>
        </b-navbar>
        
    </div>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex';
import axios from 'axios';

export default {
    name: 'Menu',
    props: {
    },
    computed: {
        ...mapGetters([
            'getMyToken',
            'getNamePage',
            'getUsername',
            'getRootDomain'
        ]),
    },
    methods: {
        ...mapActions([
        ]),
        ...mapMutations([
            'setMyToken',
            'setUsername',
        ]),
        logoutFun(){
            this.sendLogout()
            this.setUsername('')
            this.setMyToken('')
        },
        sendLogout(){
            const url = this.getRootDomain + '/api/logout/'
            let config = {
                headers: {
                    Authorization: 'Token ' + this.getMyToken,
                    }
                }
                let data = {
                }

            axios.post(url, data, config)
            .then(response => (this.responseData = response.data))
            .catch(error => console.log(this.errors = error))
        },
    },

    data(){
        return {
            bla: true,
            isActive: true,
        }
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.d1{
    background: red;
}
</style>
