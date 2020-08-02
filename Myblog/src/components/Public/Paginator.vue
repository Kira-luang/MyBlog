<template>
    <div id="paginator" v-show=record_show>
        <span>每页{{paginators.perpage}}条记录/共{{paginators.count}}条</span>
        <el-pagination
        background
        hide-on-single-page
        :pager-count = 'page_count'
        layout="prev, pager, next"
        @current-change="currentChange"
        :total="paginators.count">
      </el-pagination>  
    </div>
</template>

<script>
    export default{
        props:['ColumnID'],
        name:'paginator',
        data:()=>{
            return {
            paginators:'',
            page_count:5,
            record_show:true,
            }
        },

        methods:{
          currentChange(page){
            this.$axios.get('column/' + this.ColumnID + '?page=' + page)
          .then(response=>{
            this.paginators = response.data.paginators
            this.$emit('getPaginator', response.data.Article)
            if (this.paginators.num_pages == 1 | this.ColumnID == 1){
              this.record_show = false
            }else{
              this.record_show = true
            }
            }
          )
          .catch(error=>{
            console.log(error)
          })
          },
        },

        created(){
          this.currentChange(1)
        }
    }
</script>

<style>
  #paginator{
    padding-top: 18px;
    padding-left: 93px;
    padding-right: 85px;
    text-align: center;
  }

  #paginator span{
    float: left;
    font-size: 10px;
    position: relative;
    top:8px
  }
</style>