<template>
  <div class="main">
    <!--功能区-->
    <div class="banner">
      <el-row type="flex">
        <el-col :md="2">
          <router-link to="/admin/article/add">
            <el-button size="medium" type="primary" style="margin-left: 10px;">创建</el-button>
          </router-link>
        </el-col>
        <el-col :md="6" :offset="12">
          <el-input
            placeholder="搜索文章"
            prefix-icon="el-icon-search"
            v-model="search_val">
          </el-input>
        </el-col>
        <el-col :md="2">
          <el-button @click="handleSearch" size="medium" type="primary" style="margin-left: 10px;">搜索</el-button>
        </el-col>
      </el-row>
    </div>
    <!--数据列表-->
    <el-table
      :data="table_data"
      style="width: 100%">
      <el-table-column
        align="center"
        fixed="left"
        label="缩略图">
        <template slot-scope="scope">
          <el-image
            style="width: 60px; height: 60px"
            :src="scope.row.image_url"
            fit="contain">
            <div slot="placeholder" class="load_image">
              <i class="el-icon-loading"></i>
            </div>
          </el-image>
        </template>
      </el-table-column>
      <el-table-column
        align="center"
        fixed="left"
        prop="title"
        label="标题">
      </el-table-column>
      <el-table-column
        align="center"
        prop="author"
        label="作者">
      </el-table-column>
      <el-table-column
        align="center"
        prop="create_date"
        label="创建时间">
      </el-table-column>
      <el-table-column
        align="center"
        prop="write_date"
        label="修改时间">
      </el-table-column>
      <el-table-column
        align="center"
        fixed="right"
        min-width="140"
        label="操作">
        <template slot-scope="scope">
          <div>
            <el-button
              @click="handleEdit(scope.row)"
              type="text">编辑
            </el-button>
            <el-button
              @click="handleDelete(scope.row)"
              type="text">删除
            </el-button>
          </div>
        </template>
      </el-table-column>
    </el-table>
    <!--分页-->
    <div class="footer">
      <el-pagination
        background
        layout="total, prev, pager, next"
        @current-change="currentChange">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        table_data: [{
          'image_url': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590247256601&di=72771614f2dd55257e90825d29e8a08d&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853',
          'title': '测试测试测试测试',
          'author': '李家富',
          'create_date': '2020-05-20 13:14:00',
          'write_date': '2020-05-20 13:14:00',
        }],
        search_val: '',
      }
    },
    methods: {
      handleSearch () {
      },
      handleEdit () {
      },
      handleDelete () {
      },
      currentChange () {
      }
    }
  }
</script>

<style scoped>
  .main {
    padding: 12px;
  }

  .banner {
    margin-bottom: 12px;
    padding: 10px;
    background: #ffffff;
  }

  .load_image {
    font-size: 20px;
    line-height: 60px;
  }

  .footer {
    margin-top: 12px;
    margin-bottom: 12px;
    padding: 10px;
    text-align: center;
    background: #ffffff;
  }
</style>
