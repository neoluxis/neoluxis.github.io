---
layout: article
author: Neolux Lee
title: WinXray以及获取3000+服务节点
date: 2022-02-01
tags: 翻墙 Xray
---
# WinXray以及获取3000+服务节点

## 唠唠闲嗑

前一段时间写过一个使用v2ray和Clash进行科学上网的博客，但是毕竟那样的方法还是有**大大地**不足：节点少；速度慢。所以今天就来介绍一款新的科学上网软件——WinXray。

先来看看WinXray界面：![image-20210810222015357](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210810222015357.png)



这个是我自己做过手脚的，但仍可以看出和以前的VRay界面相似。也是全局模式，PAC模式，但这款软件多了两项功能：自动测速和自动切换更好的服务器

在工具一栏中，还多出了几项小工具![image-20210810221741916](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210810221741916.png)

看到这里是不是饥渴难耐了![image](https://img2020.cnblogs.com/blog/2493192/202108/2493192-20210811104208852-1319363934.png)![image](https://img2020.cnblogs.com/blog/2493192/202108/2493192-20210811104208852-1319363934.png)![image](https://img2020.cnblogs.com/blog/2493192/202108/2493192-20210811104208852-1319363934.png)

下面我们就来详细认识一下这款软件吧。

## WinXray源码下载及编译

WinXray在GitHub有源码和编译好的发行版

[点此下载源码](https://github.com/miduo2689/winXray)

[点此下载发行版](https://github.com/TheMRLL/winxray)

发行版十分小巧，下载解压即可使用。这里主要讲讲编译源码。

**软件源码已放弃版权贡献到公共域** ，源码可使用 [aardio](http://www.aardio.com/) 编译生成单文件绿色EXE，**[点这里下载](https://github.com/miduo2689/winXray/raw/master/release/winXray.7z)** （ [64位版本](https://github.com/miduo2689/winXray/raw/master/release/winXray.7z) / [32位版本](https://github.com/miduo2689/winXray/raw/master/release/winXray32.7z) ），解压即可直接使用( 体积很小仅 **[6.1 MB](https://github.com/miduo2689/winXray/raw/master/release/winXray.7z)** - 已自带 V-Two-Ray Core ）。

下面是用aardio做的演示：

下载源码解压：![image-20210810222727959](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210810222727959.png)

点击进入文件夹，找到default文件使用aardio打开：![image-20210810222813545](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210810222813545.png)

![image-20210810222900747](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210810222900747.png)

如果对这方面有了解，可以自己修改，在这里先不说我修改的方案，咱们直接编译。点击上方“发布”![image-20210810223019435](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210810223019435.png)

会弹出一个黑色窗口![image-20210810223054035](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210810223054035.png)

按照提示输入’y‘，回车，就会生成一个压缩包，之后会在弹出一个窗口，![image-20210810223232280](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210810223232280.png)这个窗口不用管他，关闭即可。当然你也可以点击按钮进行操作。

现在就可以关闭aardio了。编译好的压缩包会在**源码**（不要到aardio目录下找）目录下的release文件夹中，而可以直接运行的版本在源码目录下的WinXray文件夹中。

还可以制作单文件版，但是这里先不展开了。

## 获取服务节点

当然这款软件是支持我们前面提到的狗子云服务器的，可以导入狗子云订阅，也可以直接导入服务器。

我们还可以用其他方法获取更多服务器节点，下面就介绍一种方法。

### 使用爬虫获取服务器

我使用的是一个国外Youtuber制作的网站。如果有需要的，可以给我发邮件，我会将这个网站分享给你，这里暂时不方便透露。

这是这个youtuber的网站，国内是无法访问的![image-20210811081415019](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210811081415019.png)

如果你从国内进入，会提示你下图：![image-20210811081608188](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210811081608188.png)



节点列表如图：![image-20210811080504501](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210811080504501.png)

可以看到有很多节点，但是要注意，这里面也是有相当一部分不可用。而且这里的节点数量较多，一次不能完全导入WinXray。可这里的节点进行筛选：

> 参数列表：
>
> 	c -- 国家地区：如美国=US，日本=JP，香港=HK，台湾=TW，新加坡=SG，加拿大=CA，英国=GB，澳大利亚=AU，德国=DE，法国=FR，瑞士=CH，荷兰=NL，印度=ID，
> 								
> 	type -- 协议名：可选ss,ssr,vmess,trojan
> 								
> 	speed -- 速度：speed=10,30 ----筛选速度在10到30之间的节点      按速度筛选不常用，常用国家和协议配合筛选。

如：我要筛选日本、台湾、香港的服务器，协议要Trojan和Vmess，我可以在网址后面加入

```
?c=JP,TW,HG&type=vmess,trojan
```

![image-20210811083934217](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210811083934217.png)

可以发现，节点少了很多。这些都是按照条件筛选出来的节点。

全选复制![image-20210811084137681](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210811084137681.png)

在WinXray中右键>>>剪贴板导入即可。之后会自动测速，待测速完成后可以进行排序。![1628642620812](/assets/img/2022-02-01-use-winxray-proxy_imgs/1628642620812.gif)

之后我们打开YouTube，找到一个4K视频看看访问状况

![1628645482078_1](/assets/img/2022-02-01-use-winxray-proxy_imgs/1628649195938.gif)

(最后不小心有个谷歌广告啊哈哈![image](https://img2020.cnblogs.com/blog/2493192/202108/2493192-20210811104026706-1595259466.png))此时的统计信息是40,000多KBPS

![image-20210811085253894](/assets/img/2022-02-01-use-winxray-proxy_imgs/image-20210811085253894.png)

最高时可以达到90,000KBPS



更多使用小技巧还可以自己逐渐摸索。

这便是WinXray使用的简单概述，感谢阅读。

## 辅助网址

辅助筛选网站(简陋)：[Proxy Choose ](http://plaza.neolux.ml/ProxySelector/) （这个网站电脑还可，手机的CSS没设置好😁我会抽空完善的）



<!-- 全部节点列表：[点击转到](https://proxy.yugogo.xyz/clash/proxies)（不需代理）-->



