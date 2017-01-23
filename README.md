[TOC]



# yeyuPythonChannels

## Android多渠道打包，python自动化



### 使用步骤（前提：安装apktool）

+ 打一个release apk包
+ 新建一个channel.txt文件，将需要的渠道以每行形式存储
+ Android studio中的local.properties文件，签名文件信息
+ 将channel_apk.py、apk包、channel.txt、local.properties放在同一文件夹下
+ 运行python文件（cd到该目录，运行命令python channel_apk.py）




> ### channel.txt样式

> ![](https://github.com/tuyc/tuyc.github.io/blob/master/images/other/WechatIMG4.jpeg?raw=true)

> ### local.properties样式

> ![](https://github.com/tuyc/tuyc.github.io/blob/master/images/other/WechatIMG3.jpeg?raw=true)


> ### 多渠道apk文件位置

> 当前文件中的signed目录中










<br /> 
<br /> <br /> <br /> 

------

## 安装apktool

官网https://ibotpeaches.github.io/Apktool/install/

- ### MAC

  1. 下载apktool脚本

     ```java
     cd 下载文件存放的目录
     curl https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool > apktool
     ```

  2. 下载apktool-2，并保存为apktool.jar

     ```java
     curl https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.2.1.jar > apktool.jar
     ```

  3. 将前面下载的apktool.jar和apktool文件移动到/usr/local/bin

     ```java
     sudo mv apktool /usr/local/bin
     sudo mv apktool.jar /usr/local/bin
     ```

  4. 确保两个文件时可执行的

     ```java
     cd /usr/local/bin
     chmod +x apktool
     chmod +x apktool.jar
     ```

  5. run apktool脚本

     ```java
     bash apktool
     ```



- ### Linux

  1. 下载apktool脚本

     ```ja
     cd 下载文件存放的目录
     wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool
     ```

  2. 下载apktool-2，并保存为apktool.jar

     ```java
     wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.2.1.jar
     ```

  3. Make sure you have the 32bit libraries (`ia32-libs`) downloaded and installed by your linux package manager, if you are on a 64bit unix system.

  4. 将下载的apktool_xxx.jar重命名为apktool.jar

     ```java
     mv apktool_2.2.1.jar apktool.jar
     ```

  5. 将前面下载的apktool.jar和apktool文件移动到/usr/local/bin

     ```java
     sudo mv apktool /usr/local/bin
     sudo mv apktool.jar /usr/local/bin
     ```

  6. 确保两个文件时可执行的

     ```java
     cd /usr/local/bin
     chmod +x apktool
     chmod +x apktool.jar
     ```

  7. run apktool脚本

     ```java
     bash apktool
     ```