<template>
    <div>
        <ul>关注我
            <hr>
            <a href="https://weibo.com/u/2718604160" target="_blank"  rel="nofollow">
              <li><img src="../../../static/sina.png" alt=""><p>新浪微博</p></li></a>

            <a href="http://t.qq.com/liuy" target="_blank"  rel="nofollow">
              <li><img src="../../../static/tencent.png" alt=""><p>腾讯微博</p></li></a>

              <a href="/" target="_blank"  rel="nofollow">
                <li><img src="../../../static/email.png" alt=""><p>邮箱</p></li></a>

            <router-link to='/'><li><img src="../../../static/feeback.png" alt=""><p>意见反馈</p></li></router-link>
          </ul>
    </div>
</template>
<script>
    export default{
        name:'notice',
    }
</script>
<style scoped>
  ul{
    font-size: 18px;
    text-align: left;
  }

  ul li{
    width: 57px;
    height: 58;
    line-height: 10px;
    text-align: center;
    float: left;
    margin-top: 10px;
    margin-right: 18px;
    margin-bottom: 40px;
  }

  ul li p{
    font-size: 10px;
    color: #666666;
  }

  hr{
    border: solid 0.5px #DDDDDD;
    margin-top: 10px;
    margin-bottom: 10px;
  }
</style>
