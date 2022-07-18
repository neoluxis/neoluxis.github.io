# 使用 v2rayN 翻墙

## 前言

v2ray是一个比较流行的翻墙客户端，如今的v2ray不仅支持vmess，vless协议的服务器，更是兼容了trojan，ss，ssr协议的服务器，可以说是最强大的翻墙客户端。

而且，v2ray可以在Windows，Linux，Android多种平台上运行。

Windows可以使用v2rayN或v2rayN-core，还有其他的图形界面

Linux可以使用数种图形化界面方便配置，也可以使用命令行配置服务器

Android可以使用v2rayNG客户端，其可以支持多种协议，可以说是安卓平台较强的客户端了

## 下载

[点击前往GitHub下载v2rayN发行版](https://github.com/2dust/v2rayN/releases)

![image-20220713125348707](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410813.png)

下载 v2rayN.zip 即可，也可以使用v2rayN-core。二者使用方法类似。

## 使用

### 1. 添加服务器

zip文件下载完成后解压到一个文件夹![image-20220713131637071](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410815.png)

点击这个文件打开，任务栏右下角会出现图标 

**注意：不会出现主页面，直接到右下角寻找图标便好**

![image-20220713131934376](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410816.png)

双击可以打开主页面

![image-20220713132038635](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410818.png)

首次进入没有任何服务器，需要手动添加服务器

如果你获得了服务器的列表（或者json文件），那么只需要复制文件内容（服务器信息），在主界面内添加即可。

![image-20220713134618167](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410819.png)

![q2](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410820.gif)![q1](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410821.gif)

还可以在任务栏直接添加，比较方便：

![image-20220713133641494](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410822.png)

如图，右键点击任务栏图标后，菜单中不但有“从剪贴板导入url”，还可以扫描屏幕二维码添加链接。

### 2. 添加订阅

v2rayN可以使用单独的服务器，还可以添加订阅链接：

![image-20220713135333637](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410823.png)

点击订阅设置就可以添加订阅

![image-20220713135443426](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410824.png)

填写必要信息就行了。

备注随便填写，地址就是订阅链接，用户代理（UA）也根据服务器提供商填写，分组可以自由设定。最后把启用勾选就算完成

![image-20220713135625699](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410825.png)

添加订阅之后点击更新订阅就可以看到订阅中包含的服务器了![image-20220713135703870](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410826.png)

同样的，任务栏也可以更新订阅。

### 3. 连接到代理服务器

![image-20220713135814168](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410827.png)

如图我们已经添加了服务器和订阅链接，更新后得到了服务器列表。

![image-20220713140037445](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410828.png)

全部选中后右键单击，进行测速。测速完成后点击```测试结果```表头排序。

选择一个较快的服务器，按住<kbd>enter</kbd>就可以将其设置为活动服务器。活动服务器左边会显示一个对勾。

![image-20220713140212217](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410829.png)

之后在任务栏中点击选择```自动配置系统代理```![image-20220713140312294](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410830.png)

图标会变成红色![image-20220713140344109](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410831.png)

说明已经连接

连接成功后就可以访问特殊的网站了![image-20220713140456274](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/202207131410832.png)

## 后记

这是Windows平台比较好用的一款代理软件。我刚开始翻墙时，这个软件功能还不如现在这般齐全。但是现在软件不断更新，功能也不断加强。现在的v2rayN已经可以和winXray相媲美（详见博客[科学上网安卓客户端——AnXray](http://neolux.run.goorm.io/2022/07/11/anxray-proxy.html)。如果有人问我翻墙软件，我一定会毫不犹豫地推荐这款软件。👍

