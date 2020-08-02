<template>
    <div id="connect">
        <p>联系方式</p>
        <br>
        <hr>
        <br>
        <ul>您可以通过以下方式找到我：
            <li>QQ：2920167524</li>
            <li>电话：1585825890</li>
            <li>电子邮箱：2920167524@qq.com</li>
            <li>您也可以直接将想要了解的内容留言给博主喔~</li>
        </ul>

    </div>
</template>

<script>
    export default{
        name:'connect',
        mounted() {
            this.$store.state.changeCSS(this.$route.path)
        },
    }
</script>

<style scoped>
    #connect{
        margin-top: 30px;
        margin-left: 175px;
        margin-right: 175px;
    }

    p{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
    }

    ul{
        margin-left: 40px;
        line-height: 40px;
    }

    li{
        margin-left: 20px;
    }
</style>