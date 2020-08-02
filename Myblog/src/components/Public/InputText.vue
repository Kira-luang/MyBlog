<template>
    <div>
        <el-input
        type="textarea"

        :rows="5"
        placeholder="请输入内容"
        v-model="textarea">
        </el-input>
        <p><el-button type="primary" @click="sendMessage">发送消息</el-button></p>
    </div>
</template>

<script>
    export default{
        props:["path"],
        name:"inputtext",
        data:()=>{
            return {'textarea': ''}
        },
        created(){
            console.log(this.path)
        },
        methods:{
            sendMessage(){
                let token = localStorage.getItem('token')
                let formData = new FormData()
                formData.append('content', this.textarea)
                formData.append('token', token)
                if (this.path == "/message"){
                    var post_path = 'message/'
                }else{
                    var post_path = 'aticlemessage/'
                    formData.append('article', this.path)
                }
                this.$axios.post(post_path, formData)
                .then(response=>{
                    let message = response.data
                    this.$event.$emit('addmessage', message)
                    this.textarea = ''
                })
                .catch(error=>{
                    console.log(error)
                })
            },
        }
    }
</script>

<style scoped>
    div{
        margin-top: 15px;
    }
    
    p{
        margin-top: 3px;
        text-align: right;
    }
</style>
