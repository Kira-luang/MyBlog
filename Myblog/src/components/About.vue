<template>
    <div>
        <commandmodule>
            <topnav></topnav>
            <articlelist :ColumnID='ColumnID'></articlelist>
        </commandmodule>
    </div>
</template>

<script>
    export default{
        name:'about',
        provide:{path:'/about'},
        data:()=>{
            return {ColumnID:7}
        },
        mounted() {
            this.$store.state.changeCSS(this.$route.path)
        },
    }
</script>

<style scoped>

</style>