Weblog 统计系统
---
## 程序文件结构
+ Weblog
    + weblog.py --> 程序运行文件
    + weblog_data.txt --> 数据存储文件
    + README.MD
---
## 程序实现功能
+ 寻求用户输入并根据用户输入的文件名进行计算解析
+ 计算并显示日志所含的总有效uv及pv数
+ 计算并显示访问的设备名称及其相应的访问量
+ 计算并筛选top 10访问量的URL并按照访问量的大小进行排序显示
+ 计算并筛选top 10访问量的IP地址并按照访问量的大小进行排序显示
+ 计算并按照pv数的高低显示每小时pv数
+ 计算并根据时间(从00-23),显示每小时的uv数
---
## 程序的启动方式
+ 通过终端或python解释器启动weblog.py文件
---
## 登陆用户信息
+ 直接启动无需登陆
---
## 程序运行效果
+ 用户输入及总pv,uv数显示
![uv，pv总](https://i.loli.net/2020/04/23/FNctVDukUJXKQqv.jpg)
+ 设备及其访问量显示
![设备访问量](https://i.loli.net/2020/04/23/zd7rNCW9uL285MR.jpg)
+ top 10访问量的页面及其访问量
![top 10访问量页面](https://i.loli.net/2020/04/23/EMl4bvcZg8f71nx.jpg)
+ top 10uv的IP地址 
![top 10uv的IP地址](https://i.loli.net/2020/04/23/Xd7ijRzIaT3YGFH.jpg)
+ 每小时pv数
![每小时的pv数](https://i.loli.net/2020/04/23/MUqOPrpcFD63WEy.jpg)
+ 每小时uv数
![每小时的uv数](https://i.loli.net/2020/04/23/CejIt4BGxKSUD3s.jpg)
---
## 程序运行流程图
+ flowchart

![flowchart](https://i.loli.net/2020/04/23/nMg8lSGjz9FoiNV.png)