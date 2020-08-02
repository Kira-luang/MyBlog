<template>
    <div id="main">
        <h3>无敌Kira</h3>
        <div id="loginview">

            <div class="login">
                <p>用户名</p>
                <el-input v-model="username" placeholder="请输入用户名" prefix-icon="el-icon-s-custom"></el-input>
            </div>

            <div class="login">
                <p>密码</p>
                <el-input v-model="password" placeholder="请输入密码" type="password"  prefix-icon="el-icon-lock"></el-input>
            </div>


            <div class="login">
                <p>验证码</p>
                <el-input v-model="inputCode" placeholder="请输入验证码" style="width: 150px;"></el-input>
                <div id="code"><p>{{Code}}</p></div>
            </div>

            <div id="submit">
            <el-button type="primary" :loading="onLoad" @click="submit">{{buttonText}}</el-button>
        </div>
        <router-link to="/register"><p id="register">点击注册</p></router-link>

        </div>
    </div>
</template>

<script>
    export default{
        name:'login',

        data:()=>{
            return {
                Code:'',
                onLoad:false,
                username:'',
                password:'',
                inputCode:'',
                buttonText:'登陆',
            }
        },

        methods:{
            submit(){
                if (this.Code == this.inputCode){
                    this.onLoad=true
                    this.buttonText = '加载中'
                    let formData = new FormData()
                    formData.append('username', this.username)
                    formData.append('password', this.password)
                    formData.append('action', 'login')
                    this.$axios.post('users/', formData)
                    .then(response=>{
                        this.$router.push({path:'/'})
                        localStorage.setItem('token', response.data.token)
                    })
                    .catch(error=>{
                        this.onLoad = false
                        this.buttonText = '登陆'
                        this.username = ''
                        this.password = ''
                        this.inputCode = ''
                        this.$message({
                            message: '警告:'+ error.response.data.message,
                        type: 'error'
                        });
                        console.log(error.response.status)
                    })
                }else{
                    this.$message({
                        message: '警告: 输入验证码错误',
                        type: 'error'
                        });
                }
            }
        },

        created(){
            let number = Math.random().toString()
            this.Code = number.substring(2, 6)
        }
    }
</script>

<style scoped>
    #main{
        text-align: center;
        margin-top: 30px;
    }

    #loginview{
        width: 350px;
        height: 380px;
        border: solid 1px;
        border-radius: 15px;
        margin: auto;
    }

    .login{
        width: 250px;
        margin: auto;
        text-align: left;
        margin-top: 12px;
        line-height: 30px;
    }

    .login p{
        margin-left: 5px;
        font-size: 12px;
    }

    .el-input{
        width: 250px;
        position: relative;
        left: 0px;
    }

    #code{
        width: 83px;
        height: 35px;
        margin-left: 10px;
        text-align: center;
        border: solid 1px #DCDFE6;
        border-radius: 5px;
        display: inline-block;
        position: relative;
        top: 3px;
        background-color: white;
    }

    #code p{
        font-size: 20px;
        font-weight: 900;
        text-align: center;
        letter-spacing: 5px
    }

    #submit{
        margin-top: 40px;
    }

    #submit .el-button{
        width: 255px;
    }

    #register{
        margin-top: 15px;
        font-size: 10px;
    }
</style>