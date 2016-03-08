# KivyMD

[Kivy](https://kivy.org/#home)是一个基于python的跨平台应用开发框架。它同时支持Linux, Windows, OS X, Android和iOS，并且能够识别大部分的操作。
而[kivyMD](https://gitlab.com/kivymd/KivyMD)则是一个基于kivy的一个扩展包，它的目的是提供一个类似于Google Material Design的一套控件，这样，使用者就可以方便的将android上的Material Design效果移植到其他的平台上去。

## 安装

首先，本次安装过程要求全程翻墙，否则无法下载对应的控件。

那么第一步，是kivy的安装，可以参照https://kivy.org/#download，根据自己的平台去做相应的操作。这里以mac下python3.5为例：

- 首先下载mac下python3对应的安装包
- 下载完成后，解压缩文件，可以得到Kivy2.app
- 执行命令`sudo mv Kivy2.app /Applications/Kivy.app`添加到应用列表中去
- 添加链接命令到/usr/local/bin下`ln -s /Applications/Kivy.app/Contents/Resources/script /usr/local/bin/kivy`（此时可使用命令`kivy -V`来查看版本，请务必保证和当前python版本一致）
-  安装KivyMD的一个依赖module`kivy -m pip install kiva-garden`（如果安装不成功，可以尝试直接`pip install kivy-garden`）
- 安装garden这个module的一个子module`garden install recycle view`.
再次提醒，以上步骤必须翻墙，否则无法安装成功。

安装完成后，从gitlab上把KivyMD clone下来：`git clone https://gitlab.com/kivymd/KivyMD.git`，然后执行`kivy setup.py install`就可以完成KivyMD的安装了。

最后测试：`kivy kitchen_sink.py`就能够看到demo界面了。

![Alt text](images/1.png)
![Alt text](images/2.png)

### 坑
- 如果执行`kivy kitchen_sink.py`出现`No module named 'theming'`，应该属于兼容性上的问题。解决方法：对与python3来说，需要手动把kivymd中对应的py控件中的`from theming import ThemableBehavior`修改成`from kivymd.theming import ThemableBehavior`，`from elevationbehavior import ElevationBehavior`修改成`from kivymd.elevationbehavior import ElevationBehavior`。需要修改的文件包括`dialog.py`、`textfields.py`、`spinner.py`、`slidingpanel.py`等（具体根据执行`kivy kitchen_sink.py`的错误提示进行判断）。全部修改完后，再次执行`kivy setup.py install`即可。
- 修改完以上问题后，可能还会出现` KeyError: 'kivy.garden.recycleview'`，这可能是由于garden本身存在的bug，导致recycleview没有被装到需要的位置。解决方法：打开命令行，输入`ivy`进入python命令行。执行语句`import sys`，然后`print(sys.path)`，在结果中，找到以ivy结尾的路径，在mac中为`/Applications/Kivy.app/Contents/Resources/kivy/`，然后进入该目录下的`kivy/garden`，执行`git clone https://github.com/kivy-garden/garden.recycleview.git`。然后执行`mv garden.recycleview recycle view`即可。如果还出现上述问题，说明进入的路径有误，请从`sys.path`找到其他可能的路径。
