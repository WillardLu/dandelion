tcolorbox宏包可以为我们提供更好看的文本框，这里列出一些应用例子方便以后查询使用。

### 一、环境
- 操作系统：Ubuntu 20.04
- 引擎：XeTeX 3.14159265-2.6-0.999991

### 二、完整示例代码
```latex
% 繁星间漫步，陆巍的博客
\documentclass[oneside, UTF8, fontset = adobe]{ctexart}

% 注意宏包顺序，有可能会报错
\usepackage{geometry}% 用于页面设置
\usepackage[dvipsnames, svgnames, x11names]{xcolor} % 颜色支持
\usepackage[
  colorlinks=true,
  linkcolor=Navy,
  urlcolor=Navy,
  citecolor=Navy,
  anchorcolor=Navy
]{hyperref}
\usepackage{tcolorbox}% 支持更好的文本框
\tcbuselibrary{skins, breakable}% 支持文本框跨页

% 设置为A4纸
\geometry{%
  a4paper,
  left = 19.1mm,
  right = 19.1mm,
  top = 25.4mm,
  bottom = 25.4mm
}

\setlength{\parindent}{2em}% 缩进
\setlength{\parskip}{2ex} % 段间距


\begin{document}

\section{示例一：跨页的文本框}
默认的tcolorbox文本框是不会跨页显示的，在本例中演示如何实现。

\begin{tcolorbox}[enhanced, colback=GhostWhite, colframe=LightGray, coltitle=black, title=测试列表, fonttitle=\bfseries\Large, bottomrule=3ex, breakable=true]
  \setlength{\parindent}{2em}% 缩进
  \setlength{\parskip}{2ex} % 段间距
  
  控制离不开通信。控制论的创立者维纳也对信息论有独到的贡献。维纳从控制和通信的角度进行长期的研究，提出了著名的维纳滤波理论、信号预测的接受理论。他从统计的观点出发，将消息看做可测事件的时间序列，提出了将消息定量化的原则和方法。他把信息作为处理控制和通信系统的基本概念和方法而运用于许多领域，为信息的应用开辟了广阔的前景。
  
  20世纪50年代，信息论迅速向各个学科渗透。1951年，美国无线电工程学会承认了这门新学科。旅美法国物理学家布里渊（L. Brillouin）把信息熵与热力学熵直接联系起来，提出广义熵增原理、信息的负熵原理，把信息论推进到物理学领域，使之有了更大的一般性。
  
  控制论孕育在自动控制、电子技术、无线电通信、神经生理学、生物学、心理学、数理逻辑、计算机技术、统计力学等多种学科的相互渗透中。它的出现，与近代机械制造业的发展、自动机的研制、科学思想的变革相联系，特别还受到第二次世界大战需求的直接推动。
  
  维纳在1919年开始研究勒贝格积分时己经涉及到控制论的思想。他在研究随机问题时，注意到牛顿以来科学思想和科学方法论的发展趋势，注意到统计和进化的思想正在渗透到科学的各部门之中。在他看来，自动控制系统的特点是要根据周围环境的某些变化来决定和调整自己的运动，这就要突破牛顿力学传统方法的框架。20年代到30年代，他在麻省理工学院期间，接触到许多工程学问题，尤其是与布希（V. Bush）合作写了关于电工计算方法明书，一起研究运算微积问题，这使他作出了用光学方法获得傅立叶换算器的设计，提出了用数字计算机代替模拟计算机的设想，并在1940年提出了数字计算机的五点建议以及实施汁划。后来表明，他的设计思想是先进的、可行的，可惜当时布希认为这是将来考虑的事而未付诸实施。
  
  维纳在1935年8月—1936年6月来华，在清华大学电机系和数学系任教授，他与李郁荣合作共同研究电话理论和改善滤波器的设计问题。他后来写道，1935年的中国之行，是他作为一个数学家和控制论专家的分界线，是创立控制论的起点。
  
  第二次世界大战期间，维纳参加了火炮自动控制的研制工作，这是继研究计算机代替人进行复杂计算以后，又一项用于特殊功能的机械电学系统的研制工作，对于控制论的提出具有决定性意义。他研究了随机过程的预测，滤波理论的自动火炮上的应用，特别是他把火炮自动打飞机的动作与人狩猎的行为作了类比，并发现了负反馈对于控制的重要作用。他与工程师毕格罗（J. Biglow）、神经生理学家罗森勃吕特（A. Rosenblueth，1900—）合作，发现目的性行为可以用反馈来解释，从而突破了生命与非生命的界限，把目的性行为这个生物所特有的概念赋予机器。他们于1943年发表了著名的《行为、目的和目的论》一文，初步阐述了控制论的基本思想。
  
  随后，1943年冬至1944年春，由维纳与冯$\cdot$ 诺意曼（J. L. von Neumann，1903—1957）共同发起召开了多学科专家参加的方法论讨论会。1946年春，在纽约又召开了专门讨论反馈问题的讨论班，并变成了一个经常性讨论班，参加讨论班的人员的范围更加广泛。通过这些讨论班，形成了共同关心的领域——通信和控制，特别是对于信息和反馈给予了重视。维纳总结这些思想，于1948年出版了《控制论》一书，该书的副标题叫做“或关于在机器和生物的通信和控制的科学”，标志了控制论作为一门学科诞生、维纳抓住通信的控制的最本质的东西——信息，从更广意义上来理解信息，从而统一地处理通信和控制问题。反馈在控制论中是一个最基本概念，它对于系统的稳定性、目的性以至学习能力都是至关重要的。
  
  控制论在20世纪50年代得到了大的发展，生物学是取得成功的领域之一，创立了生物控制论。艾什比（W. R. Ashby）的《大脑设计》可以说是这一阶段的代表作，他还提出了超稳定系统概念，特别强调“黑箱方法”。他提出了必要“变异度”定理，加深了人们对于通信和控制共性的认识。
  
  20世纪50年代控制论十分活跃的另一分支是工程控制论，它是在控制论的基本思想的基础上，结合反馈放大器理论和伺服机器理论产生的。钱学森1954年出版的《工程控制论》是这个学科的奠基性著作。50年代的工程控制论以自动调节为基础，主要处理单输入单输出的线性自动调节系统，采用建立在传递函数或频率特性上的动态系统分析和综合方法，成为“经典控制论”。60年代以后由于导弹、航天技术等的需要，控制论逐步发展向多输入多输出的多变量系统发展，使用状态空间方法和微分方法，以计算机作为技术手段，并发展了最优控制理论，形成了“现代控制理论”。70年代以来，控制论向广度发展，目标是大系统和复杂系统的控制；向深度发展，目标是智能控制。
  
  在贝塔朗菲看来，从研制导弹、自动化、计算技术方面，并受维纳著作所推动的控制论方面，也是系统研究的发展途径。虽然控制论的出发点是技术而不是科学更不是生物学，其基本模式是反馈而不是动态系统相互作用，但控制论和一般系统论对于具有目的性行为的组织问题所表现的兴趣是一致的。控制论同样反对如下的机械论观点：宇宙是由无数粒子的偶然活动产生的。两者独立发展起来，但都力求寻找新的途径、新的综合的概念和方法，以研究机体和人构成的巨大整体。
\end{tcolorbox}


\section{示例二}
\begin{tcolorbox}[
  colback=MistyRose,
  coltext=red,
  colframe=LightGray,
  boxrule=0.5mm
  ]
  \begin{verbatim}
  <!-- Not recommended: omits the protocol -->
  <script src="//ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js">
  </script>

  <!-- Not recommended: uses HTTP -->
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.4.0/..."></script>\end{verbatim}
\end{tcolorbox}

\begin{tcolorbox}[
  colback=white,
  coltext=ForestGreen,
  colframe=LightGray,
  boxrule=0.5mm
  ]
  \begin{verbatim}
  <!-- Recommended -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/..."></script>\end{verbatim}
\end{tcolorbox}

\begin{tcolorbox}[
  colback=MistyRose,
  coltext=red,
  colframe=LightGray,
  boxrule=0.5mm
  ]
  \begin{verbatim}
  /* Not recommended: omits the protocol */
  @import '//fonts.googleapis.com/css?family=Open+Sans';

  /* Not recommended: uses HTTP */
  @import 'http://fonts.googleapis.com/css?family=Open+Sans';\end{verbatim}
\end{tcolorbox}

\begin{tcolorbox}[
  colback=white,
  coltext=ForestGreen,
  colframe=LightGray,
  boxrule=0.5mm
  ]
  \begin{verbatim}
  /* Recommended */
  @import 'https://fonts.googleapis.com/css?family=Open+Sans';\end{verbatim}
\end{tcolorbox}

\end{document}
```

### 三、pdf内容
![LaTeX之tcolorbox宏包应用示例效果图](example1.png)

### 四、说明
- 跨页的参数设置是“breakable=true”。
- 本例中把字库设置为adobe字库，这个字库操作系统默认情况下是不带的，需要自己去下载安装。当然，也可以把fontset=adobe设置去掉，以使用系统默认字库，虽然编译能通过，但会有警告提示。
