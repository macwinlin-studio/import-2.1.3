# coding=utf-8
import wx,os
from function import read,jd
def isi(l,dx):
    for i in range(len(l)):
        if l[i] in dx:
            return False
    return True
def make(path,suffix):
    if isi(['/', '\\', '?', ':', '*', '"', '<', '>', '|'],path):
        message = wx.MessageDialog(None,"Can't contain any of the following characters: (spaces),/,\\,?,:,*,<,> and |.Otherwise,an exception is thrown.",'WARNING',wx.OK | wx.ICON_WARNING)
        if message.ShowModal() == wx.ID_OK:
            return None
    file = open(path,'w',encoding='utf-8')
    if suffix == '.py' or suffix == '.pyw':
        file.write('# coding=utf-8')
    elif suffix == '.html':
        file.write('<!DOCTYPE html>\n')
        file.write('<html lang="zh">\n')
        file.write('<head>\n')
        file.write('    <meta charset="UTF-8">\n')
        file.write('    <title>HTML</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('    <p>HTML file</p>\n')
        file.write('</body>\n')
        file.write('</html>')
    elif suffix == '.java':
        file.write('public class [file name] {\n')
        file.write('    public static void main(String[] args) {\n')
        file.write('    }\n')
        file.write('}')
    else:
        pass
    file.close()
    message = wx.MessageDialog(None,'Make success!','INFORMATION',wx.OK | wx.ICON_INFORMATION)
    if message.ShowModal() == wx.ID_OK:
        pass
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='Make code',size=(300,285))
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
        self.pathsc = wx.StaticText(panel,label='Save Path:(File name not included)')
        self.path = wx.TextCtrl(panel)
        self.path.SetValue(read(0))
        self.namesc = wx.StaticText(panel,label='File Name:(Does not include suffix)')
        self.name = wx.TextCtrl(panel)
        self.name.SetValue('New project')
        self.button = wx.Button(panel,label='Make',pos=(100,50))
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
        vbox.Add(self.namesc,flag=wx.EXPAND,border=10)
        vbox.Add(self.name,flag=wx.EXPAND,border=10)
        vbox.Add(self.button,flag=wx.EXPAND,border=10)
        panel.SetSizer(vbox)
    def on_radio_click(self,event):
        listbox = event.GetEventObject()
        listbox = jd(listbox.GetLabel())
        if listbox == 1:
            self.suffix = '.js'
            self.path.SetValue(read(1))
        elif listbox == 0:
            self.suffix = '.py'
            self.path.SetValue(read(0))
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
            self.path.SetValue(read(0))
        else:
            self.suffix = 'error'
    def on_click(self,event):
        path = self.path.GetValue()
        name = self.name.GetValue()
        name += self.suffix
        try:
            file = open(path + '\\sign.sign')
            if not file.read() == 'Install sign...\nStart...\n10%...\n15%...\n20%...\n21%...\n35%...\n50%...\n60%...\n70%...\n100%...\nThis is sign file.\nOK.You can use auto create program now.':
                a = 0 / 0
            file.close()
        except:
            message = wx.MessageDialog(None,'The path is wrong or the identity file is not installed.','ERROR',wx.OK | wx.ICON_ERROR)
            if message.ShowModal() == wx.ID_OK:
                pass
        else:
            if name in os.listdir(path):
                message = wx.MessageDialog(None,'This file already exists in this directory. Do you want to replace it?','WARNING',wx.YES_NO | wx.ICON_WARNING)
                if message.ShowModal() == wx.ID_YES:
                    path += '\\'
                    path += name
                    make(path,self.suffix)
            else:
                path += '\\'
                path += name
                make(path,self.suffix)
app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()