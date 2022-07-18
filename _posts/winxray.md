# WinXray以及获取3000+服务节点

## 唠唠闲嗑

前一段时间写过一个使用v2ray和Clash进行科学上网的博客，但是毕竟那样的方法还是有**大大地**不足：节点少；速度慢。所以今天就来介绍一款新的科学上网软件——WinXray。

先来看看WinXray界面：

![image-1657512500162](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-1657512500162-16577735686071.png)

这个是我自己做过手脚的，但仍可以看出和以前的VRay界面相似。也是全局模式，PAC模式，但这款软件多了两项功能：自动测速和自动切换更好的服务器

![image-1657512514906](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-1657512514906-16577735892333.png)

在工具一栏中，还多出了几项小工具，看到这里是不是饥渴难耐了？下面我们就来详细认识一下这款软件吧。

## WinXray源码下载及编译

WinXray在GitHub有源码和编译好的发行版

[点此下载源码](https://github.com/miduo2689/winXray)

[点此下载发行版](https://github.com/TheMRLL/winxray)

发行版十分小巧，下载解压即可使用。这里主要讲讲编译源码。

**软件源码已放弃版权贡献到公共域** ，源码可使用 [aardio](http://www.aardio.com/) 编译生成单文件绿色EXE，**[点这里下载](https://github.com/miduo2689/winXray/raw/master/release/winXray.7z)** （ [64位版本](https://github.com/miduo2689/winXray/raw/master/release/winXray.7z) / [32位版本](https://github.com/miduo2689/winXray/raw/master/release/winXray32.7z) ），解压即可直接使用( 体积很小仅 **[6.1 MB](https://github.com/miduo2689/winXray/raw/master/release/winXray.7z)** - 已自带 V-Two-Ray Core ）。

下面是用aardio做的演示：  

下载源码解压：

![image-1657512567906](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-1657512567906-16577736028625.png)

点击进入文件夹，找到default文件使用aardio打开：

![image-1657512611859](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-1657512611859-16577736177577.png)

如果对这方面有了解，可以自己修改，在这里 咱们先不修改，直接编译。点击上方“发布”!

![image-1657512623343](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-1657512623343-16577736308679.png)

会弹出一个黑色窗口

![image-1657512673836](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-1657512673836-165777364215311.png)

按照提示输入’y‘，回车，就会生成一个压缩包，之后会在弹出一个窗口，

![image-1657512685479](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-1657512685479-165777364933413-165777421812725.png)

这个窗口不用管他，关闭即可。当然你也可以点击按钮进行操作。

现在就可以关闭aardio了。编译好的压缩包会在**源码**（不要到aardio目录下找）目录下的release文件夹中，而可以直接运行的版本在源码目录下的WinXray文件夹中。

还可以制作单文件版，但是这里先不展开了。

## 获取服务节点

当然这款软件是支持一般的服务器提供商的节点的，可以导入相关的订阅，也可以直接导入服务器。

我们还可以用其他方法获取更多服务器节点，下面就介绍一种方法。

### 使用爬虫获取服务器

我们使用一个在服务器部署的爬虫网站

节点列表如图：

![image-1657512798824](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-1657512798824-165777366202215.png)

可以看到有很多节点，但是要注意，这里面也是有相当一部分不可用。而且这里的节点数量较多，一次不能完全导入WinXray。可这里的节点进行筛选：

> 参数列表：
>
> 	c -- 国家地区：如美国=US，日本=JP，香港=HK，台湾=TW，新加坡=SG，加拿大=CA，英国=GB，澳大利亚=AU，德国=DE，法国=FR，瑞士=CH，荷兰=NL，印度=ID，
> 				
> 	type -- 协议名：可选ss,ssr,vmess,trojan
> 				
> 	speed -- 速度：speed=10,30 ----筛选速度在10到30之间的节点      按速度筛选不常用，常用国家和协议配合筛选。
> 如：我要筛选日本、台湾、香港的服务器，协议要Trojan和Vmess，我可以在网址后面加入

```
?c=JP,TW,HG&type=vmess,trojan
```
回车后发现网页变化：

![image-1657512826182](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-1657512826182-165777367093617.png)

可以发现，节点少了很多。这些都是按照条件筛选出来的节点。

全选复制

![image-1657512876204](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-1657512876204-165777367877519.png)

在WinXray中右键>>>剪贴板导入即可。之后会自动测速，待测速完成后可以进行排序。!

![import proxy](winxray.assets/1628642620812.gif)

之后我们打开YouTube，找到一个4K视频看看访问状况

![test-4k](winxray.assets/1628649195938-165777457444332.gif)

(最后不小心有个谷歌广告啊哈哈)此时的统计信息是40,000多KBPS

![image-20210811085253894](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-20210811085253894-165777369740823.png)

最高时可以达到90,000KBPS

更多使用小技巧还可以自己逐渐摸索。

## 辅助网址

节点筛选网站：（在做了在做了）