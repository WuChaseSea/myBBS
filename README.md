# myBBS

## 项目简介

&emsp;&emsp;论坛系统

## 数据库说明

&emsp;&emsp;使用的数据库为MySQL，用户名为bbs_admin,密码是000821，数据库名bbs，已经授予所有权限；

## 详细步骤

### 建立项目文件

1. 在整个项目中新建应用程序boards，并在setting.py文件中修改相关设置。对于BBS这种简单网站来说，建立一个应用程序已经足够。（记得修改数据库的设置，不然默认是将之后建立的模型存到db.sqlite3中了）；  
2. 建立模型。在应用程序boards中的models.py中添加自己的模型，然后将其迁移到数据库中。然后在shell中已经添加两个版块做测试用； 

### 创建版块界面

1. 建立模板。home.html表示版块的页面；  
2. 测试用例。test.py中进行测试；  
3. 静态文件。引入js，css等一些静态文件；  
4. 创建管理员账户。账户名：admin，邮箱：admin@bbs.com，密码：lover520；  
5. 进入admin界面之后，添加了一个新版块；  

### 从版块链接到主题

1. 给某一个具体的版块添加url，并进行了测试；  
2. 添加导航链接，版块可以链接到主题列表页面，主题列表页面可以回到版块页面；  
3. 复用模板；  
4. 在fonts.google.com上面寻找字体并应用；  

### 创建新主题界面

1. 表单处理。创建一个添加主题的界面；  
2. 添加数据之后在主题界面中显示；  
3. 在主题界面添加“新主题”按钮跳到添加新主题界面；  
4. 将创建新主题的界面整成表单形式，使用表单；  
5. 渲染表单；
6. 复用表单模板；

### 用户注册

1. 创建新的app；  
2. 添加新的注册用户界面；  
3. 注册完用户之后会返回版块界面；  
4. 在模板上中引用已认证的用户；  
5. 美化注册模板；
