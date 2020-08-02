<template>
    <div>
    <commandmodule>
        <!-- 插入正文 -->
        <div id="center">
            <!-- 面包屑 -->
            <breakcrumb :columnID="columnID"></breakcrumb>
            <div id="Article">
                <p id="title">{{article.title}}</p>
                <p id="author"><i class="el-icon-s-custom">&nbsp;{{article.Author}}&nbsp;&nbsp;&nbsp;</i>
                    <i class="el-icon-date">&nbsp;{{article.time | timefilter('YYYY-MM-DD h:mm:ss')}}</i></p>
                    <div v-html='article.content'></div>

                    <!-- 底部声明 -->
                    <announce></announce>
            </div>

            <!-- 展现上一篇和下一篇文章 -->
            <div id="nextlast">
                <p v-show=last><b>上一篇:&nbsp;</b>
                    <router-link :to="{name:'detail', params:{id:last.id}}">{{last.title}}</router-link></p>
                <p v-show=next><b>下一篇:&nbsp;</b>
                    <router-link :to="{name:'detail', params:{id:next.id}}">{{next.title}}</router-link></p>
            </div>

            <!-- 输入框 -->
            <inputtext v-show='is_login' :path="detail_id"></inputtext>

            <!-- 非登陆状态遮盖框 -->
            <needlogin v-show='!is_login'></needlogin>

            <discuss :path="detail_id"></discuss>
        </div>

    </commandmodule>
</div>
</template>

<script>
    export default{
        name:'detail',
        data:()=>{
            return {
                article:"",
                last:'',
                next:'',
                columnID:'',
                link:'',
                is_login:false,
                detail_id:'',
                }
        },
        watch:{
            $route(to, from){
                this.getArticle(to.params.id)
            }
        },
        created(){
            this.getArticle(this.$route.params.id)
            this.detail_id = this.$route.params.id
            this.$store.state.changeCSS('/')
            this.judge_token()
        },

        methods:{
            getArticle(id){
            let req1 = this.$axios.get('detail/' + id)
            let req2 = this.$axios.get('lastnext/' + id)
            this.$axios.all([req1, req2])
            .then(this.$axios.spread((article, lastnext)=>{
                this.article = article.data.Article[0]
                this.columnID = this.article.column
                switch (lastnext.data.length){
                    case 2:
                        if (lastnext.data[0].id < id){
                            this.last = lastnext.data[0]
                            this.next = lastnext.data[1]
                        }else{
                            this.last = lastnext.data[0]
                            this.next = lastnext.data[1]}
                        break
                    case 1:
                        this.last = lastnext.data[0]
                        if (lastnext.data[0].id > id){
                            this.next = lastnext.data[0]
                            this.last = ''
                        }
                        break
                    case 0:
                        this.next = ''
                        this.last = ''
                }

            }))
            .catch(error=>{
                console.log(error)
            })
            },

            judge_token(){
                let token = localStorage.getItem('token')
                this.$axios.get('/confirm/?token='+token)
                .then(response=>{
                    this.is_login = true
                })
                .catch(error=>{
                    localStorage.clear()
                    this.is_login = false
                })
            },
        }
    }
</script>

<style scoped>
    #center{
        width: 675px;
        float: left;
    }

    #Article{
        line-height: 38px;
        margin-top: 28px;
    }

    #title{
        font-size: 28px;
    }

    #author{
        font-size: 12px;
        color: grey;
    }

    .para{
    font-size: 14px;
    word-wrap: break-word;
    color: #333;
    margin-bottom: 15px;
    text-indent: 2em;
    line-height: 24px;
    zoom: 1;
}

    #nextlast{
        font-size: 10px;
        line-height: 23px;
        margin-top: 5px;
    }
</style>