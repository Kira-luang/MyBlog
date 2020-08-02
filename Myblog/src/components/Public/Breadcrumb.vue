<template>
    <div id="Breadcrumb">
        <p><b>您现在的位置是：&nbsp;</b>
            <router-link to="/">首页</router-link>&nbsp;&nbsp;&gt;&nbsp;
            <router-link :to="link">{{columnName}}</router-link>&nbsp;&nbsp;&gt;</p>
            <hr>
    </div>
</template>

<script>
    export default{
        name:"breakcrumb",
        props:['columnID'],
        data:()=>{
            return {
                link:'',
                columnName:''
            }
        },
        watch:{
            columnID(ID, oldID){
                this.getColumn(ID)
            }
        },

        methods:{
            getColumn(id){
                this.$axios.get('singlecolumn/?id=' + id)
            .then(response=>{
                this.link = response.data.path
                this.columnName = response.data.name
            })
            .catch(error=>{
                console.log(error)
            })
            }
        },

        created(){
            if (this.columnID){
                this.getColumn(this.columnID)
            }
        }
    }
</script>

<style>
    #Breadcrumb{
        font-size: 18px;
        margin-top: 30px;
    }

    #Breadcrumb a{
        color: black;
    }

    #Breadcrumb hr{
        height: 4px;
        background-color: grey;
        margin-top: 8px;
    }
</style>