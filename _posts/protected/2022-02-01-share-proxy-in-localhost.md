---
layout: article
author: Neolux Lee
title: 局域网共享代理设置
date: 2022-02-01
tags: 翻墙 
---

# 局域网共享代理

我们平时在自己的电脑上手机上可能用到国外的代理，那么，有没有一种方法可以让“一人代理，全家YouTube”吗？其实，在很多代理软件中，都会有这样的功能：在局域网中共享正在使用的代理服务器。只要确保这台设备的代理服务正常，在局域网中的所有设备都可以使用这个代理并访问国外网站。

下面就让我以WinXray为例示范如何进行这样的操作吧。

## 开启局域网共享设置

在设置里面，可以看到有“允许来自局域网的连接”的选项，我们将它勾选，之后确定自己的端口。如果你的其他设备使用的是HTTP代理，就记住这里这值得HTTP代理端口；如果是ShadowSocks/SSR就记住Socks端口。![image-20210812105614341](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812105614341.png)

之后我们打开终端<kbd>win</kbd>+<kbd>x</kbd>=>打开WindowsTerminal（Windows10 是Powershell，我这里用的是Windows11）![image-20210812110053255](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812110053255.png)

在终端中运行下列命令

```powershell
PS C:\Users\Administrator> ipconfig
```

找到你正在使用的适配器，查看IPv4地址![image-20210812110410128](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812110410128.png)

这些信息都获取后，就可以连接了

## 其他设连接（手机为例）

现在我已经在一个全新的安卓模拟器中打开浏览器，可以看到此时YouTube和Google都是是不能访问的![image-20210812112510482](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812112510482.png)

![image-20210812112438889](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812112438889.png)



下面我们就开始连接到电脑的代理

1. 打开设置，连接到同一个局域网![image-20210812112557048](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812112557048.png)

   这里使用的是模拟器，所以已经连接到WiFi

2. 编辑WiFi设置
   打开WiFi高级设置，在代理一栏选择手动![image-20210812112733517](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812112733517.png)

3. 填入信息

   主机名就填入刚刚查到的IPv4地址，端口填入你的端口![image-20210812112916111](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812112916111.png)

保存之后再打开浏览器看看![image-20210812113216087](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812113216087.png)此时已经可以正常打开了

我们打开一个视频，看看访问速度是否会降低

电脑：![image-20210812113822302](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812113822302.png)![image-20210812113907385](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812113907385.png)

![image-20210812113924947](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812113924947.png)

手机：![image-20210812114117558](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812114117558.png)![image-20210812114218744](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812114218744.png)![image-20210812114421425](/assets/img/2022-02-01-share-proxy-in-localhost_imgs/image-20210812114421425.png)

可见速度是差不多的，没有因为中间多了一个设备而出现明显降速的状况。

## 总结

大致步骤如下：

1. 电脑上允许局域网连接，并设置好地址和端口
2. 手机上打开网络连接的高级选项，将代理配置到电脑上设置好的地址，保存
3. 连接代理

如果担心电脑上的IP地址发生变化，也可将其设置为静态的。这样，手机上就不需要多次进行配置。