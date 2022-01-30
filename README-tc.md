# import

這是import的README的繁體中文版。

[English](https://github.com/macwinlin-studio/import-2.1.3/blob/2.1.3/README.md) | [简体中文](https://github.com/macwinlin-studio/import-2.1.3/blob/2.1.3/README-zh.md) | 繁體中文

此項目使您能夠快速創建新項目。該項目已停止更新，並且基於wxPython包。

## 背景

~~作者總是有一些奇奇怪怪的想法。~~作者想製作一個快速建造項目的程序，於是作者製造了這個名為import的項目。

之前作者計劃讓您們直接修改代碼來更改默認路徑的。

但後來仔細想想，貌似有點太不方便了。

於是又使用**SQLite3包**+**SQL命令**+**數據庫**存儲/修改默認路徑。

隨後創建了**Change config.py**文件。

您現在可以使用**Change config.py**程序直接修改默認路徑。

## 安裝

此項目可以直接運行，但此項目需要安裝一些必要的模塊。 您在項目保存位置可以使用此代碼：pip install wxPython

然後打開Python並運行它。

使用EXE版可忽略以上步驟。

## 使用

目前已實現以下功能：

- 新建
- 剪切
- 複製
- 重命名
- 刪除
- 安裝簽名
- 更改配置

此項目可直接運行，但此項目需要安裝一些必要的模塊。
代碼在上面。

## 維護

現在我是唯一一個維護這個項目的人。
將來可能會有更多的人加入。

(來自bilibili-query-information)

## 更新日誌

### V1.0

- 添加了基礎功能(新建+剪切+複製+重命名+刪除)
- 繪製了圖標

### V1.5

- 添加了GUI界面
- 添加了sign.sign文件(同時添加安裝簽名+卸載簽名)
- 重新繪製了圖標

### V2.0

- 使用數據庫存儲默認路徑
- 添加**Change config.py**程序
- 將其他功能(安裝簽名、寫在簽名除外)改為使用數據庫路徑

### V2.1

- 重寫了選擇語言代碼(將Listbox更改為RadioButton)

#### V2.1效果展示

更新前：

![2 1_effect_display_1](https://user-images.githubusercontent.com/82391092/142764548-cda808a6-a36c-4f98-9c96-07d6045f28c5.png)

更新後：

![2 1_effect_display_2](https://user-images.githubusercontent.com/82391092/142764555-f6b0f9a5-04c3-446b-9245-d254e8f5d8df.png)

### V2.1.1

- 將文件從py文件改為pyw文件

### V2.1.2

- 添加了新建pyw文件及其他適配pyw文件的功能

### 2.1.3

- 修復了Uninstall Sign的漏洞

<details>
  <summary>詳情</summary>
  不知為何，Python OS庫的popen不起作用了，我迫於無奈更改了方法。popen方法被換成remove方法了。
  Delete Code不受影響。它使用unlink方法。
  為popen默哀0.01毫秒，下週它可能就會被我忘了。。。
</details>

## 許可證

該項目使用Apache 2.0許可證。
