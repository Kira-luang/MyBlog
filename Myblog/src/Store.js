import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default  new Vuex.Store({
    state: {
      count: 0,

      // 当创建的时候修改导航样式,要不然返回和刷新时候会失去样式(组件统一控制样式的方法)
      changeCSS:(path)=>{
        let navbars = document.getElementsByClassName('el-menu-item')
        for (let i = 0; i < navbars.length; i++) {
          let element = navbars[i];
          if (element.getAttribute('path')==path) {
            element.style="color: rgb(255, 208, 75); border-bottom-color: rgb(255, 208, 75); background-color: rgb(145, 145, 145);"
          }else{
            element.style="color: rgb(255, 255, 255); border-bottom-color: transparent; background-color: rgb(145, 145, 145);"
          }
        }  
      },
      
    },
    mutations: {
      increment (state, number) {
        console.log(state.count, number)
        state.count += number
      }
    },

    actions:{
        Asyncincrement({commit}, number){ // 支持异步操作
          setTimeout(()=>{
              console.log(number)
              commit('increment', number)
          }, 50)
      },

    },
  })