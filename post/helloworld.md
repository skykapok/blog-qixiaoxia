#Hello World

又又又重新开了博客。

事情是这样的，两年前用wordpress搭建了一个[博客](http://old.qixiaoxia.com)，虽然一直没有写，但域名一直在续费，服务器一直在买。又由于wordpress是php+mysql的，我对这二者一窍不通，每次迁移都折腾的要死。后来觉得同事[lvzixun](https://github.com/lvzixun)的方法不错，文章用[markdown](https://help.github.com/articles/markdown-basics/)写，放在github上，然后写个脚本自动拉到服务器上转成html页面。于是我也这么撸了一个。

wordpress的文章可以导出成xml，然后用python解析一下导过来应该很容易。还想把之前所有博客都导过来，网上找到有人写了一个[blogstowordpress](http://www.crifan.com/crifan_released_all/website/python/blogstowordpress/)脚本，试用了一下发现有些博客不成功，比如QQ空间，以后再折腾吧。

##为什么不用Jekyll？
Jekyll是ruby写的，跟php一样都是不懂，我想要一个自己可以完全控制的，想用python。

##为什么是纯静态的？
开始想做动态的，去了解了一下python的web开发，才知道要用[框架](https://wiki.python.org/moin/WebFrameworks)，而看起来python的部署比php更复杂（我就是怕迁移麻烦才放弃wordpress的）。于是还是先搭一个静态站点，目前也足够用了，后面有精力再改。

##为什么不能评论？
静态站也可以使用第三方的评论系统。看了下[多说](http://duoshuo.com/)和[Disqus](https://disqus.com/)，准备用多说，因为有分享到国内SNS的功能，另外就是应该有敏感词过滤吧，我不想因为谁的一句评论让网站被墙掉。~~这篇文章目前还不能评论，近期会加上。~~

##为什么这么丑？
你才丑。

---
14.12.03更新：增加了评论框。

---
17.03.23更新：多说要关闭服务，评论框换成Disqus。

---
17.03.28更新：原来Disqus被墙了，评论区又换成了网易云跟帖。导入多说的数据后头像没了，我的名字也变成了有态度网友 --!