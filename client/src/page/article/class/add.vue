<template>
  <div class="main">
    <el-form ref="form" :model="data" label-width="82px">
      <el-form-item label="名称">
        <el-input v-model="data.name" label="名称"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button v-if="!edit" type="primary" @click="handleAdd">添加</el-button>
        <el-button v-else type="primary" @click="handleAdd">修改</el-button>
        <el-button @click="$router.back(-1)">返回</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        edit: false,
        data: {
          title: 'name'
        }
      }
    },
    created () {
      let components_name = this.$route.name;
      let class_id = this.$route.params.class_id;
      if (components_name == 'ArticleClassEdit') {
        this.edit = true;
        this.getData(class_id);
      }
    },
    methods: {
      getData (class_id) {
        let params = {};
        params.class_id = class_id;
        this.$axios.get('/api/admin/article/class', {params: params})
          .then((res) => {
            if (!res.data.code) {
              this.data = res.data.data;
            } else {
              this.$message.error(res.data.msg);
              this.$router.push('/admin/article/class');
            }
          })
          .catch((err) => {
            console.log(err);
          })
      },
      handleAdd () {
        if (!this.data.name) {
          this.$message.error('名称不能为空');
          return false;
        }
        this.handleSubmit();
      },
      handleSubmit () {
        let data = new FormData();
        data.append('name', this.data.name);
        if (!this.edit) {
          // 添加数据
          this.$axios.post('/api/admin/article/class', data)
            .then((res) => {
              if (!res.data.code) {
                this.$router.push('/admin/article/class');
                this.$message.success(res.data.msg);
              } else {
                this.$message.error(res.data.msg);
              }
            })
            .catch((err) => {
              console.log(err);
            })
        } else {
          // 修改数据
          data.append('class_id', this.data.id);
          this.$axios.put('/api/admin/article/class', data)
            .then((res) => {
              if (!res.data.code) {
                this.$router.push('/admin/article/class');
                this.$message.success(res.data.msg);
              } else {
                this.$message.error(res.data.msg);
              }
            })
            .catch((err) => {
              console.log(err);
            })
        }
      }
    }
  }
</script>

<style scoped>
  .avatar-uploader {
    display: inline-block;
    vertical-align: top;
  }

  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }

  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }

  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    text-align: center;
  }

  .avatar {
    display: inline-block;
    width: 146px;
    height: 146px;
    border: 1px dashed #409EFF;
    border-radius: 6px;
    vertical-align: top;
    margin-right: 10px;
  }

  .main {
    padding: 30px 50px 10px;
    border-radius: 10px;
    background: #ffffff;
  }
</style>
