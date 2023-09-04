## 在LaTeX的几何图形内嵌入图片

---

本文简单介绍在LaTeX中如何在几何图形内嵌入图片。

### 1、环境
* 操作系统：Ubuntu 22.04
* 编译方式：XeLaTeX

### 2、完整示例代码
```latex
% 繁星间漫步，陆巍的博客
\documentclass{ctexart}

\usepackage{graphics}% 图形支持
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, positioning}


% ------------------ 开始 -------------------

\begin{document}
  \begin{tikzpicture}
    \node[
      circle,
      minimum size = 100mm,
      path picture = {
        \node at (path picture bounding box.center)
        {\includegraphics[width = 280mm]{images/cover2.png}};
      }
    ] {};
  \end{tikzpicture}
  
  \begin{tikzpicture}
    \node[
      isosceles triangle,
      isosceles triangle stretches,
      minimum size = 90mm,
      path picture = {
        \node at (path picture bounding box.center)
        {\includegraphics[height = 100mm]{images/cover1.png}};
      }
    ] {};
  \end{tikzpicture}

\end{document}
```

### 3、效果
![在LaTeX的几何图形内嵌入图片](example1.png)

### 4、说明
* 代码比较短，一看就基本明白，就不再赘述。
* 示例中之所以把两幅图用两个单独的 tikzpicture 环境编写，是因为使用一个 tikzpicture 环境时，第二幅图形中的图片位置会受到前面的影响，跑到很靠下的位置，而无法正常在第二幅的三角形图形中显示。这个问题我暂时还没有去寻找更好的解决办法，暂且如此吧。