<template>
  <div id="app">

  <!-- 顶部 -->
  <div id="topbg">
      <ul>
        <a href="javascript:0">Home</a>
        <a href="javascript:0">关于我们</a>
      </ul>
  </div>

  <!-- 背景图 -->
  <div id="mainimg"></div>

  <!-- 导航栏 -->
  <div id="Navbar">
  <el-menu
    class="el-menu-demo"
    mode="horizontal"
    background-color="#919191"
    text-color="#fff"
    active-text-color="#ffd04b"
    
    router>
    <el-menu-item v-for="item in columns" :index="item.path" :path="item.path">{{ item.name }}</el-menu-item>

    <el-input
    placeholder="搜索..."
    prefix-icon="el-icon-search"
    v-model="input21">
  </el-input>
  </el-menu>
</div>

  <router-view />
  <!-- 底部 -->
  <div id="foot">
    <span>粤ICP备1314520号</span>
  </div>

</div>
</template>

<script>
export default {
  name: 'App',

  data:()=>{
    return {
      input21:'',
      columns:'',
      }
  },

  created(){
    this.$axios.get('columns')
    .then(response=>{
      this.columns = response.data
    })
    .catch(error=>{
      console.log(error)
    })
},
}
</script>

<style>
  *{
    margin:0px;
    padding: 0px;
  }

  body{
    background-color:floralwhite;
  }

  a{
    text-decoration: none;
    color: #444444;
  }

  li{
    list-style-type: none;
  }

  #topbg ul{
    background-color:#EEEEEE;
    text-align: right;
    height: 30px;
    font-size: 10px;
    padding-right: 164px;
    border: solid 1px ;color:#CCCCCC; 
  }

  #topbg ul a{
    margin-right: 20px;
    position: relative;
    top: 6px
  }

  /* 背景图 */
  #mainimg{
    width: 100%;
    height: 170px;
    margin-top: 3px;
    background-image: url('../static/backgroundimg.png');
    background-size: cover;
  }

  /* 导航栏 */
  #Navbar{
    margin: auto;
    width: 100%;
    height: 50px;
    text-align: center;
    background-color: rgb(145, 145, 145);
  }

  #Navbar ul{
    height: 50px;
    display: inline-block;
  }

  #Navbar ul li{
    text-align: center;
    font-size: 18px;
    height: 50px;
    display: inline-block;
  }

  /* 搜索框 */
  .el-input{
    width:100px;
    position: relative;
    top:5px;
    left: 30px;
  }

  /* 尾部 */
  #foot{
    text-align: center;
    font-size: 10px;
    color: #666666;
    margin-top: 20px;
    margin-bottom: 10px;
  }

  /* 轮播 */
  .el-carousel__indicator{
      position: relative;
      top: 70px
  }
  

  .el-pagination.is-background .btn-next, .el-pagination.is-background .btn-prev, .el-pagination.is-background .el-pager li{
    border: red;
    background-color: rgb(247, 243, 235);
  }

  .el-form-item__label{
        text-align: left;
    }

    /* 上传图片框 */
    .el-upload-dragger{
    width: 210px;
    height: 150px;
    }

    .el-upload-dragger i{
      width: 50px;
      height: 50px;
    }
</style>
