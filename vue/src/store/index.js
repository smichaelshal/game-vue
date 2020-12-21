import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const state = {
    myToken: '',
    namePage: '',
    username: '',
    rootDomain: 'https://djangovueattackapplice3.herokuapp.com',
};

const getters = {
    getMyToken(){
        return state.myToken
    },
    getNamePage(){
        return state.namePage
    },
    getUsername(){
        return state.username
    },
    getRootDomain(){
        return state.rootDomain
    },
};

const actions = {
};

const mutations = {
    setMyToken(state, token){
        state.myToken = token
    },
    setNamePage(state, namePage){
        state.namePage = namePage
    },

    setUsername(state, username){
        state.username = username
    },
};

const store = new Vuex.Store({
    state,
    getters,
    actions,
    mutations,
});

export default store;
