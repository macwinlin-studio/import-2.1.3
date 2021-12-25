# coding=utf-8
import wx,os
from function import read,pd,jd
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='Rename code',size=(300,270))
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
        self.Bind(wx.EVT_RADIOBUTTON,self.on_radio_click,id=1,id2=6)
        self.pathsc = wx.StaticText(panel,label='Path:(Including the original file name and suffix)')
        self.path = wx.TextCtrl(panel)
        if pd(0):
            self.path.SetValue(read(0) + '\\[file name].py')
        else:
            self.path.SetValue(read(0) + '[file name].py')
        self.namesc = wx.StaticText(panel,label='New Name:(Extension not included)')
        self.name = wx.TextCtrl(panel)
        self.button = wx.Button(panel,label='Rename',pos=(100,50))
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
        vbox.Add(self.namesc,flag=wx.EXPAND,border=10)
        vbox.Add(self.name,flag=wx.EXPAND,border=10)
        vbox.Add(self.button,flag=wx.EXPAND,border=10)
        panel.SetSizer(vbox)
    def on_radio_click(self,event):
        listbox = event.GetEventObject()
        listbox = jd(listbox.GetLabel())
        if listbox == 0:
            self.suffix = '.py'
            if pd(0):
                self.path.SetValue(read(0) + '\\[file name].py')
            else:
                self.path.SetValue(read(0) + '[file name].py')
        elif listbox == 1:
            self.suffix = '.js'
            if pd(1):
                self.path.SetValue(read(1) + '\\[file name].js')
            else:
                self.path.SetValue(read(1) + '[file name].js')
        elif listbox == 2:
            self.suffix = '.html'
            if pd(2):
                self.path.SetValue(read(2) + '\\[file name].html')
            else:
                self.path.SetValue(read(2) + '[file name].html')
        elif listbox == 3:
            self.suffix = '.java'
            if pd(3):
                self.path.SetValue(read(3) + '\\[file name].java')
            else:
                self.path.SetValue(read(3) + '[file name].java')
        elif listbox == 4:
            self.suffix = '.c'
            if pd(4):
                self.path.SetValue(read(4) + '\\[file name].c')
            else:
                self.path.SetValue(read(4) + '[file name].c')
        elif listbox == 5:
            self.suffix = '.cpp'
            if pd(5):
                self.path.SetValue(read(5) + '\\[file name].cpp')
            else:
                self.path.SetValue(read(5) + '[file name].cpp')
        else:
            self.suffix = 'error'
    def on_click(self,event):
        path = self.path.GetValue()
        if os.path.isfile(path):
            n = -1
            for i in range(len(path)):
                if path[n] == '\\':
                    break
                n -= 1
            ypath = path[0:n]
            ypath += '\\'
            ypath += self.name.GetValue()
            ypath += self.suffix
            os.rename(path,ypath)
            message = wx.MessageDialog(None,'Rename succeeded!','INFORMATION',wx.OK | wx.ICON_INFORMATION)
            if message.ShowModal() == wx.ID_OK:
                pass
        else:
            message = wx.MessageDialog(None,'Wrong path or no file!','ERROR',wx.OK | wx.ICON_ERROR)
            if message.ShowModal() == wx.ID_OK:
                pass
app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()