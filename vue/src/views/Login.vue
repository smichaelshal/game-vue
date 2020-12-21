<template>
  <div class="login">
    <h1>Login</h1>
    <div class="div-form">
      <el-input style="width: 300px; margin: 10px;" placeholder="Enter a username" v-model="inputUsername" type="email"></el-input>
    </div>

    <div class="div-form">
      <el-input style="width: 300px; margin: 10px;" placeholder="Enter a password" v-model="inputPassword" type="password"></el-input>
    </div>

    <div class="div-form">
      <el-button @click="sendLogin">Send</el-button>

      <!-- <el-button type="warning" plain>I forgot the password</el-button> -->
      <div style="margin: 20px;">
        <el-button style="padding: 3px 10px" type="text"><router-link to="/reset-password">I forgot the password</router-link></el-button>
      </div>
    </div>

    <!-- <div style="width: 300px; margin: auto;" v-if="errorMsg != ''">
      <el-alert
    :title="errorMsg"
    type="error"
    show-icon
    @close="fun1"
    >
  </el-alert>

    </div> -->

    <!-- <Table /> -->
  </div>
</template>

<script>
// import Table from '@/components/Table.vue'
import { mapGetters, mapActions, mapMutations } from 'vuex';
import axios from 'axios';

export default {
  name: "Login",
  components: {
    // Table,
  },
  data(){
    return {
      inputUsername: '',
      inputPassword: '',
      responseData: '',
      errors: '',
      errorMsg: '',
    }
  },

  computed: {
    ...mapGetters([
        'getMyToken',
        'getNamePage',
        'getUsername',
        'getRootDomain',
    ]),
  },
  methods: {
    alertError(val){
      const h = this.$createElement;
      this.$notify({
          title: 'Error',
          message:  h('i', { style: 'color: black' }, val),
          position: 'bottom-right',
          type: "error",
          duration: 5000,
        });
    },
    sendLogin(){
      axios.post(this.getRootDomain + '/api/login', {
      username: this.inputUsername,
      password: this.inputPassword,
    })

    .then(response => (this.responseData = response.data))
    .catch(error => console.log(this.errors = error))

    },
      ...mapActions([
      ]),
      ...mapMutations([
          'setMyToken',
          'setNamePage',
          'setUsername',
      ]),
  },
  mounted: function () {
      this.setNamePage('/login')
  },
  watch: {
    responseData: function(val){
      this.setMyToken(val.token)
      this.setUsername(this.inputUsername)
      this.$router.push({ path: '/' })
      this.errorMsg = ''
    },
    errors: function(val){
      this.errorMsg = val.response.data.msg
      this.alertError(val.response.data.msg)
    },
  },
  
};
</script>

<style scoped>
.div-form{
  margin-bottom: 10px;
}
</style>
