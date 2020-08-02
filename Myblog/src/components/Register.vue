<template>
    <div id="main">
        <p style="margin-bottom: 10px;"><b style="font-size: 20px;">欢迎您访问Kira博客</b></p>
        <div id="fromtable">
            
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
                <el-form-item label="用户名" prop="name">
                  <el-input v-model="ruleForm.name" placeholder="请输入3-18个字符的用户名"></el-input>
                </el-form-item>

                <el-form-item label="密码" prop="password">
                    <el-input v-model="ruleForm.password" placeholder="请输入5-26个字符的密码"></el-input>
                  </el-form-item>

                  <el-form-item label="邮箱" prop="email">
                    <el-input v-model="ruleForm.email" placeholder="请输入您的邮箱"></el-input>
                  </el-form-item>

                  <el-form-item label="上传头像：" prop="headImg">
                    <el-upload
                    class="upload-demo"
                    drag
                    :before-upload="beforeAvatarUpload"
                    action="https://jsonplaceholder.typicode.com/posts/"
                    multiple>
                    <i class="el-icon-upload"></i>
                    <div class="el-upload__text" v-html="imgtext"></div>
                    <div class="el-upload__tip" slot="tip">{{imgTip}}</div>
                    </el-upload>
                  </el-form-item>


                <el-form-item>
                  <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
                  <el-button @click="resetForm('ruleForm')">重置</el-button>
                </el-form-item>
              </el-form>

              <router-link to="/login"><p id="login">点击登陆</p></router-link>
        </div>
    </div>
</template>

<script>
    export default{
        name:"loginregister",
        data() {
      return {
        test:true,
        imgTip:'只能上传jpg/png文件，且不超过500kb',
        imgtext:'将文件拖到此处，或<em>点击上传</em>',

        ruleForm: {
          name: '',
          password:'',
          email:'',
          headImg:false,
          imgobj:'',
        },
        rules: {
          name: [
            { required: true, message: '请输入名称', trigger: 'blur' },
            { min: 3, max: 18, message: '长度在 3 到 18 个字符', trigger: 'blur' }
          ],
          password: [
            { required: true, message: '请选择密码', trigger: 'blur' },
            { min: 5, max: 26, message: '长度在 5 到 26 个字符', trigger: 'blur' }
          ],
          email: [
            { required: true, message: '请选择密码', trigger: 'blur' }
          ],
          
        }
      };
    },
    methods: {
      submitForm(formName) {
// 对整个表单进行校验的方法，参数为一个回调函数。该回调函数会在校验结束后被调用，并传入两个参数：
// 是否校验成功和未通过校验的字段。若不传入回调函数，则会返回一个 promise
        this.$refs[formName].validate((valid) => {
          if (valid) {
            let fromData = new FormData()
            fromData.append('username', this.ruleForm.name)
            fromData.append('password', this.ruleForm.password)
            fromData.append('headimg', this.ruleForm.imgobj)
            fromData.append('email', this.ruleForm.email)
            let config = {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                    };
            this.$axios.post('users/', fromData, config)
            .then(response=>{
                console.log(response)
                this.$router.push({path:'/login'})
            })
            .catch(error=>{
                console.log(error)
            })
            console.log(this.ruleForm)
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },

      // 对整个表单进行重置，将所有字段值重置为初始值并移除校验结果
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },

      // 图片自动上传终端,并把其保存在参数里
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isPNG = file.type === 'image/png';
        const isLt2M = file.size / 1024 / 1024 < 2;
        if (!isJPG & !isPNG) {
          this.$message.error('上传头像图片只能是 JPG和PNG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        this.imgTip = '图片上传成功'
        this.imgtext = '图片上传成功'
        this.ruleForm.imgobj = file
        return false
      }
    }
  }

</script>

<style scoped>
    #main{
        width: 100%;
        text-align: center;
        margin-top: 20px;
    }

    #fromtable{
        width: 400px;
        height: 500px;
        border: solid 1px;
        padding-top: 20px;
        margin: auto;
        text-align: left;
    }

    .el-form-item{
        padding-left: 30px;
    }

    .el-input{
        width: 200px;
        position: relative;
        left: 0px;
    }

    

    .el-upload__tip{
      margin-top: 0px;
    }
    
    #login{
      text-align: center;
      font-size: 13px;
      position: relative;
      top: -10px;
    }
</style>
