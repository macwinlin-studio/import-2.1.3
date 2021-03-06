<div align="center">
  <img src="https://s1.imagehub.cc/images/2022/01/29/icon.png" width="80px" height="80px">
  <h1 align="center">import</h1>
  
  [English](https://github.com/macwinlin-studio/import-2.1.3/blob/2.1.3/README.md) | 简体中文 | [繁體中文](https://github.com/macwinlin-studio/import-2.1.3/blob/2.1.3/README-tc.md)
  
  <a href="https://github.com/macwinlin-studio/import-2.1.3/releases">
    <img src="https://img.shields.io/badge/release-2.1.3-blue" alt="">
  </a>
  <a href="https://github.com/macwinlin-studio/import-2.1.3/blob/2.1.3/LICENSE">
    <img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="">
  </a>
  <a href="https://github.com/macwinlin-studio/import-2.1.3/releases">
    <img src="https://img.shields.io/github/downloads/macwinlin-studio/import-2.1.3/total?color=red" alt="">
  </a>
  <a href="https://www.microsoft.com/zh-cn/windows">
    <img src="https://img.shields.io/badge/platform-windows-orange">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-v3.9-orange">
  </a>
</div>

这是import的README的中文版。

此项目使您能够快速创建新项目。该项目已停止更新，并且基于wxPython包。

## 背景

~~作者总是有一些奇奇怪怪的想法。~~ 作者想制作一个快速建造项目的程序，于是作者制造了这个名为import的项目。

之前作者计划让您们直接修改代码来更改默认路径的。

但后来仔细想想，貌似有点太不方便了。

于是又使用**SQLite3包**+**SQL命令**+**数据库**存储/修改默认路径。

随后创建了`Change config.py`文件。

您现在可以使用`Change config.py`程序直接修改默认路径。

## 安装

此项目可以直接运行，但此项目需要安装一些必要的模块。 您在项目保存位置可以使用此代码：`pip install wxPython`

然后打开Python并运行它。

使用EXE版可忽略以上步骤。

## 使用

目前已实现以下功能：

- 新建
- 剪切
- 复制
- 重命名
- 删除
- 安装签名
- 卸载签名
- 更改配置

此项目可直接运行，作者以后将会制作应用程序版。 此项目需要安装一些必要的模块。
代码在上面。

## 维护

现在我是唯一一个维护这个项目的人。
将来可能会有更多的人加入。

(来自bilibili-query-information)

## 更新日志

### V1.0

- 添加了基础功能(新建+剪切+复制+重命名+删除)
- 绘制了图标

### V1.5

- 添加了GUI界面
- 添加了`sign.sign`文件(同时添加安装签名+卸载签名)
- 重新绘制了图标

### V2.0

- 使用数据库存储默认路径
- 添加`Change config.py`程序
- 将其他功能(安装签名、卸载签名除外)改为使用数据库路径
### V2.1

- 重写了选择语言代码(将Listbox更改为RadioButton)

#### V2.1效果展示

更新前：

![2 1_effect_display_1](https://user-images.githubusercontent.com/82391092/142764548-cda808a6-a36c-4f98-9c96-07d6045f28c5.png)

更新后：

![2 1_effect_display_2](https://user-images.githubusercontent.com/82391092/142764555-f6b0f9a5-04c3-446b-9245-d254e8f5d8df.png)

### V2.1.1

- 将文件从py文件改为pyw文件

### V2.1.2

- 添加了新建pyw文件及其他适配pyw文件的功能

### V2.1.3

- 修复了Uninstall Sign的漏洞

<details>
  <summary>详情</summary>
  不知为何，Python OS库的popen不起作用了，我迫于无奈更改了方法。popen方法被换成remove方法了。
  Delete Code不受影响。它使用unlink方法。
  为popen默哀0.01毫秒，下周它可能就会被我忘了。。。
</details>

## 许可证

该项目使用Apache 2.0许可证。



