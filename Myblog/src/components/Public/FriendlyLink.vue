<template>
    <div>
    <ul>友情链接
        <hr>
          <li><a href="">Kira博客</a></li>
      </ul>
    </div>
</template>

<script>
    export default{
        name:'friendlylink'
    }
</script>

<style scoped>
      /* 友情连接 */
    div{
      margin-top: 20px;
      text-align: left;
    }

    ul{
    font-size: 18px;
    }

    hr{
    border: solid 0.5px #DDDDDD;
    margin-top: 15px;
    margin-bottom: 15px;
  }

  li{
    height: 48px;
    border: solid 1px #AAAAAA;
    font-size: 10px;
    padding: 18px;
  }
</style>