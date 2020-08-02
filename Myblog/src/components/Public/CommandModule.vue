<template>
    <div id="main">
        <div id="content">
            <slot></slot>
          </div>

          <div id="rightshow">
            <table>
                <tr>
                    <router-link to="/about"><td id="td1">关于博主</td></router-link>
                    <router-link to="/mood"><td id="td2">心情随笔</td></router-link>
                    <router-link to="/recall"><td id="td3">回忆往事</td></router-link>
                </tr>
                <tr>
                    <router-link to="/"><td id="td4">网站首页</td></router-link>
                    <router-link to="/about"><td id="td5">Blog留言</td></router-link>
                    <router-link to="/technology"><td id="td6">技术分享</td></router-link>
                </tr>
            </table>

            <newarticle></newarticle>

            <friendlylink></friendlylink>
          </div>
    </div>
</template>

<script>
    export default{
        name:'commandmodule'
    }
</script>

<style scoped>
    #main{
        width: 100%;
        margin: auto;
        overflow: hidden;
        text-align: center;
    }

  #content{
    width: 675px;
    height: auto;
    text-align: left;
    overflow: hidden;
    display: inline-block;
    vertical-align:top
  }


  .mymood{
    width: 557px;
    height: 70px;
    border-radius: 5px;
    border: solid 1px	#DDDDDD;
    padding-top: 25px;
    padding-left: 20px;
    padding-right: 95px;
    margin-bottom: 10px;
    font-size: 13px;
    color: 	#888888;
    background-color: #F5FFFA;
  }

  #rightshow{
      width: 300px;
      margin-top: 40px;
      margin-left: 25px;
      text-align: left;
      display: inline-block;
      vertical-align:top
  }

  table{
    width: 282px;
  }

  td{
    width: 76px;
    height: 50px;
    padding-left: 10px;
    padding-top: 28px;
  }

  #td1{
      border: solid 1px #8A2BE2;
      background-color: #E6E6FA ;
  }

  #td2{
      border: solid 1px #FF69B4;
      background-color: #FFEFD5 ;
  }

  #td3{
      border: solid 1px #DDA0DD;
      background-color: #F5F5DC ;
  }

  #td4{
      border: solid 1px #00FF7F;
      background-color: #E0FFFF ;
  }

  #td5{
      border: solid 1px #8B008B;
      background-color: #DDA0DD ;
  }

  #td6{
      border: solid 1px #66CDAA;
      background-color: #E6E6FA ;
  }
</style>