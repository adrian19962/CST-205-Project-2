import wx

class windowClass(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs) 

        self.basicGUI()
       

    def basicGUI(self):

        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        editButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT, 'Quit\tCtrl+Q')
        exitItem.SetBitmap(wx.Bitmap(#enter pic address here))
        fileButton.AppendItem(exitItem)
                                     
        button=wx.Button(panel,label="Filter",pos=(130,10),size=(60,60))
        self.Bind(wx.EVT_BUTTON, self.filter, button)
                                     
    def filter(self,event):
        #Enter filter code
                             

        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        wx.TextCtrl(panel, pos=(10,10), size = (250,150))
        
        self.SetTitle('Epic Window')
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()   
