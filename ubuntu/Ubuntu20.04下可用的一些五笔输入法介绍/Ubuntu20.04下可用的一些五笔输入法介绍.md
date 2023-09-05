## Ubuntu20.04下可用的一些五笔输入法介绍

---

#### 1. 默认提供的五笔输入法
Ubuntu 20.04操作系统默认提供iBus下的极点与海峰五笔输入法，如果要使用fcitx下的五笔输入法，可使用以下命令安装 ：
```shell
sudo apt install fcitx-table-wubi
```
记得修改“区域与语言”->“管理 已安装语言”->“键盘输入法系统”，把默认的IBus修改为fcitx。这个用起来还可以。

#### 2. 百度输入法
官方网址为：[https://srf.baidu.com/site/guanwang_linux/index.html](https://srf.baidu.com/site/guanwang_linux/index.html) 。此输入法使用的键盘输入法系统为fcitx（系统默认是iBus，需要自己修改）。我以前安装使用过几天，感觉上比系统提供的好用，功能也强大。但是，不清楚什么原因，我在安装后时不时的会有系统报错，不过并不影响正常使用。

#### 3. 使用开源的iWubi
此输入法在Ubuntu 20.04下需要自己编译源代码，源代码地址为：[https://github.com/Honghe/iwubi](https://github.com/Honghe/iwubi) ，上面有详细的编译安装方法，非常简单。安装好后，添加方法与添加默认的输入法方式一样。此输入法使用的键盘输入法系统为iBus。使用体验上也比系统提供的两种五笔输入法好。但这个输入法我没有发现词频调整的设置，字词出现的排列顺序一直不变，这对于大量输入文字时并不方便。

#### 4. 搜狗输入法
下载地址：[https://pinyin.sogou.com/linux/?r=pinyin](https://pinyin.sogou.com/linux/?r=pinyin)。搜狗输入法使用的键盘输入法系统是 fcitx，支持拼音与五笔，默认情况下是拼音输入，自己修改设置即可切换为五笔。此输入法很好用。我在使用搜狗输入法时，目前只发现在某些情况下会出现重复打印词组的问题，例如：输入“后面”（rgdm），这里如果不跟着打空格而是再打“的”（r）。也就是连打“rgdmr”后，再按空格，输出结果就是“后面后面的”。类似这样的句型（如：你们的、变量中……）都会出现重复打印，注意点就是了。

#### 5. 五笔加加
下载地址：[https://github.com/yanzilisan183/ibus-wbjj](https://github.com/yanzilisan183/ibus-wbjj)。下载后，进入目录，给其中的文件install.sh可执行权限，然后运行即可。此输入法使用的键盘输入法系统为iBus，使用体验也不错。可惜所带词库比较老，许多新词组打不出来。

#### 6. 极点五笔
下载地址：[http://www.freewb.org/](http://www.freewb.org/)，看主页右边的“Linux版极点”[http://210.22.22.150:1278/freewb_0.1.3_amd64.deb](http://210.22.22.150:1278/freewb_0.1.3_amd64.deb)。Ubuntu 20.04自带的五笔输入法就有极点五笔输入，只不过从极点官网下载的更新，并且键盘输入法系统也变成了fcitx。使用体验很好。虽然字库比较老，但会自动造词，使用时间长了自然就好。