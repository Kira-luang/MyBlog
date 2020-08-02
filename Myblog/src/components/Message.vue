<template>
    <div>
        <commandmodule>
            <!-- 面包屑 -->
            <breakcrumb :columnID="columnID"></breakcrumb>

            <!-- 输入框 -->
            <inputtext v-show='is_login' :path="current_path"></inputtext>

            <!-- 非登陆状态遮盖框 -->
            <needlogin v-show='!is_login'></needlogin>

            <discuss :path="current_path"></discuss>
        </commandmodule>
    </div>
</template>

<script>
    export default{
        name:'message',
        methods:{
            // 验证token是否有效
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

        },
        mounted() {
            this.$store.state.changeCSS(this.$route.path)
        },

        data:()=>{
            return {
            columnID:6,
            is_login:false,
            current_path:''
            }
        },
        created(){
            this.current_path = this.$route.path
            this.judge_token()
        }
    }
</script>

<style scoped>

</style>
