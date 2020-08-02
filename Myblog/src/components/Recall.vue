<template>
    <div>
        <commandmodule>
            <topnav></topnav>
            <articlelist  :ColumnID='ColumnID'></articlelist>
        </commandmodule>
    </div>
</template>

<script>
    export default{
        name:'recall',
        provide:{path:'/recall'},
        data:()=>{
            return {ColumnID:3}
        },
        mounted() {
            this.$store.state.changeCSS(this.$route.path)
        },
    }
</script>

<style scoped>

</style>