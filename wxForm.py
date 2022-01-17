import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title="wxPython",size=(400,300),pos=(100,100))
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel,label = "hello,python",pos=(100,100))

        b1 = wx.Button(parent=panel,id=10,label="click",pos=(100,150))
        b2 = wx.Button(parent=panel,id=11,label="click",pos=(100,150))

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(b1,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
        hbox.Add(b2,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.statictext,proportion=1,
                 flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.TOP,border=30)
                # ALIGN_CENTER_HORIZONTAL 控件水平居中
                # border 顶部边框宽度
                # FIXED_MINSIZE 刚好包裹控件
                # TOP 顶部有边框
        vbox.Add(hbox,proportion=1,flag=wx.CENTER)
                # EXPAND 完全填满有效空间
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON,self.on_click,id=10,id2=20)

    def on_click(self,event):
        event_id = event.GetId()
        if(event_id==10):
            self.statictext.SetLabelText("button1 clicked")
        else:
            self.statictext.SetLabelText("button2 clicked")


app = wx.App()

frm = MyFrame()
# frm = wx.Frame(None,title='wxPython',size=(400,300),pos=(100,100))
frm.Show()

app.MainLoop()