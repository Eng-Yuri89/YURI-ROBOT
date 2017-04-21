import wx
import wikipedia
import wolframalpha
import  pyttsx

engine = pyttsx.init()
# endregion

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          pos=wx.DefaultPosition, size=wx.Size(450, 100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                                wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="yuri")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
                            label="Hello I am YURI the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        usrinput = input.lower()
        try:
            # wolframalpha
            client = wolframalpha.Client ('QEUXVY-VRAH5X4EA6')
            res = client.query(usrinput)
            answer = next (res.results).text
            engine.say (answer)
            print (answer) , engine.runAndWait()
        except:
            usrinputs = wikipedia.summary(usrinput)
            print ( wikipedia.summary ( usrinput, sentences=1 ) )
            engine.say(usrinputs)
            engine.runAndWait()






if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()





engine.runAndWait()