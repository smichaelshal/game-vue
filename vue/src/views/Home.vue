<template>
  <div class="home">
    <!-- Home -->
    <Table v-if="getMyToken != ''"/>
    <div v-else style="margin-top: 100px;">
      <h1 class="title is-2">You have not registered yet</h1>
      <h1 class="subtitle is-2">Sign up today</h1>
    <!-- <div class="buttons"> -->
      <b-button type="is-primary">
        <router-link to="/login">
        <h1 class="title is-5" style="color: white;">
          <strong>Sign up</strong>
          </h1>
        </router-link>
      </b-button>
      <!-- </div> -->

    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters, mapActions, mapMutations } from 'vuex';
import Table from '@/components/Table.vue'


export default {
  name: 'Home',
  components: {
    Table,
  },
  computed: {
        ...mapGetters([
            'getMyToken',
            'getNamePage',
            'getUsername',
        ]),
    },

    methods: {
        ...mapActions([
        ]),
        ...mapMutations([
            'setMyToken',
            'setNamePage',
            'setUsername',
        ]),
    },
      mounted: function () {
      this.setNamePage('/')
  },
}
</script>
