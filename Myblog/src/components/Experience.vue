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
        name:'experience',
        provide:{path:'/experience'},
        data:()=>{
            return {ColumnID:5}
        },
        mounted() {
            this.$store.state.changeCSS(this.$route.path)
        },
    }
</script>

<style scoped>

</style>