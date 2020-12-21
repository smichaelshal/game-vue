<template>
  <div class="changePassword">
      <div>
      <el-input style="width: 300px; margin: 10px;" placeholder="Enter old password" v-model="oldPassword" type="password"></el-input>
      </div>
      <div>
    <el-input style="width: 300px; margin: 10px;" placeholder="Enter new password" v-model="newPassword" type="password"></el-input>
    </div>
    
       <el-button @click="sendChangePassword">Send</el-button>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';


export default {
  name: "ChangePassword",
  components: {
  },
      computed: {
    ...mapGetters([
        'getMyToken',
        'getNamePage',
        'getUsername',
        'getRootDomain',
    ]),
  },
  data(){
      return {
          oldPassword: '',
          newPassword: '',
          responseData: '',
      }
  },
  methods:{
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
    sendChangePassword(){
    const url = 'http://localhost:8000/api/change-password/'
    let config = {
        headers: {
            Authorization: 'Token ' + this.getMyToken,
            }
        }
        let data = {
          old_password: this.oldPassword,
          new_password: this.newPassword
        }

    axios.put(url, data, config)
    .then(response => (this.responseData = response.data))
    .catch(error => console.log(this.errors = error))
    },
  },
    mounted: function () {
      this.setNamePage('/change-password')
  },

  watch: {
    responseData: function(){
    }
  }
};
</script>
