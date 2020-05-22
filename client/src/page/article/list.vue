<template>
  <div class="main">
    <!--功能区-->
    <div class="banner">
      <el-row type="flex">
        <el-col :md="6">
          <el-input
            placeholder="搜索文章"
            prefix-icon="el-icon-search"
            v-model="search_val">
          </el-input>
        </el-col>
        <el-col :md="4">
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
        prop="username"
        label="标题">
      </el-table-column>
      <el-table-column
        align="center"
        prop="city"
        label="作者">
      </el-table-column>
      <el-table-column
        align="center"
        prop="city"
        label="创建时间">
      </el-table-column>
      <el-table-column
        align="center"
        prop="city"
        label="修改时间">
      </el-table-column>
      <el-table-column
        align="center"
        fixed="right"
        min-width="140"
        label="操作">
        <template slot-scope="scope">
          <div v-if="cur_index == scope.row.id">
            <el-button
              @click="handleSave(scope.row)"
              type="text" size="small">保存
            </el-button>
            <el-button
              @click="handleCancel(scope.row)"
              type="text" size="small">取消
            </el-button>
          </div>
          <div v-else>
            <el-button
              @click="handleDialog(scope.row)"
              type="text">赠送
            </el-button>
            <el-button
              @click="handleEdit(scope.row)"
              type="text">修改
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
        :page-size="page_size"
        layout="total, prev, pager, next"
        :total="total"
        @current-change="currentChange">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  export default {

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
