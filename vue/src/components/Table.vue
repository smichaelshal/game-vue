<template>
<div class="table">
    <el-row>
        <el-col :span="6" class="divClear">a</el-col>
        <el-col :span="12">
            <el-table
                :data="tableData"
                style="width: 100%">
                <el-table-column
                label="Username"
                >
                <template slot-scope="scope">
                    <p>{{ scope.row.username }}</p>
                </template>
                </el-table-column>
                <el-table-column
                label="Points"
                >
                <template slot-scope="scope">
                    <p>{{ scope.row.points }}</p>
                </template>
                </el-table-column>
                <el-table-column
                label="To Attack">
                <template slot-scope="scope">
                    <el-button
                    size="mini"
                    type="danger"
                    @click="ToAttack(scope.$index, scope.row)">Attack</el-button>
                </template>
                </el-table-column>
            </el-table>
            </el-col>
            <el-col :span="6" class="divClear">a</el-col>
  </el-row>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapMutations} from 'vuex';
import axios from 'axios';

export default {
    name: 'Table',
    

    data() {
      return {
        responseData: '',
        responseDataAttack: '',
        errors: '',
        intervalid1:'',

        tableData: [],
        tableData2: [
        {
          username: 'admin',
          points: 10,
        },
        {
          username: 'michael',
          points: 9,
        },
        {
          username: 'ran',
          points: 8,
        },
        ]
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
    ...mapMutations([
      ]),
    ToAttack(index, row) {
    // console.log(row.username);
    const url = this.getRootDomain + '/api/life/'
    let config = {
        headers: {
            Authorization: 'Token ' + this.getMyToken,
            }
        }
        let data = {
          toattack: row.username
        }

    axios.post(url, data, config)
    .then(response => (this.responseDataAttack = response.data))
    .catch(error => console.log(this.errors = error))
    },
    setList(val){
      this.tempTableData = []
      this.tableData = []
      
      for (const [key, value] of Object.entries(val)) {
        const tempObj = {
          username: key, 
          points: value
        }
      
      this.tempTableData.push(tempObj)

      
      }

      this.tableData = this.tempTableData.sort(function(obj1, obj2){return obj2.points - obj1.points});


    },
    sendRequestListLifes(){
        // const url = 'http://localhost:8000/api/life/'
        //     let config = {
        //         headers: {
        //             Authorization: 'Token ' + this.getMyToken,
        //             }
        //         }
        //         let data = {
        //         }

            // axios.get(url, data, config)
            axios.get(this.getRootDomain + '/api/life/', {
              headers: {
                Authorization: 'Token ' + this.getMyToken,
              }
            })
            .then(response => (this.responseData = response.data))
            .catch(error => console.log(this.errors = error))
    },
      ...mapActions([
      ]),
    todoLoop: function(){           
        this.intervalid1 = setInterval(function(){
          this.sendRequestListLifes()
        }.bind(this), 1000);
      }

  },
  mounted: function () {
    //   this.setNamePage('/login')
    this.sendRequestListLifes()
    this.todoLoop()
  },

    watch: {
    responseData: function(val){
      // console.log(val.admin)
      this.setList(val)
    },
    // tableData: function(val){
      
    // }
  }

  }
</script>

<style scoped>
.divClear{
    color: white;
}
</style>