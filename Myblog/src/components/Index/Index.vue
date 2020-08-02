<template>
    <div id="main">
      <div id="centercontent">
        <div id="show">
            <el-container>
                <!-- 轮播图 -->
                <el-main>
                <div class="block">
                    <el-carousel trigger="click" height="280px" :interval='5000'>
                      <el-carousel-item v-for="(item, index) in imgurl" :key="index"><img :src=item alt="">{{item}}
                      </el-carousel-item>
                    </el-carousel>
                  </div>
                </el-main>

                <!-- 展示内容 -->
                <el-aside width="200px">
                <div id="about">
                    <router-link to='/about'><p><b>关于博主</b></p></router-link>
                    <span>个人资料：男，90后，IT男，双子座，座右铭：多看电视多看报，少吃零食多睡觉。爱好：旅游</span>
                </div>
                <div id="attention">
                    <p><b>最新公告</b></p>
                    <span>1.不知妻美刘强东</span>
                    <br>
                    <span>2.普通家庭马化腾</span>
                    <br>
                    <span>3.悔创阿里杰克马</span>
                    <br>
                    <span>4.北大还行撒贝宁</span>
                </div>
            </el-aside>
              </el-container>
              </div>
              <div id="topnav">
                <b>最新文章</b>
                <span v-for="(count, column) in columncount">{{column}}({{count}})&nbsp;&nbsp;&nbsp;&nbsp;</span>
                <hr>
            </div>

        <articlelist :ColumnID='ColumnID'></articlelist>

      </div>

      <!-- 这是右侧 -->
      <div id="rightcontent">
        <!-- 关注我 -->
        <Notice></Notice>
        <!-- 最新文章 -->
        <newarticle></newarticle>
        <!-- 友情链接 -->
        <friendlylink></friendlylink>

      </div>
    </div>
</template>

<script>
  // 导入关注我模块
  import Notice from './Notice'

  export default{
    name:'index',
    components:{Notice},
    
    mounted() {
            this.$store.state.changeCSS(this.$route.path)
        },

    data:()=>{
      return {
        imgurl:[
        '../../../static/lunbo/lunbo1.jpg',
        '../../../static/lunbo/lunbo2.jpg',
        '../../../static/lunbo/lunbo3.jpg',
        '../../../static/lunbo/lunbo4.jpg',],
        ColumnID:1,
        columncount:''
        }
    },

    created(){
      this.$axios.get('articlecount/?columnid=3,4')
      .then(response=>{
        this.columncount = response.data
      })
      .catch(error=>{
        console.log(error)
      })
    }
  }
</script>

<style scoped>
  #main{
    width: 100%;
    margin: auto;
    overflow: hidden;
    text-align: center;
  }

  #centercontent{
    width: 690px;
    overflow: hidden;
    /* float: left; */
    display: inline-block;
  }

    #show{
        overflow: hidden;
        margin-top: 20px;
    }

    .el-container {
    width: 675px;
    height: 280px;
    float: left;
  }

  /* 这是轮播图样式 */
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    line-height: 160px;
    width: 500px;
    padding: 0px;
  }

  .el-carousel__item img{
      width: 100%;
      height: 100%;
  }

  /* 这是展示样式 */
  .el-aside {
    color: #333;
  }

  /* 关于博主 */
  #about{
      width: 135px;
      height: 97.4px;
      border: solid 1px yellow;
      padding: 20px;
      margin-left: 1px;
      text-align: center;
  }

  #about span{
    font-size: 10px;
    color: #AAAAAA;
    position: relative;
    top: 5px;
  }

  /* 最新公告 */
  #attention{
    width: 135px;
    height: 97px;
    border: solid 1px #99FFFF;
    margin-top: 2px;
    padding: 20px;
    margin-left: 1px;
    text-align: center;
  }

  #attention span{
    font-size: 10px;
    color: #AAAAAA;
    position: relative;
    top: 5px;
  }


  /* 右侧栏显示 */
  #rightcontent{
    width: 305px;
    margin-top: 30px;
    display: inline-block;
    vertical-align:top
  }


  #topnav{
    width: 675px;
    margin-top: 48px;
    text-align: left;
  }

  #topnav span{
    font-size: 10px;
    float: right;
    color: #666666;
  }

</style>