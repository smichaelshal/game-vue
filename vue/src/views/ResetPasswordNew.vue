<template>
  <div class="resetPasswordNew">
        <el-input style="width: 300px; margin: 10px;" placeholder="Enter a password" v-model="password" type="password"></el-input>
       <el-button @click="sendLogin">Send</el-button>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';


export default {
  name: "ResetPasswordNew",
  components: {
  },
    computed: {
    ...mapGetters([
        'getRootDomain',
    ]),
  },
  data(){
      return {
          password: '',
          errors: '',
          responseData: '',
      }
  },
  methods:{
    alertSuccess(title, val){
      const h = this.$createElement;
      this.$notify({
          title: 'Success ' + title,
          message:  h('i', { style: 'color: black' }, val),
          position: 'bottom-right',
          type: "success",
          duration: 5000,
        });
    },

        alertError(val, titles){
      const h = this.$createElement;
      this.$notify({
          title: 'Error ' + titles,
          message:  h('i', { style: 'color: black' }, val),
          position: 'bottom-right',
          type: "error",
          duration: 5000,
        });
    },
        sendLogin(){
        let tempToken = this.$route.query.token
        axios.post(this.getRootDomain + '/api/password_reset/confirm/', {
            token: tempToken,
            password: this.password
    })

    .then(response => (this.responseData = response.data))
    .catch(error => console.log(this.errors = error))

    },
      mounted: function () {
      this.setNamePage('/reset-password-new')
  },
  },
    watch: {
    responseData: function(){
      this.errorMsg = ''
      this.alertSuccess('Password', 'Password changed successfully')
      this.$router.push({ path: '/login' })
    },
    errors: function(val){
      this.errorMsg = val.response.data.password
      this.alertError(val.response.data.password, 'Password')

    },
  },
};
</script>
