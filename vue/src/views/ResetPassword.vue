<template>
  <div class="resetPassword">
    <el-input style="width: 300px; margin: 10px;" placeholder="Enter a email" v-model="email" type="text" :disabled="isSend"></el-input>
    <el-button :disabled="isSend" @click="sendRequestRestPassword">Send</el-button>

    <div style="margin: 20px;" v-if="isSend">
        <el-button style="padding: 3px 10px" type="text" @click="sendRequestRestPassword">The email did not arrive, send again.</el-button>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: "ResetPassword",
  components: {
  },
  computed: {
    ...mapGetters([
        'getRootDomain',
    ]),
  },
  data(){
    return{
      email: '',
      responseData: '',
      errors: '',
      isSend: false
    }
  },

  methods: {
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

    alertSuccess(val, title){
      const h = this.$createElement;
      this.$notify({
          title: 'Success ' + title,
          message:  h('i', { style: 'color: black' }, val),
          position: 'bottom-right',
          type: "success",
          duration: 5000,
        });
    },
    sendRequestRestPassword(){
      axios.post(this.getRootDomain + '/api/password_reset/', {
      email: this.email,
    })

    .then(response => (this.responseData = response.data))
    .catch(error => console.log(this.errors = error))

    },
    
  },
  mounted: function () {
      this.setNamePage('/reset-password')
  },

    watch: {
    responseData: function(){
      this.isSend = true
      this.alertSuccess('Email', 'The email was sent successfully.')
      this.errorMsg = ''
    },
    errors: function(val){
      this.errorMsg = val.response.data.email
      this.alertError(val.response.data.email, 'Email')

    },
  },
};
</script>
