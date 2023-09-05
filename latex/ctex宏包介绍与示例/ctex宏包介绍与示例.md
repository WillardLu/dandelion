本文简单介绍ctex宏包，并通过实例来介绍一些常用设置。

*我们知道，软件有不同的版本，LaTeX宏包自然也不例外。通常情况下，默认安装的宏包在版本上会比最新的低一些，所以本文介绍的功能与帮助文件可能与最新版的有差异，如果你已经单独下载最新版本的宏包，请到CTAN（Comprehensive TeX Archive Network，世界上最主要的TeX资源集散网站）上查询最新的帮助文件。*

## 一、简介

### 1. 作用
ctex宏包帮助文件的简介是：CTEX宏集是面向中文排版的通用LATEX排版框架，为中文LATEX文档提供了汉字输出支持、标点压缩、字体字号命令、标题文字汉化、中文版式调整、数字日期转换等支持功能，可适应论文、报告、书籍、幻灯片等不同类型的中文文档。简单的说，ctex就是用来支持汉字排版。

### 2. Ubuntu20.04下默认安装的版本（2022年8月12日）
2019/05/29 v2.4.16∗

ctex宏包帮助文件：[ctex.pdf](https://code.gitlink.org.cn/api/v1/repos/youling/latex-help-doc/raw/C/ctex.pdf?ref=master&access_token=504b568599ab24fcbd59a6296b0c2f87a835a98a)

### 3. CTAN已公布的最新版本
2022/07/14 v2.5.10∗

ctex宏包帮助文件：[ctex.pdf](https://mirrors.ustc.edu.cn/CTAN/language/chinese/ctex/ctex.pdf)

### 4. 开发者网站
[http://www.ctex.org/](http://www.ctex.org/HomePage)

## 二、实例

### 1. 实例一

#### 1）验证环境
- 操作系统：Ubuntu 20.04
- 引擎：XeTeX 3.14159265-2.6-0.999991
- CTeX 2019/05/29 v2.4.16∗

#### 2）源码
```latex
% 繁星间漫步，陆巍的博客
% 这里只考虑电子书形式，所以选择了oneside。
% UTF8指源文件使用UTF8编码保存。
% fontset=adobe意为设置adobe提供的中文字库
\documentclass[oneside, UTF8, fontset = adobe]{ctexbook}

\usepackage{geometry}% 用于页面设置
\usepackage[dvipsnames, svgnames, x11names]{xcolor}% 颜色支持
\usepackage{graphicx}% 图形支持
% 支持超链接，加载此宏包后，目录才可点击跳转。
\usepackage[
  colorlinks=true,
  linkcolor=Navy,
  urlcolor=Navy,
  citecolor=Navy,
  anchorcolor=Navy
]{hyperref}

% 设置纸张与边距
% 这里只考虑电子书形式，所以页边距都设为1英寸。如果要打印出来，应根据相关规定或实际需要进行调整。
\geometry{
  a4paper,
  left = 1in,
  right = 1in,
  top = 1in,
  bottom = 1in
}

% 设置章节标题左对齐，+=表示在原有格式上追加，如果只有=则表示完全替换
\ctexset{
  chapter/format += \raggedright,
  section/format += \raggedright,
  subsection/format += \raggedright,
  subsubsection/format += \raggedright,
}

\setlength{\parindent}{2em}% 缩进
\setlength{\parskip}{2ex} % 段间距

% 用来控制编译时只包含哪些部分，当调试内容很多的文档时，可以节省时间。
% \includeonly{}


% ------------------ 开始 -------------------
\begin{document}

\begin{titlepage}
  \quad

  \vspace{.15\textheight}
  \begin{center}
    \includegraphics[width = .2\textwidth]{images/cover.png}

    \huge\textbf{CTeX宏包应用示例一}
    \vfill
    \normalsize 2022年8月12日
  \end{center}  
\end{titlepage}


% ------------------ 前言 -------------------
\frontmatter% 关闭前言部分的章节序号，页码使用罗马数字

\chapter{前言}
CTeX宏包应用示例。


% ------------------ 目录 -------------------
\tableofcontents% 生成目录


% ------------------ 正文 -------------------
\mainmatter

% 载入tex文档
%\include{}


\chapter{现代诗}

\section{胡适}

\large\textbf{梦与诗}\normalsize

\vspace{2ex}\itshape
都是平常经验

都是平常影象

偶然涌到梦中来

变幻出多少新奇花样

\vspace{2ex}
都是平常情感

都是平常言语

偶然碰着个诗人

变幻出多少新奇诗句

\vspace{2ex}
醉过才知酒浓

爱过才知情重

你不能做我的诗

正如我不能做你的梦

\end{document}
```

#### 3）生成的pdf文件内容
![ctex宏包介绍实例一pdf内容](example1.png)

#### 4）说明
- 先看第一行命令：\documentclass[oneside, UTF8, fontset = adobe]{ctexbook}，其中的ctexbook是ctex宏包提供的汉字文档类。ctex宏包提供了四个汉字文档类：ctexart、ctexrep、ctexbook和ctexbeamer，分别对应LaTeX标准文档类article、report、book和beamer。在使用中，我们会发现各种文档类对命令的支持不一样。因为使用汉字，所以这里加入UTF8选项，让源文件使用UTF-8编码保存。
- ctex中可以设置六种汉字字库，我使用后目前表现最好的是adobe提供的汉字字库。Ubuntu系统默认提供的和方正免费提供的字体都存在问题，虽然二者都能通过编译，但总是冒出一些警告信息，目前在安装adobe公司提供的字体后（[adobe字体](https://github.com/shanyouli/Adobe-chinese-fonts)），能通过编译，并且没有警告信息。是不是有点遗憾？
- \ctexset命令用于控制ctex宏包的各项功能。一般不需要改动什么设置，只是我不喜欢默认章节标题居中排列，所以在这里改为左对齐。要注意的是，如无特殊需要，请使用“+=”来修改设置，+=表示在原有格式上追加。如果只用等号（=）则表示完全替换，这样就需要做完整设置，比较麻烦。
- 如果使用的文档类是ctexart，\frontmatter、\mainmatter、\chapter等命令不能使用，就连前面\ctexset设置中也不能有\chapter出现。
- 代码中我使用\vspace命令来控制间距，并没有使用\\\\换行来控制。虽然用\\\\后有效果，但会出现警告信息（Underfull \hbox）。现在这个例子的代码在使用XeLaTeX引擎编译后，无错误、无警告。