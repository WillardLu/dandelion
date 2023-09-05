## Ubuntu 22.04下安装配置rime五笔输入法

---

我曾介绍过在Ubuntu 20.04下的一些五笔输入法，在把操作系统升级到22.04后，这些五笔输入法大部分都出现了各种各样的问题。因此，我现在改用rime五笔输入法，安装与配置的方法如下。

### 1、安装
```shell
sudo apt install ibus-rime
sudo apt install librime-data-wubi
```
安装后重启系统，在“设置->键盘->输入源”中添加“汉语”，再选择中文（Rime），如下图：
![添加rime输入源](https://img-blog.csdnimg.cn/bdad94d34d354bf3aeee651f1c740aa7.png#pic_center)


### 2、配置
第一步安装好后，默认的输入法是拼音输入法，还需要我们自己设置。打开设置的方法是先把输入法调到“中文(Rime)”下，然后使用热键打开设置，热键有F4键，或者Ctrl+~键（即Ctrl加上波浪符号键）。设置菜单出来后用上下方向键选择后回车。

我们会发现默认的选择菜单中没有五笔输入法，需要修改一下配置表。配置表的位置在“~/.config/ibus/rime/build/”下，名称为default.yaml。找到后用文本编辑器打开，并在“schema_list:”下添加“- schema: wubi86”。见下图：
![在配置表中添加五笔输入法](https://img-blog.csdnimg.cn/62696b17948e4e2d8d378370e317eb3f.png#pic_center)
修改后保存退出。然后，再用前面说的方法打开设置，用**向下的方向键**（这里注意，用鼠标滚轮和点击菜单中向下方向按钮翻页均无效。）向下寻找，就能找到五笔输入法。
![rime五笔输入法设置](https://img-blog.csdnimg.cn/f7f62bf0edfd4e989d418a5b44e6311a.png#pic_center)
选择好回车后立即生效，就可以开始使用了。

---

在设置默认输入法的时候，我们可以看到Rime里面提供了各种各样的输入法，所以想要使用其他输入法的朋友可以用相同的安装配置方法。