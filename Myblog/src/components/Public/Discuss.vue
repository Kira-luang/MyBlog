<template>
    <div>
    <!-- 评论留言区 -->
    <div id="discuss">
        <p><span><b>评论</b></span>
            <span id="rightdiscuss"><b>{{usercount}}</b>人参与评论,<b>{{messagecount}}</b>条评论</span></p>
            <hr>
        <p id="hot"><i class="el-icon-edit"></i>热门评论</p>

        <div class='discusscontent' v-for="item in message_list">
            <!-- 头像 -->
            <div class="avatar">
                <el-row class="demo-avatar demo-basic">
                    <el-col :span="12">
                        <div class="sub-title"></div>
                        <div class="demo-basic--circle">
                        <div class="block"><el-avatar :size="50" :src="item.user_headimg"></el-avatar></div>
                        <div class="block" v-for="size in sizeList" :key="message_user.message.id">
                            <el-avatar :size="size" :src="item.user_headimg"></el-avatar>
                        </div>
                        </div>
                    </el-col>  
                </el-row>
            </div>
            
            <!-- 评论内容 -->
            <div class="content">
                <p class="nameTime"> {{item.username}} <span>{{item.time | timefilter("YYYY-MM-DD h:mm:ss")}}</span></p>
                <p class="detail">{{item.content}}</p>
            </div>

            <!-- 赞或者踩 -->
            <p class="agree">
                <a href="javascript:0" @click="addAgree(item)"><i class="el-icon-circle-plus-outline">&nbsp;{{item.agree}}&nbsp;&nbsp;&nbsp;</i></a>
                <a href="javascript:0" @click="addDisagree(item)"><i class="el-icon-remove">&nbsp;{{item.disagree}}</i></a>
            </p>
        </div>
    </div>
    
    <!-- 加载更多 -->
    <a href="javascript:0"><p id="seeMore" @click="GetMore" ref="loadMore">{{loading_message}}
        <i class="el-icon-bottom" v-show="show_icon"></i></p></a>
    </div>
</template>

<script>
    export default{
        props:["path"],
        name:'discuss',
        methods:{
            // 获取留言数据
            GetData(page){
                this.$axios.get(this.url + '/?page=' + page)
                .then(response => {    // response这个参数有坑
                this.message_list = this.message_list.concat(response.data)
                if (response.data.length < 10){
                    this.loading_message = "已经到底部了"
                    this.show_icon = false
                    this.Button = false
                }
            })
            .catch(error=>{
                console.log(error)
            })
            },

            // 获取统计
            GetCount(path){
                this.$axios.get(path)
                .then(response=>{
                    this.usercount = response.data.usercount
                    this.messagecount = response.data.messagecount
                })
                .catch(error=>{
                    console.log(error)
            })
            },

            // 加载更多
            GetMore(){
                ++this.page
                if (this.Button){
                    this.GetData(this.page)
                }
            },

            // 实现点赞和不点赞功能
            AgreeDisagree(item, action){
                let formData = new FormData()
                formData.append('token', localStorage.getItem('token'))
                formData.append('message', item.id)
                formData.append('action', action)
                this.$axios.post('messageagree/' + item.id, formData)
                .then(response=>{
                    item.agree = response.data.agree
                    item.disagree = response.data.disagree
                    console.log(response.data.agree, response.data.disagree)
                })
                .catch(error=>{
                    this.$message.error(error.response.data);
                    console.log(error.response.data)
                })
            },

            // 实现点赞功能
            addAgree(item){
                this.AgreeDisagree(item)
            },

            // 实现不赞同功能
            addDisagree(item){
                this.AgreeDisagree(item, 'disagree')
            }
        },

        data:()=>{
            return {
            sizeList:[],
            message_list:[],
            usercount:'',
            messagecount:'',
            page: 1,
            loading_message:'查看更多',
            show_icon:true,
            Button:true,
            url:''
            }
        },

        created(){
            console.log(this.path)
            if (this.path == '/message'){
                this.url = '/message'
                this.GetData(this.page)
                this.GetCount('usermessage/')
            }else{
                let path = 'userarticlemsg/' + this.path
                this.GetCount(path)
                this.url = 'articlemessage/' + this.path
                this.GetData(this.page)
            }
        },
        mounted(){
            this.$event.$on("addmessage", message=>{
                this.message_list.unshift(message)
                this.usercount = ++this.usercount
                this.messagecount = ++this.messagecount
            })
        }
    }
</script>

<style>
    #discuss{
        height: auto;
        margin-top: 50px;
    }

    #discuss hr{
        margin-top: 15px;
    }

    #rightdiscuss{
        float: right;
        position: relative;
        top: -3px;
    }

    #rightdiscuss b{
        font-size: 20px;
        color: red;
    }

    #hot{
        margin-top: 15px;
    }

    .discusscontent{
        padding-top: 20px;
        padding-bottom: 10px;
        overflow: hidden;
        border-bottom: dashed 1px #DCDCDC;

    }

    .avatar{
        width: 60px;
        float: left;
    }

    .content{
        width: auto;
        float: left;
        padding-left: 20px;
    }

    .nameTime{
        width: 593px;
        font-size: 10px;
        color: red;
        position: relative;
        top: 3px;
    }

    .nameTime span{
        color: grey;
        float: right;
    }

    .detail{
        margin-top: 10px;
        font-size: 15px;
    }

    .agree{
        float: right;
        font-size: 15px;
        color: grey;
        margin-right: 10px;
    }

    #seeMore{
        width: 100%;
        height: 24px;
        text-align: center;
        margin-top: 18px;
        background-color:#eeebeb;
        font-size: 12px;
        padding-top: 6px;
        color: #a39f9f;
    }
</style>