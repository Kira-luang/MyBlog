<template>
    <div>
      <ul>最新文章
        <hr>
        <li v-for="article in Articles"><a href="">{{article.title}}</a></li>
      </ul>
    </div>
</template>

<script>
    export default{
        name:'newarticle',
        data:()=>{
          return {Articles:''}
        },
        created(){
          this.$axios.get('column/1')
          .then(response=>{
            this.Articles = response.data.Article.slice(0, 6)
            }
          )
          .catch(error=>{
        console.log(error)
      })
        }
    }
</script>

<style scoped>
      /* 友情连接 */
    div{
      padding-top: 25px;
      text-align: left;
    }

    ul{
    font-size: 18px;
    }

    hr{
    border: solid 0.5px #DDDDDD;
    margin-top: 10px;
    margin-bottom: 10px;
  }

    li{
    list-style-type: square;
    font-size: 10px;
    line-height: 25px;
    position: relative;
    left: 17px;
  }
</style>