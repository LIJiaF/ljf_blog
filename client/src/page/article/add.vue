<template>
  <div class="main">
    <el-form ref="form" :model="data" label-width="82px">
      <el-form-item label="标题">
        <el-input v-model="data.title" label="标题"></el-input>
      </el-form-item>
      <el-form-item label="缩略图">
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
          <img v-if="data.image_url" :src="data.image_url" class="avatar">
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-form-item>
      <el-form-item label="内容">
        <Editor @getEditorContent="getEditorContent"></Editor>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleAdd">添加</el-button>
        <el-button @click="$router.back(-1)">返回</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import Editor from '@/components/editor'

  export default {
    data () {
      return {
        action: 'http://127.0.0.1:8888/upload',
        data: {
          title: '',
          image_url: '',
          content: ''
        }
      }
    },
    components: {
      Editor
    },
    methods: {
      getEditorContent (content) {
        this.data.content = content;
      },
      handleAdd () {
        if (!this.data.title) {
          this.$message.error('标题不能为空');
          return false;
        }
        if (!this.data.content) {
          this.$message.error('内容不能为空');
          return false;
        }
        this.$refs.upload.submit();
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
        console.log(response);
      },
      handleError (err) {
        this.$message.error(JSON.parse(err.message).msg);
      }
    }
  }
</script>

<style scoped>
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

  .main {
    padding: 30px 50px 10px;
    border-radius: 10px;
    background: #ffffff;
  }
</style>
