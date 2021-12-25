# coding=utf-8
import wx
from os import remove
from os.path import isfile,isdir
from shutil import copyfile
from function import read,jd
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='Cut code',size=(300,315))
        panel = wx.Panel(parent=self)
        icon = wx.Icon('icon.ico',wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        self.suffix = '.py'
        self.sc = wx.StaticText(panel,label='Language:')
        self.radio1 = wx.RadioButton(panel,id=1,label='Python',style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(panel,id=2,label='JavaScript')
        self.radio3 = wx.RadioButton(panel,id=3,label='HTML5')
        self.radio4 = wx.RadioButton(panel,id=4,label='JAVA')
        self.radio5 = wx.RadioButton(panel,id=5,label='C')
        self.radio6 = wx.RadioButton(panel,id=6,label='C++')
        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio_click, id=1,id2=6)
        self.pathsc = wx.StaticText(panel,label='Path:(File name not included)')
        self.path = wx.TextCtrl(panel)
        self.path.SetValue(read(0))
        self.path2sc = wx.StaticText(panel,label='Cut Path:(File name not included)')
        self.path2 = wx.TextCtrl(panel)
        self.path3sc = wx.StaticText(panel,label='File Name:(Does not include suffix)')
        self.path3 = wx.TextCtrl(panel)
        self.button = wx.Button(panel,label='Cut',pos=(100,50))
        self.Bind(wx.EVT_BUTTON,self.on_click,self.button)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.sc,flag=wx.EXPAND,border=10)
        vbox.Add(self.radio1)
        vbox.Add(self.radio2)
        vbox.Add(self.radio3)
        vbox.Add(self.radio4)
        vbox.Add(self.radio5)
        vbox.Add(self.radio6)
        vbox.Add(self.pathsc,flag=wx.EXPAND,border=10)
        vbox.Add(self.path,flag=wx.EXPAND,border=10)
        vbox.Add(self.path2sc,flag=wx.EXPAND,border=10)
        vbox.Add(self.path2,flag=wx.EXPAND,border=10)
        vbox.Add(self.path3sc,flag=wx.EXPAND,border=10)
        vbox.Add(self.path3,flag=wx.EXPAND,border=10)
        vbox.Add(self.button,flag=wx.EXPAND,border=10)
        panel.SetSizer(vbox)
    def on_radio_click(self,event):
        listbox = event.GetEventObject()
        listbox = jd(listbox.GetLabel())
        print(listbox)
        if listbox == 0:
            self.suffix = '.py'
            self.path.SetValue(read(0))
        elif listbox == 1:
            self.suffix = '.js'
            self.path.SetValue(read(1))
        elif listbox == 2:
            self.suffix = '.html'
            self.path.SetValue(read(2))
        elif listbox == 3:
            self.suffix = '.java'
            self.path.SetValue(read(3))
        elif listbox == 4:
            self.suffix = '.c'
            self.path.SetValue(read(4))
        elif listbox == 5:
            self.suffix = '.cpp'
            self.path.SetValue(read(5))
        else:
            self.suffix = 'error'
    def on_click(self,event):
        path = self.path.GetValue()
        path += '\\'
        path += self.path3.GetValue()
        path += self.suffix
        if isfile(path):
            path2 = self.path2.GetValue()
            if isdir(path2):
                path2 += '\\'
                path2 += self.path3.GetValue()
                path2 += self.suffix
                copyfile(path,path2)
                remove(path)
                message = wx.MessageDialog(None,'Cut successfully!','INFORMATION',wx.OK | wx.ICON_INFORMATION)
                if message.ShowModal() == wx.ID_OK:
                    pass
            else:
                message = wx.MessageDialog(None,'Cut path error!','ERROR',wx.OK | wx.ICON_ERROR)
                if message.ShowModal() == wx.ID_OK:
                    pass
        else:
            message = wx.MessageDialog(None,'Original path error!','ERROR',wx.OK | wx.ICON_ERROR)
            if message.ShowModal() == wx.ID_OK:
                pass
app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()