<template>
  <div id="ArticleList">
    <div class="articlelist" v-for='item in Articles' :key=item.id>
      <!-- 缩略图 -->
      <a href="javascript:0"><img :src="item.thumbnail" alt=""></a>
      <!-- 展现文章内容 -->
      <div class="showArticle">

        <router-link :to="{name:'detail', params:{id:item.id}}"><p><b>{{ item.title }}</b></p></router-link>
        <br>
        <span >{{ item.content | fontfilter() }}
          <router-link :to="{name:'detail', params:{id:item.id}}">[详情]</router-link>
        </span>

        <!-- 展现其他数据 -->
        <div class="detail">
          <i class="el-icon-paperclip"> {{ item.ownername }}&nbsp;&nbsp;</i>
          <i class="el-icon-alarm-clock">{{ item.time | timefilter('YYYY-MM-DD') }}</i>
        <span class="detailRight">
          <i class="el-icon-chat-round"> {{item.discuss_count}}&nbsp;&nbsp;</i>
          <i class="el-icon-view">{{ item.reads }}&nbsp;&nbsp;</i>
          <a href="javascript:0" @click='addAgree(item)'><i class="el-icon-thumb"> {{item.agree}}</i></a>
        </span>
        </div>
    </div>
  </div>

  <paginator :ColumnID='ColumnID' @getPaginator='getPaginator' ref='paginator_obj'></paginator>

    </div>
      
</template>

<script>
    export default{
        name:'articlelist',
        props:['ColumnID'],
        data:()=>{
          return {
            Articles:'',
          }
        },
        
        methods:{
          getPaginator(Articles){
            this.Articles = Articles
          },

          addAgree(item){
            let formData = new FormData()
            formData.append('token', localStorage.getItem('token'))
            this.$axios.post('articleagree/' + item.id, formData)
            .then(response=>{
              item.agree = response.data.articleAgree
              this.$message({
              message: '点赞成功：谢谢您',
              type: 'success'
            });
            })
            .catch(error=>{
              console.log(error.response.data)
              this.$message({
              dangerouslyUseHTMLString: true,
              message: '<b>点赞失败：</b>' + error.response.data.message,
              type: 'error'
            });
            })
          }
        },

    }
</script>

<style scoped>
  #ArticleList{
    width: 670px;
    text-align: left;
  }

  /* 文章列表 */
  .articlelist{
    height: 138px;
    padding-top: 30px;
    padding-bottom: 38px;
    border-bottom: solid 1px;
  }

  .articlelist img{
    width: 170px;
    height: 140px;
    float: left;
  }
  
  .showArticle{
    width: 465px;
    margin-left: 20px;
    float: left;
  }

  .showArticle span{
    font-size: 10px;
  }

  .detail{
    height: 20px;
    margin-top: 15px;
    font-size: 10px;
  }

  .detailRight{
    float: right;
  }


</style>