<template>
    <div>
        <p>很抱歉,您需要登陆后才能留言&nbsp;
            <router-link to="/login">登陆</router-link>&nbsp;|&nbsp;<router-link to="/register">立即注册</router-link>
        </p>
    </div>
</template>

<script>
    export default{
        name:'needlogin'
    }
</script>

<style scoped>
    div{
        width: 668px;
        height: 138px;
        border: solid 1px;
        text-align: center;
        margin-top: 28px;
    }

    p{
        margin-top: 60px;
        font-size: 15px;
    }
</style>