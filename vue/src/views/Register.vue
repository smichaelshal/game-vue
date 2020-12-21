<template>
  <div class="register">
    <h1>Register</h1>
    <div class="div-form">
      <el-input style="width: 300px; margin: 10px;" placeholder="Enter a username" v-model="inputUsername" type="text"></el-input>
    </div>

    <div class="div-form">
      <el-input style="width: 300px; margin: 10px;" placeholder="Enter a email" v-model="inputEmail" type="email"></el-input>
    </div>

    <div class="div-form">
      <el-input style="width: 300px; margin: 10px;" placeholder="Enter a password" v-model="inputPassword" type="password"></el-input>
    </div>

    <div class="div-form">
      <el-input style="width: 300px; margin: 10px;" placeholder="Enter again password" v-model="inputPassword2" type="password"></el-input>
    </div>

    <div class="div-form">
      <el-button @click="sendRegister">Send</el-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters, mapActions, mapMutations } from 'vuex';

export default {
  name: "Register",
  components: {
  },
  data(){
    return {
      inputUsername: '',
      inputEmail: '',
      inputPassword: '',
      inputPassword2: '',
      responseData: '',
      errors: '',
      errorMsg: ''

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
    sendRegister(){
      if(this.inputUsername === ''){
        this.alertError('Enter a valid username.')
      } else if(this.inputEmail === ''){
        this.alertError('Enter a valid email address.')
      }else if(this.inputPassword === ''){
        this.alertError('Enter a valid password.')
      }
      else if(this.inputPassword2 === ''){
        this.alertError('Enter a valid password again.')
      }
       else{
        axios.post(this.getRootDomain + '/api/register/', {
        username: this.inputUsername,
        email: this.inputEmail,
        password: this.inputPassword,
        password2: this.inputPassword2,
      })

      .then(response => (this.responseData = response.data))
      .catch(error => console.log(this.errors = error))
      }

    },
      ...mapActions([
      ]),
      ...mapMutations([
          'setMyToken',
          'setNamePage',
          'setUsername',
          'getRootDomain',
      ]),
  },
  mounted: function () {
      this.setNamePage('/register')
  },

    watch: {
    responseData: function(val){
      this.$router.push({ path: '/login' })
      this.errorMsg = val
    },
    errors: function(val){
      const username =  val.response.data.username
      const password =  val.response.data.password
      const email =  val.response.data.email
      const msg =  val.response.data.msg
      
      let varToSend = ''

      if(username != undefined){
        varToSend = username
      }else if(password != undefined){
        varToSend = password
      }else if(msg != undefined){
        varToSend = msg
      }else if(email != undefined){
        varToSend = email
      }
      
      console.log(val.response.data)

      this.errorMsg = varToSend
      this.alertError(varToSend)
    },
  },

};
</script>

<style scoped>
.div-form{
  margin-bottom: 10px;
}
</style>
