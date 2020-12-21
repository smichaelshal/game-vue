<template>
  <div class="footer">
      <el-footer>Footer</el-footer>
  </div>
  
</template>

<script>

export default {
  name: 'Footer',
  props: {
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

.footer{
   position: fixed;
   left: 0;
   bottom: 0;
   width: 100%;
   text-align: center;
   height: 0px;
}
</style>
