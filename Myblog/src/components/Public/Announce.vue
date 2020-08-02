<template>
    <div id="announce">
        <p><b>版权声明：</b>本站原创文章，于2020-7-23，由Kira发表</p>
        <p><b>转载请注明：</b><router-link to='/'>Kira博客</router-link></p>
    </div>
</template>

<script>
    export default{
        name:'announce'
    }
</script>

<style>
    #announce{
        height: 35px;
        background-color: #EEE8AA;
        padding-top: 30px;
        padding-bottom: 30px;
        padding-left: 20px;
        font-size: 10px;
        line-height: 20px;
        color: #444444;
        border: solid 1px#BDB76B;
    }

    #announce a{
        color: black;
    }
</style>