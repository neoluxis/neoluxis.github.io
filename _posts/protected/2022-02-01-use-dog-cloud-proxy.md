---
layout: article
author: Neolux Lee
title: 使用v2ray和dogcloud翻墙
date: 2022-02-01
tags: 翻墙 v2ray
---



#  V2Ray&狗云连接国外网站



## （一）. 下载客户端

​			GitHub下载

​			[点击到达GitHub下载Windows版本](https://github.com/2dust/v2rayN)			![image-20210808190340654](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808190340654.png)

 * 两种方式

   	1. 下载core到本地解压
    	2. 红框的两个都下载，解压后文件夹合并

* 解压后文件如下（这个没有参考价值）![image-20210808191011081](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808191011081.png)

* ![image-20210808191049282](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808191049282-164380648493424.png)

  点击后没有界面，会在托盘有一个图标，点击图标可打开主界面。![image-20210808191205543](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808191205543.png)

  未配置状态应该是这样![image-20210808191229280](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808191229280.png)

  这样客户端就算安装好了，下面来配置服务器连接国外网站。






## （二）获取订阅链接/服务器链接

​	这里给推荐一个服务器提供商：狗子云。

​	它提供了免费的服务器订阅链接，如果没(xiang)有(yao)资(bai)金	(piao)的话,可以使用这里的服务器订阅节点。[<img src="https://s2.loli.net/2022/02/01/OlNR6v4rXTSFiL9.png" alt="dogHead" style="zoom:12%;" />点击直达](https://dogcloud.best)



1. 在浏览器地址栏输入： https://dogcloud.best 或者点击到达[<img src="https://s2.loli.net/2022/02/01/OlNR6v4rXTSFiL9.png" alt="dogHead" style="zoom:12%;" />点击直达](https://dogcloud.best)。这是一个地址发布页，进入后点击跳转到最新地址

   ![image-20210808181714003](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808181714003.png)

2. 注册账号

   ![image-20210808181844377](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808181844377.png)

   ![image-20210808182048248](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808182048248.png)

   * 值得一提的是，狗子云注册时并没有进行邮箱的验证，所以你可以使用任何合法的邮箱进行注册。什么是合法的邮箱呢？这里的合法不是指符合法律，而是符合邮箱的格式。比如shittyCCP@example.mail.com并不是不合法，而GreatChina@example、ILoveChina.example不合法。总之，你注册的邮箱只要是XXX@XXX.XXX就行，如果提示无法注册，不要怕，换一个邮箱就行了。

     这也就是说，我们并不需要狗子云中的登录领取丰(han)厚(suan)的国外流量，当流量用完的时候，只要再注册一个就行了。

   * 再一，上述方法非必要不使用。否则可能会引起提供商注意。

3. 登录狗子云

   进入后是这个页面（不同设备界面可能不同）

   ![image-20210808183526331](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808183526331-164380650292630.png)

   下滑找到“复制v2ray订阅链接”（如果你用的是Clash，复制Clash配置）

   ![image-20210808183713183](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808183713183-164380650687133.png)

   点击复制后打开v2ray客户端

   ![image-20210808183953625](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808183953625.png)

   

## （三）配置v2ray客户端

1. 点击订阅>订阅设置

   ![image-20210808184206868](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808184206868.png)

   ​	按照图示填入信息。

2. 更新订阅&连接服务器

   点击订阅>更新订阅，你会发现列表里多出了几个服务器

   ![image-20210808184349679](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808184349679.png)

   图中的前两个服务器是可连接使用的，后面三个是为你提供的信息，以防止你找不到网页的地址。

   连接服务器：

   在右下角托盘里找到v2ray的图标，右键单击

   ![image-20210808184628626](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808184628626.png)

   点击服务器，确认可用的服务器已被勾选![image-20210808184816246](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808184816246.png)

   点击系统代理，选择自动配置系统代理（或者全局代理）![image-20210808184911275](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808184911275.png)



​		你会发现图标变红![image-20210808184951081](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808184951081.png)

​		这就代表连接成功了

3. 在墙外愉快遨游

   打开浏览器，地址栏中输入：https://www.youtube.com

   如果能够访问说明连接成功，你可以快乐地玩耍了

   ![image-20210808185616032](/assets/img/2022-02-01-use-dog-cloud-proxy_imgs/image-20210808185616032.png)

   * 注意：这里使用的是免费版，速度不能保证，所以不推荐用来进行游戏联机，尤其是对速度要求高的游戏。日常看看谷歌学术之类的还可以。
   * 如果你对这个方法不满，你还可以在YouTube上面搜索更多方法去 Be Free。在这里就不再说了，一般你可以对照视频进行配置。







