# yeyuPythonChannels
### Android多渠道打包，python自动化



#### 使用方式（步骤）

+ 打一个release apk包
+ 新建一个channel.txt文件，将需要的渠道以每行形式存储
+ Android studio中的local.properties文件，签名文件信息
+ 将channel_apk.py、apk包、channel.txt、local.properties放在同一文件夹下
+ 运行python文件（cd到该目录，运行命令python channel_apk.py）




#### channel.txt样式

![](https://github.com/tuyc/tuyc.github.io/blob/master/images/other/WechatIMG4.jpeg?raw=true)

#### local.properties样式

![](https://github.com/tuyc/tuyc.github.io/blob/master/images/other/WechatIMG3.jpeg?raw=true)


#### 多渠道apk文件位置

当前文件中的signed目录中