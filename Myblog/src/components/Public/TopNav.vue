<template>
    <div id="topnav">
        <b>{{topnavTitle}}</b>
        <span><a href="javascript:0" @click='back'>返回</a>&gt;&gt;</span>
        <hr>
    </div>
</template>

<script>
    export default{
        name:'topnav',
        inject:["path"],
        data:()=>{
          return {topnavTitle:''}
        },

        created(){
          this.$axios.get('singlecolumn/?path=' + this.path)
          .then(response=>{
            this.topnavTitle = response.data.name
          })
          .catch(error=>{
            console.log(error)
          })
        },

        methods:{
          back(){
            this.$router.go(-1)
          },
        },
    }
</script>

<style scoped>
  #topnav{
    width: 675px;
    margin-top: 48px;
  }

  #topnav span{
    font-size: 10px;
    float: right;
    color: #666666;
    position: relative;
    top: 5px;
  }

  #topnav hr{
    height: 5px;
    background-color: darkslategrey;
    margin-top: 8px;
  }
</style>