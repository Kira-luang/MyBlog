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
        name:'technology',
        data:()=>{
            return {
                ColumnID:4,
            }
        },
        provide:{path:'/technology'},
        created() {
            this.$store.state.changeCSS(this.$route.path)
        },
    }
</script>

<style scoped>

</style>