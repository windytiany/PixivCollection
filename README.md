<h1 align="center"><span style="color: #0398fa;">Pixiv</span>Collection</h1>

![preview](docs/screenshot.jpg)

## 简介

[原作者示例站点](https://pixiv.orilight.top/)

浏览个人收藏的P站图片。

图片数据一次性全部加载，图片较多时可能需要较长的时间。

## 功能

- 图片浏览
  - 瀑布流布局，可自定义瀑布流列数与间隔
  - 简易的图片浏览器，支持PC端和移动端的图片缩放与拖动
- 图片筛选
  - 通过发布年份、形状、尺寸、不健全度、R18、作者、标签、收藏数筛选图片
- 图片搜索
  - 通过图片id、图片标题、作者id、作者昵称、标签、标签翻译搜索图片
- 夜间模式
- 全屏模式

## 使用
初次使用请点击右上方的“设置”按钮，设置`Images path`和`Json path`
`Images path`是存放图片的文件夹的路径
`Json path`是保存图片元数据的json文件的路径
关于图片文件夹与json文件结构，请参考原项目

## 从源码构建

1.构建前端

> [!NOTE]
> 构建前端需要安装 NodeJS 环境及 PNPM 包管理器

```bash
cd web

# 安装依赖
pnpm i

# 构建前端
pnpm build
```

构建后的前端文件位于 `web/dist` 目录下

2.构建后端

> [!NOTE]
> 需要Python环境，本地版本为3.10.16

```bash
cd server

# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
.venv/Scripts/activate

# 安装依赖
pip install fastapi[standard]
```

3.打包

```bash
# 安装依赖
pnpm i

# 打包
pnpm dist
```
