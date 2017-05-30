
import wx
import os
class recog(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Handwriting Recognition',size=(400,510))
        # mainPanel =wx.Panel(self)

        self.panel=wx.Panel(self)
        heading=wx.StaticText(self.panel,-1,"HANDWRITING RECOGNITION TOOL",(25,50));
        font = self.GetFont() 
        font.SetPointSize(16) 
        heading.SetFont(font)
        self.createImagePicker()

        exitButton=wx.Button(self.panel,label="Exit",pos=(150,350),size=(100,30))
        wx.StaticText(self.panel,-1,"Project by Aishwarya Paher, Akash Rawat, Apurva Thakur",(40,400));
        
        self.Bind(wx.EVT_BUTTON,self.closeAction,exitButton)

        self.Bind(wx.EVT_CLOSE,self.closeWindow)

        statusBar=self.CreateStatusBar()
        menuBar = wx.MenuBar();
        first=wx.Menu()

        first.Append(wx.NewId(),"About","About the project")
        first.Append(wx.NewId(),"Help","How to run the program")

        menuBar.Append(first,"Help")
        self.SetMenuBar(menuBar)

    def createImagePicker(self):
        """
        Create image picker
        """
        wx.StaticText(self.panel,-1,"CHOOSE IMAGE",(100,85));
        self.photoTxt = wx.TextCtrl(self.panel, size=(200,-1),pos=(100,120))
        browseBtn = wx.Button(self.panel, label='Browse',pos=(200,80))
        browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)
        recognizeButton=wx.Button(self.panel,label="Recognize",pos=(150,230),size=(100,30))
        recognizeButton.Bind(wx.EVT_BUTTON, self.onRecog)
        
    def onRecog(self, event):
        """ 
        Browse for file
        """
        os.system('python performRecognition.py -c digits_cls.pkl -i '+self.photoTxt.GetValue())

    def onBrowse(self, event):
        """ 
        Browse for file
        """
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",wildcard=wildcard,style=wx.OPEN)
#        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.photoTxt.SetValue(dialog.GetPath())
        dialog.Destroy() 


    def closeAction(self,event):
        self.Close(True)

    def closeWindow(self,event):
        self.Destroy()


if __name__=='__main__':
    app = wx.App()

    frame = recog(parent=None, id=-1)
    frame.Show()

    app.MainLoop()