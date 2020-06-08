<template>
  <div class="main">
    <!--功能区-->
    <div class="banner">
      <el-row type="flex">
        <el-col :md="2">
          <router-link to="/admin/article/class/add">
            <el-button size="medium" type="primary" style="margin-left: 10px;">创建</el-button>
          </router-link>
        </el-col>
        <el-col :md="6" :offset="12">
          <el-input
            placeholder="搜索分类"
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
        prop="name"
        label="名称">
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
            <router-link :to="{name: 'ArticleClassEdit', params: {class_id: scope.row.id}}">
              <el-button
                type="text">编辑
              </el-button>
            </router-link>
            <el-button
              @click="handleDelete(scope.row.id)"
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
        :total="total"
        :page-size="page_size"
        @current-change="currentChange">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        table_data: [],
        search_val: '',
        total: 0,
        page_size: 0,
      }
    },
    created () {
      this.getData();
    },
    methods: {
      getData (cur_page = 1) {
        let params = {};
        params.cur_page = cur_page;
        this.$axios.get('/api/admin/article/class/list', {params: params})
          .then((res) => {
            this.table_data = res.data.data;
            this.page_size = res.data.page_size;
            this.total = res.data.total;
          })
          .catch((err) => {
            console.log(err);
          })
      },
      handleSearch () {
      },
      handleDelete (class_id) {
        this.$confirm('此操作将永久删除该分类, 是否继续?', '提示', {
          cancelButtonText: '取消',
          confirmButtonText: '确定',
          type: 'warning',
          center: true
        }).then(() => {
          let params = {};
          params.class_id = class_id;
          this.$axios.delete('/api/admin/article/class', {params: params})
            .then((res) => {
              if (!res.data.code) {
                if (this.cur_page > 1 && this.table_data.length <= ((this.cur_page - 1) * this.page_size) + 1) {
                  this.cur_page = this.cur_page - 1;
                }
                this.getData(this.cur_page);
                this.$message({
                  type: 'success',
                  message: res.data.msg,
                  showClose: true
                });
              } else {
                this.$message({
                  message: res.data.msg,
                  type: 'error',
                  showClose: true
                });
              }
            })
            .catch((err) => {
              console.log(err);
            });
        }).catch(() => {
        });
      },
      currentChange (cur_page) {
        this.getData(cur_page);
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
