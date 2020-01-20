import wx
import wikipedia
import wolframalpha
listOfQuestionWords = ['who' , 'what', 'where', 'when', 'which', 'how']
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
        pos=wx.DefaultPosition, size=wx.Size(450,100),
        style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
        wx.CLOSE_BOX | wx.CLIP_CHILDREN,
        title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello, I am your personal assistant. How may I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        query = self.txt.GetValue()
        query = query.lower()
        try:
            # wolframalpha
            app_id = "YK36GA-W36R83QG5E"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
            print(answer)
        except:
            # wikipedia
            query = query.split(' ')
            if query[0] in listOfQuestionWords:
                query = " ".join(query[2:])
            print(wikipedia.summary(query))

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
