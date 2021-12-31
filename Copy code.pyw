# coding=utf-8
from shutil import copyfile
import pathlib,wx
from os import listdir
from function import read,pd,jd
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='Copy code',size=(300,330))
        panel = wx.Panel(parent=self)
        icon = wx.Icon('icon.ico',wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        self.suffix = '.py'
        self.sc = wx.StaticText(panel,label='Language:')
        self.radio1 = wx.RadioButton(panel,id=1,label='Python(.py)',style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(panel,id=2,label='JavaScript')
        self.radio3 = wx.RadioButton(panel,id=3,label='HTML5')
        self.radio4 = wx.RadioButton(panel,id=4,label='JAVA')
        self.radio5 = wx.RadioButton(panel,id=5,label='C')
        self.radio6 = wx.RadioButton(panel,id=6,label='C++')
        self.radio7 = wx.RadioButton(panel,id=7,label='Python(.pyw)')
        self.Bind(wx.EVT_RADIOBUTTON,self.on_radio_click,id=1,id2=7)
        self.pathsc = wx.StaticText(panel,label='Path:(Including the original file name and suffix)')
        self.path = wx.TextCtrl(panel)
        if pd(0):
            self.path.SetValue(read(0) + '\\[file name].py')
        else:
            self.path.SetValue(read(0) + '[file name].py')
        self.path2sc = wx.StaticText(panel,label='Copy Path:(File name not included)')
        self.path2 = wx.TextCtrl(panel)
        self.path3sc = wx.StaticText(panel,label='Copy Name:(Does not include suffix)')
        self.path3 = wx.TextCtrl(panel)
        self.button = wx.Button(panel,label='Copy',pos=(100,50))
        self.Bind(wx.EVT_BUTTON,self.on_click,self.button)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.sc,flag=wx.EXPAND,border=10)
        vbox.Add(self.radio1)
        vbox.Add(self.radio2)
        vbox.Add(self.radio3)
        vbox.Add(self.radio4)
        vbox.Add(self.radio5)
        vbox.Add(self.radio6)
        vbox.Add(self.radio7)
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
        elif listbox == 6:
            self.suffix = '.pyw'
            if pd(6):
                self.path.SetValue(read(6) + '\\[file name].pyw')
            else:
                self.path.SetValue(read(6) + '[file name].pyw')
        else:
            self.suffix = 'error'
    def on_click(self,event):
        path = pathlib.Path(self.path.GetValue())
        if path.is_file():
            path = pathlib.Path(self.path2.GetValue())
            if self.path3.GetValue() + self.suffix not in listdir(self.path2.GetValue()):
                if path.is_dir():
                    path = self.path.GetValue()
                    c_path = self.path2.GetValue()
                    c_name = self.path3.GetValue()
                    c_name += self.suffix
                    c_path += '\\'
                    c_path += c_name
                    copyfile(path,c_path)
                    message = wx.MessageDialog(None,'Copy succeeded!','INFORMATION',wx.OK | wx.ICON_INFORMATION)
                    if message.ShowModal() == wx.ID_OK:
                        pass
                else:
                    message = wx.MessageDialog(None,'Copy path error!','ERROR',wx.OK | wx.ICON_ERROR)
                    if message.ShowModal() == wx.ID_OK:
                        pass
            else:
                message = wx.MessageDialog(None,'The file already exists. Do you want to replace it?','QUESTION',wx.YES_NO | wx.ICON_QUESTION)
                if message.ShowModal() == wx.ID_YES:
                    from os import remove
                    remove(self.path3.GetValue() + self.suffix)
                    if path.is_dir():
                        path = self.path.GetValue()
                        c_path = self.path2.GetValue()
                        c_name = self.path3.GetValue()
                        c_name += self.suffix
                        c_path += '\\'
                        c_path += c_name
                        copyfile(path, c_path)
                        message = wx.MessageDialog(None, 'Copy succeeded!', 'INFORMATION', wx.OK | wx.ICON_INFORMATION)
                        if message.ShowModal() == wx.ID_OK:
                            pass
                    else:
                        message = wx.MessageDialog(None, 'Copy path error!', 'ERROR', wx.OK | wx.ICON_ERROR)
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