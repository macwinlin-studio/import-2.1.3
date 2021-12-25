# coding=utf-8
import wx
import os
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='Install sign',size=(500,105))
        panel = wx.Panel(parent=self)
        icon = wx.Icon('icon.ico',wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        self.sc = wx.StaticText(panel,label='Path:')
        self.tc = wx.TextCtrl(panel)
        self.tc.SetValue('C:\\')
        self.button = wx.Button(panel,label='Install',pos=(100,50))
        self.Bind(wx.EVT_BUTTON,self.on_click,self.button)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.sc,flag=wx.EXPAND,border=10)
        vbox.Add(self.tc,flag=wx.EXPAND,border=10)
        vbox.Add(self.button,flag=wx.EXPAND,border=10)
        panel.SetSizer(vbox)
    def on_click(self,event):
        path = self.tc.GetValue()
        if os.path.exists(path):
            if not 'sign.sign' in os.listdir(path):
                path += '\\sign.sign'
                file = open(path,'w')
                file.write('Install sign...\nStart...\n10%...\n15%...\n20%...\n21%...\n35%...\n50%...\n60%...\n70%...\n100%...\nThis is sign file.\nOK.You can use auto create program now.')
                file.close()
                message = wx.MessageDialog(None,'Installation successful!','INFORMATION',wx.OK | wx.ICON_INFORMATION)
                if message.ShowModal() == wx.ID_OK:
                    pass
            else:
                message = wx.MessageDialog(None,'You have installed sign!','WARNING',wx.OK | wx.ICON_WARNING)
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