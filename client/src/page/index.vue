<template>
  <div class="main">
    <!--头部-->
    <div class="header">
      <h1 class="title">后台管理系统</h1>
      <ul class="menu">
        <router-link to="/admin">
          <li class="active">首页</li>
        </router-link>
      </ul>
    </div>
    <div>
      <!--侧边栏-->
      <div class="aside">
        <el-menu
          :default-active="activeIndex"
          :unique-opened="true"
          class="el-menu-vertical-demo">
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-document"></i>
              <span>文章管理</span>
            </template>
            <router-link to="/admin/article">
              <el-menu-item index="article">文章列表</el-menu-item>
            </router-link>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-document"></i>
              <span>用户管理</span>
            </template>
            <router-link to="/admin/user">
              <el-menu-item index="user">用户列表</el-menu-item>
            </router-link>
          </el-submenu>
        </el-menu>
      </div>
      <!--内容-->
      <div class="content">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        activeIndex: ''
      }
    },
    created () {
      this.activeIndex = this.$route.path.split('/')[2];
    },
  }
</script>

<style scoped>
  .el-menu {
    height: 100%;
  }

  .header {
    min-width: 525px;
    background: #6495ED;
    overflow: hidden;
  }

  .title {
    float: left;
    width: 250px;
    padding: 15px;
    font-size: 28px;
    text-align: center;
    color: #ffffff;
    box-sizing: border-box;
  }

  .menu {
    float: left;
    overflow: hidden;
  }

  .menu li {
    float: left;
    color: #ffffff;
    padding: 23px 20px;
  }

  .menu li.active {
    background: #673ab7;
  }

  .aside {
    position: fixed;
    top: 67px;
    bottom: 0;
    width: 250px;
    background: #ffffff;
  }

  .content {
    position: fixed;
    top: 67px;
    left: 250px;
    right: 0;
    bottom: 0;
    overflow: auto;
    padding: 10px;
  }
</style>
