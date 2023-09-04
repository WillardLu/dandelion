## Ubuntu下Git简单基础操作备忘

---

本文记录有关Git的一些最简单的基础操作，详细内容请参考官网或有关书籍。

#### 1. 安装Git
```shell
sudo apt install git
```

#### 2. 环境设置
```shell
git config --global user.name "name"
git config --global user.email "myname@163.com"
git config --global core.quotepath false
```
其中第三条命令用于解决中文文件名显示问题。

#### 3. 查看配置命令
以下命令分别对应系统、当前用户与当前仓库。
```shell
git config --system --list
git config --global --list
git config --local --list
```

#### 4. 查看参数帮助
```shell
git help <verb>
git <verb> --help
man git-<verb>
```
例如：
```shell
git help config
git config --help
man git-config
```

#### 5. 创建仓库
#### 5.1 对已经存在的文件目录进行初始化
```shell
git init
```
##### 5.2 初始化本地空仓库
下面的命令将在当前目录生成一个.git目录。
```shell
git --bare init
git --bare init <directory>
```
上面的第二条命令将指定目录作为Git仓库。

##### 5.3 克隆仓库
```shell
git clone <repo>
git clone <repo> <direcotry>
```

#### 6. 常用命令
##### 6.1 查看当前状态
```shell
git status
```
##### 6.2 将文件添加到版本库中
```shell
git add <file>
```
文件名可以使用通配符。取消添加的方法在执行以上命令或查看状态命令时会有详细操作提示，这里不再赘述。此命令实际只是暂存，并未正式添加到库中，可以用以下命令正式提交：
```shell
git commit -m "说明"
```
##### 6.3 修改库内的文件或文件夹名称
```shell
git mv <原名称> <新名称>
```
##### 6.4 删除文件或文件夹
```shell
git rm <文件>
git rm -r <文件夹>
```
-r表示递归所有子目录。这里要注意的是，如果目录并未被git跟踪的话，执行此命令时会提示找不到目录的信息，这个时候直接使用rm -r命令删除此文件夹即可。这种情况通常会出现在空目录或者目录里面的文件还未提交时。

##### 6.5 查看日志
```shell
git log
```
#### 7. 创建Git服务
##### 7.1 创建简单本地服务
这里假设在U盘上创建company服务，U盘路径为：/media/starry/origin。步骤如下：
a. 在/media/starry/origin/下执行命令：
```shell
git init --bare company.git
```
b. 在/home/starry/目录下克隆U盘上的仓库，执行命令：
```shell
git clone /media/starry/origin/company.git
```
c. 如果本来就没有内容的话，这时可以直接在生成的company文件夹中操作。如果原来有内容，只须把相应文件夹移动到这个文件夹内。记得添加.gitignore文件，把不需要管理的文件、目录放在里面。
d. 使用git add 与 git commit命令添加文件、提交说明。
e. 使用命令git push origin把新增的内容推送到U盘中。
##### 7.2 设置SSH登录GitCode
使用此方法前，从GitCode克隆项目时，应该选用“通过 SSH Clone 项目”来克隆。虽然用HTTPS方式也可以，但要修改配置文件后才能使用SSH（.git文件夹中的config文件）。

a. 在本地生成密钥
在主目录下执行以下命令：
```shell
ssh-keygen -t rsa
```
执行后显示的提示中不用输入任何内容，一直回车下去，最后生成的密钥在~/.ssh目录下，文件为id\_rsa.pub。

b. 在GitCode上添加SSH密钥
在GitCode上，点击“个人设置”->“SSH密钥”，把前面生成的id_rsa.pub文件中的全部内容粘贴上去（可以用gedit打开，全选->复制），保存即可。