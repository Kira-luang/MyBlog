<template>
    <div>
          <commandmodule>
                <topnav></topnav>
                <div v-infinite-scroll="loadMore" infinite-scroll-disabled="busy" infinite-scroll-distance="10" infinite-scroll-immediate-check="auto">
                    <ul>
                        <li class="mymood" v-for='item in article_list'>
                            <p><i class="el-icon-date">{{item.time | timefilter('YYYY-MM-DD')}}</i></p>
                            <span>{{item.content}}</span>
                        </li>
                    </ul>
                </div>

          </commandmodule>
    </div>
</template>

<script>
    export default{
        name:'mood',
        provide:{path:'/mood'},
        mounted() {
            this.$store.state.changeCSS(this.$route.path)
        },
        data:()=>{
            return {columnID:2,
            article_list:'',
            busy:false,
            page:1}
        },
        created(){
            this.$axios.get('http://127.0.0.1:8000/api/column/' + this.columnID)
            .then(response=>{
                this.article_list = response.data.Article
            })
            .catch(error=>{
                console.log(error)
            })
        },

        methods:{
            loadMore:function(){
                ++this.page
                console.log(this.page)
                this.$axios.get('column/' + this.columnID + '?page=' + this.page)
                .then(response=>{
                    this.article_list = this.article_list.concat(response.data.Article)
                    if (response.data.Article.length < 10) {
                        this.busy = true
                    }
                })
                .catch(error=>{
                    console.log(error)
	   })
	}
        }
    }
</script>

<style scoped>
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
</style>