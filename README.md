# TZ-大规模指纹图像检索的模型与实现


## 题目来源：
十二届MathorCup高校数学建模挑战赛A题（企业出题） [网页链接](http://mathorcup.org/detail/2378)

  
## 文件说明  
1.<font color="blue">指纹图像原始数据.zip：</font> 组委会所给原始数据，可以从官网下载 [[点击下载]](http://mathorcup.org/detail/2378)  

2.<font color=blue>data_计算结果.zip：</font> 本程序提供的计算结果，分别在不同穿透率下筛选出的指纹图像ID  

3.<font color=blue>DataRead(2).py：</font> 读取并整理txt格式原始数据的脚本，封装为函数  

4.<font color=blue>03\_同指.jpg / 03\_异指.jpg：</font> 模糊聚类算法下相同指纹和不同指纹的图像差异  

5.<font color=blue>07\_..：</font> 使用支持向量机（SVM）将同指/异指分类，赋予0/1标签，进行特征值提取  

6.<font color=blue>10\_穿透率测试框架.py：</font> 导入本程序算法，对原始数据进行穿透率测试的代码  

7.<font color=blue>exact\_traits.py：</font> 综合提取指纹图像数据特征值的代码，封装为类（<font color=LightSeaGreen>TraitExactor</font>）

8.<font color=blue>输出特征值/..：</font> 程序提取的特征值数据


###<font color=red>欢迎讨论交流</font>： rifn20@163.com
