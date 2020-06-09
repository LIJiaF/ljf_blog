<template>
  <div class="main">
    <el-form ref="form" :model="data" label-width="82px">
      <el-form-item label="分类">
        <el-select v-model="data.class_id" placeholder="请选择">
          <el-option
            v-for="item in article_class"
            :key="item.id"
            :label="item.name"
            :value="item.id">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="标题">
        <el-input v-model="data.title" label="标题"></el-input>
      </el-form-item>
      <el-form-item label="缩略图">
        <el-image
          class="avatar"
          fit="contain"
          v-if="data.image_url"
          :src="data.image_url"></el-image>
        <el-upload
          class="avatar-uploader"
          list-type="picture-card"
          ref="upload"
          :limit="1"
          :auto-upload="false"
          :action="action"
          :on-exceed="handleExceed"
          :on-change="handleChange"
          :on-success="handleSuccess"
          :on-error="handleError">
          <i class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-form-item>
      <el-form-item label="描述">
        <el-input type="textarea" v-model="data.note" label="描述" :rows="2" resize="none"></el-input>
      </el-form-item>
      <el-form-item label="内容">
        <Editor :content="data.content" @getEditorContent="getEditorContent"></Editor>
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
  import Editor from '@/components/editor'

  export default {
    props: ['article_id'],
    data () {
      return {
        action: 'http://127.0.0.1:8888/upload',
        edit: false,
        article_class: [],
        data: {
          class_id: null,
          title: '',
          image_url: '',
          note: '',
          content: ''
        }
      }
    },
    components: {
      Editor
    },
    created () {
      // 获取分类
      this.getClassData();
      // 判断是否是修改
      let components_name = this.$route.name;
      if (components_name == 'ArticleEdit') {
        this.edit = true;
        this.getData(this.article_id);
      }
    },
    methods: {
      getClassData () {
        this.$axios.get('/api/admin/article/class/all')
          .then((res) => {
            this.article_class = res.data;
          })
          .catch((err) => {
            console.log(err);
          })
      },
      getData (article_id) {
        let params = {};
        params.article_id = article_id;
        this.$axios.get('/api/admin/article', {params: params})
          .then((res) => {
            if (!res.data.code) {
              this.data = res.data.data;
            } else {
              this.$message.error(res.data.msg);
              this.$router.push('/admin/article');
            }
          })
          .catch((err) => {
            console.log(err);
          })
      },
      getEditorContent (content) {
        this.data.content = content;
      },
      handleAdd () {
        if (!this.data.class_id) {
          this.$message.error('分类不能为空');
          return false;
        }
        if (!this.data.title) {
          this.$message.error('标题不能为空');
          return false;
        }
        if (!this.data.content) {
          this.$message.error('内容不能为空');
          return false;
        }
        if (this.$refs.upload.uploadFiles.length) {
          this.$refs.upload.submit();
        } else {
          this.handleSubmit();
        }
      },
      handleExceed () {
        this.$message.error('最多只能上传一张图片');
      },
      handleChange (file) {
        let is5M = file.raw.size < 2 * 1024 * 1024;
        let isType = (file.raw.type === 'image/jpeg' || file.raw.type === 'image/png');
        if (!is5M) {
          this.$message.error('大小超出2M');
          this.$refs.upload.clearFiles();
          return false;
        }
        if (!isType) {
          this.$message.error('图片类型只能是jpg/png');
          this.$refs.upload.clearFiles();
          return false;
        }
      },
      handleSuccess (response) {
        if (!response.code) {
          this.data.image_url = response.image_url;
          this.handleSubmit();
        }
      },
      handleError (err) {
        this.$message.error(JSON.parse(err.message).msg);
      },
      handleSubmit () {
        let data = new FormData();
        data.append('class_id', this.data.class_id);
        data.append('title', this.data.title);
        data.append('image_url', this.data.image_url);
        data.append('note', this.data.note);
        data.append('content', this.data.content);
        if (!this.edit) {
          // 添加数据
          this.$axios.post('/api/admin/article', data)
            .then((res) => {
              if (!res.data.code) {
                this.$router.push('/admin/article');
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
          data.append('article_id', this.data.id);
          this.$axios.put('/api/admin/article', data)
            .then((res) => {
              if (!res.data.code) {
                this.$router.push('/admin/article');
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
