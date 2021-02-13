import wx
from pexpect import popen_spawn

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        panel = wx.Panel(self)
        
        self.static_text1 = wx.StaticText(panel, label="Host:", pos = (40,40))
        self.static_text2 = wx.StaticText(panel, label="Path:", pos = (40, 80))
        self.static_text3 = wx.StaticText(panel, label="FileName:", pos = (40, 120))
        self.text1 = wx.TextCtrl(panel, value = "100.23.45.1", pos = (100, 35), size = (120, 25))
        self.text2 = wx.TextCtrl(panel, value = "remotepath", pos = (100, 75), size = (120, 25))
        self.text3 = wx.TextCtrl(panel, value = "filename", pos = (100, 115), size = (120, 25))

        self.button1 = wx.Button(panel, label = "scp", pos = (250, 150), size = (100, 30))

        self.Bind(wx.EVT_BUTTON, self.OnButton1, self.button1)

    def Scp(self, host, path, fileName):
        user = "user"
        paasWord = "pass"
        command = "scp -r %s@%s:%s/%s ." % (user, host, path, fileName)
        child = popen_spawn.PopenSpawn(command)
        child.expect('password:', timeout = 5)
        child.sendline(passWord)        
        print(child.after)

    def OnButton1(self, event):
        print("scp begin!")
        host = self.text1.Value
        path = self.text2.Value
        fileName = self.text3.Value
        self.Scp(host, path, fileName)
        print("scp finish!")

app = wx.App()
frame = MyFrame(None, title = "scp tool")
frame.Show()
app.MainLoop()
