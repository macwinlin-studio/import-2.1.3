<div align="center">
  <img src="https://s1.imagehub.cc/images/2022/01/29/icon.png" width="80px" height="80px">
  <h1 align="center">import</h1>
  
  English | [简体中文](https://github.com/macwinlin-studio/import-2.1.3/blob/2.1.3/README-zh.md) | [繁體中文](https://github.com/macwinlin-studio/import-2.1.3/blob/2.1.3/README-tc.md)
  
  <a href="https://github.com/macwinlin-studio/import-2.1.3/releases">
    <img src="https://img.shields.io/badge/release-2.1.3-blue" alt="">
  </a>
  <a href="https://github.com/macwinlin-studio/import-2.1.3/blob/2.1.3/LICENSE">
    <img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="">
  </a>
  <a href="https://github.com/macwinlin-studio/import-2.1.3/releases">
    <img src="https://img.shields.io/github/downloads/xinxin2021/import-2.1.3/total" alt="">
  </a>
  <img src="https://img.shields.io/badge/platform-windows-red">
  <img src="https://img.shields.io/badge/python-v3.9-orange">
</div>

This is import's README.

This project enables you to quickly create a new project.That has stopped updating and is based on the wxPython package.

## Background

~~The author always has some strange ideas.~~ The author wanted to make a program to quickly build a project, so the author made this project called import.

Previously, the author planned to let you directly modify the code to change the default path.

But then think about it, it seems a little inconvenient.

Therefore, **SQLite3 package** + **SQL command** + **database** are used to store / modify the default path.

The **Change config.py** file is then created.

You can now directly modify the default path using the **Change config.py** program.

## Install

This project can be run directly,but this project needs to install some necessary modules.

You can use this code in the project save location:pip install wxPython

Then open Python and run it.

The above steps can be ignored when using the exe version.

## Usage

At present, the following functions have been realized:

- Make
- Cut
- Copy
- Rename
- Delete
- Install sign
- Uninstall sign
- Change config

This project can be run directly.

This project needs to install some necessary modules.

The code is on it.

## Maintainers

Now I'm the only one maintainers this project.

More people may join in the future.

(From bilibili-query-information)

## Update Log

### V1.0
- Added basic functions(Make+Cut+Copy+Rename+Delete)
- Icon drawn
### V1.5
- Added GUI interface
- Added sign.sign file(Add installation sign + uninstall sign at the same time)
- Redrawn Icon
### V2.0
- Use database storage default path
- Add **Change config.py** program
- Change other functions (Install and uninstall sign) to use database path
### V2.1
- Rewrite select language code(Change Listbox to RadioButton)
#### V2.1 Effect Display
Before update:

![2 1_effect_display_1](https://user-images.githubusercontent.com/82391092/142764421-3f20e3f2-da2f-432b-b662-3ddefb530c3f.png)

After update:

![2 1_effect_display_2](https://user-images.githubusercontent.com/82391092/142764462-6557cd1e-f771-46db-bfd2-361b049c6c77.png)

### V2.1.1

- Change the file from py file to pyw file

### V2.1.2

- Added the function of creating new pyw files and other adaptive pyw files

### V2.1.3

- Fixed a vulnerability in Uninstall Sign.

<details>
  <summary>Details</summary>
  Somehow,Popen in Python OS Library doesn't work,I was forced to change the function.Popen Function has been replaced with Remove Function.
  Delete code is not affected.It uses the Unlink Function.
</details>

## License

This project uses Apache 2.0 License.
