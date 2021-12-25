# coding=utf-8
import wx
import os
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='Uninstall sign',size=(500,100))
        panel = wx.Panel(parent=self)
        icon = wx.Icon('icon.ico',wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        self.sc = wx.StaticText(panel,label='Path:')
        self.tc = wx.TextCtrl(panel)
        self.tc.SetValue('C:\\')
        self.button = wx.Button(panel,label='Uninstall',pos=(100,50))
        self.Bind(wx.EVT_BUTTON,self.on_click,self.button)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.sc,flag=wx.EXPAND,border=10)
        vbox.Add(self.tc,flag=wx.EXPAND,border=10)
        vbox.Add(self.button,flag=wx.EXPAND,border=10)
        panel.SetSizer(vbox)
    def on_click(self,event):
        path = self.tc.GetValue()
        if os.path.exists(path):
            if 'sign.sign' in os.listdir(path):
                command = 'del '
                command += path
                command += '\\sign.sign'
                os.popen(command)
                message = wx.MessageDialog(None,'Uninstall succeeded!','INFORMATION',wx.OK | wx.ICON_INFORMATION)
                if message.ShowModal() == wx.ID_OK:
                    pass
            else:
                message = wx.MessageDialog(None,'You have uninstalled or not installed sign!','WARNING',wx.OK | wx.ICON_WARNING)
                if message.ShowModal() == wx.ID_OK:
                    pass
        else:
            message = wx.MessageDialog(None,'The path is wrong!','ERROR',wx.OK | wx.ICON_ERROR)
            if message.ShowModal() == wx.ID_OK:
                pass
app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()