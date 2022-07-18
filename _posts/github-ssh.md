# Git 配置SSH key

git ssh密钥创建和重置
许多人都用过git的https直接拉取代码，今天来操作下ssh的形式拉取代码

安装了Git后，右键打开Git bash（或者其他的终端）

## 1. 查看是否配置过密钥

```bash
cd ~/.ssh
```
![img](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/14253829-518b2b068220110d.png)

如图，没有ssh就创建。如果已经有ssh key，可以覆盖创建或直接跳转到第三步

## 2. 进行创建ssh

```bash
ssh-keygen -t rsa -C 'youremail@qq.com'
```
之后不断<kbd>enter</kbd>即可

![img](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/14253829-2be933f5d7eaa774.png)

## 3. 查看生成的公钥

```bash
cat ~/.ssh/id_rsa.pub
```

回车后看到终端输入这样的结果

![img](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/14253829-fd3255a979b98650.png)

也可以在C盘打开

![img](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/14253829-65d238c46a22f2f1.png)

## 4. 登入GitHub

在账户设置里找到`SSH and GPG keys`

![image-20220714095703463](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-20220714095703463.png)

点击`新建SSH key`

![image-20220714095847081](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-20220714095847081.png)

如图

![image-20220714095950462](https://testingcf.jsdelivr.net/gh/neoluxis/image/img/image-20220714095950462.png)

title一行填写自定义的名称，Key一栏填写~/.ssh/id_rsa.pub文件里面的内容

完成后点击添加SSH key

## 5. 测试SSH key是否正常工作

使用下列命令

```bash
$ ssh -T git@github.com
// 使用gitee的同学改成这个命令
$ ssh -T gitee@gitee.com
```

之后会问你
 Are you sure you want to continue connecting (yes/no)?
 只要回答yes，回车就会看到下面的
 Hi Anonymous! You've successfully authenticated, but GITEE.COM does not provide shell access.
 就表示你的设置已经成功了。

## 6. 接下来就可以开始直接克隆你的代码下来
复制你代码库的ssh

执行

```bash
git clone git@github.com:username/repository-name.git
```



到这里就结束了