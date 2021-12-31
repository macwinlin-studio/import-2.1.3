# coding=utf-8
import wx,os
from function import read,jd
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='Delete code',size=(300,270))
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
        self.Bind(wx.EVT_RADIOBUTTON,self.on_radio_click,id=1,id2=7)
        self.pathsc = wx.StaticText(panel,label='Path:(Including the original file name and suffix)')
        self.path = wx.TextCtrl(panel)
        self.path.SetValue(read(0))
        self.namesc = wx.StaticText(panel,label='File Name:(Does not include suffix)')
        self.name = wx.TextCtrl(panel)
        self.name.SetValue('New project')
        self.button = wx.Button(panel,label='Delete',pos=(100,50))
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
        elif listbox == 6:
            self.suffix = '.pyw'
            self.path.SetValue(read(6))
        else:
            self.suffix = 'error'
    def on_click(self,event):
        path = self.path.GetValue()
        if os.path.isdir(path):
            file = os.listdir(path)
            name = self.name.GetValue()
            name += self.suffix
            if name in file:
                message = wx.MessageDialog(None,'Are you sure you want to delete?','QUESTION',wx.YES_NO | wx.ICON_QUESTION)
                if message.ShowModal() == wx.ID_YES:
                    path += '\\'
                    path += name
                    os.unlink(path)
                    message = wx.MessageDialog(None,'Delete successfully!','INFORMATION',wx.OK | wx.ICON_INFORMATION)
                    if message.ShowModal() == wx.ID_OK:
                        pass
            else:
                message = wx.MessageDialog(None,'The file does not exist!','ERROR',wx.OK | wx.ICON_ERROR)
                if message.ShowModal() == wx.ID_OK:
                    pass
        else:
            message = wx.MessageDialog(None,'Please enter the correct path!','ERROR',wx.OK | wx.ICON_ERROR)
            if message.ShowModal() == wx.ID_OK:
                pass
app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()