# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse,Circle,Polygon,Rectangle
import numpy as np
from numpy import sqrt


class ExamplePanel(wx.Panel):           ##### this class is the second page of the notebook
    

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        # instructions at top of page
        self.quote = wx.StaticText(self, label="Design your profile here, then go the the next step.")
        grid.Add(self.quote, pos=(0,0))


        ############################Set up the default figure
        self.fig = Figure(figsize=(2, 3), dpi=100)
        self.axes = self.fig.add_subplot(111)
        self.fig, ax = plt.subplots() 
        #####head
        self.background=Rectangle((0.,0.),1.,1.,color='white')
        self.head = Ellipse(xy=(0.5, 0.7), width=0.15, height=0.3, color='bisque')
        #####eyes
        self.eyesY=0.73
        self.remidx=0.53
        self.remidy=self.eyesY
        self.righteyewhite=Ellipse(xy=(self.remidx, self.remidy), width=0.04, height=0.03, color='white')
        self.rerad=0.007
        self.rebX=self.remidx
        self.rebY=self.remidy
        self.rpupil=0.01
        self.righteyeblack=Circle((self.rebX, self.rebY), self.rpupil, color='black')
        self.lemidx=0.47
        self.lemidy=self.eyesY
        self.lebX=self.lemidx
        self.lebY=self.lemidy
        self.lefteyewhite=Ellipse(xy=(self.lemidx, self.lemidy), width=0.04, height=0.03, color='white')
        self.lefteyeblack=Circle((self.lebX, self.lebY), self.rpupil, color='black')
        #####shirt
        self.shirtcolor='darkgray'
        self.shmid=0.5#shirtmid
        self.shw=0.13#shirtwidth
        self.shirtlist=[(self.shmid-self.shw,0.6),(self.shmid-self.shw-0.07,0.45),(self.shmid-self.shw-0.02,0.4),(self.shmid-self.shw,0.45),(self.shmid-self.shw,0.1),(self.shmid+self.shw,0.1),(self.shmid+self.shw,0.45),(self.shmid+self.shw+0.02,0.4),(self.shmid+self.shw+0.07,0.45),(self.shmid+self.shw,0.6)]
        self.shirt = Polygon(self.shirtlist,True, color=self.shirtcolor)
        self.shirtcontour = Polygon(self.shirtlist,True, color='black',fill=False)
        #####hair
        hairlist=[(0.55,0.75),(0.50,0.79),(0.47,0.77),(0.44,0.79),(0.42,0.77),(0.43,0.78),(0.41,0.81),(0.46,0.85),(0.49,0.88),(0.53,0.86),(0.55,0.87),(0.58,0.79),(0.55,0.76)]
        self.hair= Polygon(hairlist,True,color='darkgray')
        #####glasses
        self.brilhoog=0.75
        self.brillaag=0.728
        self.rightglass=Ellipse(xy=(self.remidx, self.remidy), width=0.06, height=0.05, color='black',fill=False,lw=2)
        self.leftglass=Ellipse(xy=(self.lemidx, self.lemidy), width=0.06, height=0.05, color='black',fill=False,lw=2)
        self.rightpoot = plt.Line2D((0.44,0.42),(self.brillaag,self.brilhoog), lw=2, color='black')
        self.leftpoot  = plt.Line2D((0.56,0.58),(self.brillaag,self.brilhoog), lw=2, color='black')
        self.rightglass.set_visible(False)
        self.leftglass.set_visible(False)
        self.rightpoot.set_visible(False)
        self.leftpoot.set_visible(False)
        self.glasseson=0
        ##### add the shapes to the figure        
        ax.set_axis_off()
        ax.add_artist(self.background)
        ax.add_artist(self.shirt)
        ax.add_artist(self.shirtcontour)
        ax.add_artist(self.head)
        ax.add_artist(self.righteyewhite)
        ax.add_artist(self.righteyeblack)
        ax.add_artist(self.lefteyewhite)
        ax.add_artist(self.lefteyeblack)
        ax.add_artist(self.hair)
        ax.add_artist(self.rightglass)
        ax.add_artist(self.leftglass)
        ax.add_artist(self.rightpoot)
        ax.add_artist(self.leftpoot)
        ###### draw the figure
        self.fig.canvas.draw() 
        self.canvas = FigureCanvas(self, -1, self.fig)
        ##############################################################
        
        # Next step button
        self.button =wx.Button(self, label="Next step")
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        
        # Slider for shirt size
        self.balkX=5
        self.balkY=8
        self.balk = wx.Slider(self, value=2, minValue=0, maxValue=5, size=(300,40), style=wx.SL_HORIZONTAL)
        grid.Add(self.balk,pos=(9,0))
        self.lblshirt = wx.StaticText(self, label="What size are you?")
        grid.Add(self.lblshirt, pos=(7,0))
        self.lblshirtsz = wx.StaticText(self, label="    XS              S               M               L               XL            XXL")
        grid.Add(self.lblshirtsz, pos=(8,0))
        self.balk.Bind(wx.EVT_SLIDER, self.OnSliderScroll)
        self.keuzeval=0 #default value

        # the editor for the costumer name
        self.username="Costumer_name"
        self.lblname = wx.StaticText(self, label="What's your name :")
        grid.Add(self.lblname, pos=(1,0))
        self.editname = wx.TextCtrl(self, value=self.username, size=(140,-1))
        grid.Add(self.editname, pos=(1,1))
        self.Bind(wx.EVT_TEXT, self.EvtText1, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        # the combobox to choose which type of order
        self.sampleList = ['Myself on a shirt', 'My favourite galaxy', 'My favourite 2D graph']
        self.lblhear = wx.StaticText(self, label="What type of shirt would you like to order ?")
        grid.Add(self.lblhear, pos=(3,0))
        self.edithear = wx.ComboBox(self, size=(150, -1), 
                                    choices=self.sampleList, 
                                    style=wx.CB_DROPDOWN)
        grid.Add(self.edithear, pos=(3,1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtText,self.edithear)

        # add a spacer to the sizer
        grid.Add((10, 40), pos=(2,0))

        # Checkbox for glasses or not 
        self.insure = wx.CheckBox(self, label="I have glasses")
        grid.Add(self.insure, pos=(4,0), span=(1,2), 
                 flag=wx.BOTTOM, border=5)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        # Radio Boxes for hair color
        radioList = ['light blond', 'blond', 'light brown', 'brown', 'black', 'red', 'blue', 'gray', 'white']
        rb = wx.RadioBox(self, label="What hair color do you have?", pos=(20, 210), choices=radioList,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        grid.Add(rb, pos=(5,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)
        
        # Radio Boxes for shirt color
        radioList2 = ['red', 'orange', 'yellow', 'green', 'blue', 'puple', 'black', 'gray', 'white']
        rb2 = wx.RadioBox(self, label="What colour should your shirt be?", pos=(20, 210), choices=radioList2,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        grid.Add(rb2, pos=(10,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox2, rb2)
        
        #mouse move event so eyes will follow the mouse
        self.Bind(wx.EVT_MOTION,self.OgenBewegen)

        #the left and right part of the screen
        hSizer.Add(grid, 0, wx.ALL, 5)
        hSizer.Add(self.canvas) 
        
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        mainSizer.Add(self.button, 0, wx.CENTER)
        self.SetSizerAndFit(mainSizer)
        
    def OgenBewegen(self,event): #makes the eyes follow the mouse
        xmuis,ymuis = event.GetPositionTuple()
        distancefromreye=sqrt((self.rebX-xmuis)**2+(self.rebY-ymuis)**2)
        distancefromleye=sqrt((self.lebX-xmuis)**2+(self.lebY-ymuis)**2)
        rfactor=self.rerad/distancefromreye
        lfactor=self.rerad/distancefromleye
        newrebX=self.remidx+rfactor*(self.remidx-xmuis)
        newrebY=self.remidy+rfactor*(self.remidy-ymuis)
        newlebX=self.lemidx+lfactor*(self.lemidx-xmuis)
        newlebY=self.lemidy+lfactor*(self.lemidy-ymuis)
        self.righteyeblack.center = newrebX, newrebY
        self.lefteyeblack.center  = newlebX, newlebY
        self.fig.canvas.draw()

    def OnSliderScroll(self,event): #changes the size of the shirt
        maat=event.GetInt()
        self.maat=event.GetInt()
        self.shw=0.09+0.02*maat#shirtwidth
        print "Balkje value =", event.GetInt(),"shirtwidth=",self.shw
        print "Shirt coordinates before:", self.shirtlist[0:4]
        self.shirtlist=[(self.shmid-self.shw,0.6),(self.shmid-self.shw-0.07,0.45),(self.shmid-self.shw-0.02,0.4),(self.shmid-self.shw,0.45),(self.shmid-self.shw,0.1),(self.shmid+self.shw,0.1),(self.shmid+self.shw,0.45),(self.shmid+self.shw+0.02,0.4),(self.shmid+self.shw+0.07,0.45),(self.shmid+self.shw,0.6)]
        print "Shirt coordinates after:", self.shirtlist[0:4]

        self.shirt.set_xy(self.shirtlist)
        self.shirtcontour.set_xy(self.shirtlist)
        self.fig.canvas.draw() 

    def EvtRadioBox(self, event): #change the hair color
        self.welke=event.GetInt()
        if self.welke is 0:
            self.hair.set_color('khaki')
        elif self.welke is 1: 
            self.hair.set_color('gold')
        elif self.welke is 2:
            self.hair.set_color('goldenrod')
        elif self.welke is 3: 
            self.hair.set_color('saddlebrown')
        elif self.welke is 4:
            self.hair.set_color('black')
        elif self.welke is 5: 
            self.hair.set_color('red')
        elif self.welke is 6:
            self.hair.set_color('blue')
        elif self.welke is 7: 
            self.hair.set_color('gray')
        elif self.welke is 8:
            self.hair.set_color('white')
        print "hair color is: ",self.welke    
        self.fig.canvas.draw()
        
    def EvtRadioBox2(self, event):
        self.shcol=event.GetInt()
        if self.shcol is 0:
            self.shirt.set_color('red')
        elif self.shcol is 1: 
            self.shirt.set_color('orange')
        elif self.shcol is 2:
            self.shirt.set_color('yellow')
        elif self.shcol is 3: 
            self.shirt.set_color('green')
        elif self.shcol is 4:
            self.shirt.set_color('blue')
        elif self.shcol is 5: 
            self.shirt.set_color('purple')
        elif self.shcol is 6:
            self.shirt.set_color('black')
        elif self.shcol is 7: 
            self.shirt.set_color('gray')
        elif self.shcol is 8:
            self.shirt.set_color('white')
        print "Shirt color is: ",self.shcol    
        self.fig.canvas.draw() 

    def EvtComboBox(self, event):
        print 'Combobox was clicked'
        
    def OnClick(self,event):
        self.fig.savefig('profile.png') #save profile picture
     
        f = open('costumerdata.txt', 'a') #write constumer data to database
        info=[self.username,self.keuzeval,self.glasseson,self.welke,self.maat,self.shcol]
        print info
        for item in info:  f.write("%s\t" % item)
        f.write("\n")
        f.close()
        
        g = open('tpm.txt', 'w') #write order type to temporary file
        g.write(str(self.keuzeval))
        print 'keuzeval', self.keuzeval, 'written to file'
        g.close
        
        h = open('tmpname.txt', 'w') #write costumer name to temporary file
        h.write(str(self.username))
        print 'username', self.username, 'written to file'
        h.close
       
    def EvtText1(self, event): #reads the username
        print 'EvtText1 ziet', event.GetString()
        self.username=event.GetString()

    def EvtText(self, event): #reads which thing to print on shirt
        keuze=event.GetString()
        print 'Choice =', keuze
        self.keuzeval=0
        if keuze in self.sampleList[0]:
            self.keuzeval=1   
        elif keuze in  self.sampleList[1]:
            self.keuzeval=2
        elif keuze in self.sampleList[2]:
            self.keuzeval=3
        elif keuze in self.sampleList[3]:
            self.keuzeval=4   
        print 'Keuzeval=',self.keuzeval
        
    def EvtChar(self, event): #lets name appear in the type box
        print "EvtChar geeft:", event.GetKeyCode()
        event.Skip()
        
    def EvtCheckBox(self, event): #checks whether glasses should be on or off
        if event.Checked():
            print "Bril op"
            self.rightglass.set_visible(True)
            self.leftglass.set_visible(True)
            self.rightpoot.set_visible(True)
            self.leftpoot.set_visible(True)
            self.glasseson=1            
        elif event.Checked() is False:
            print "Bril af"
            self.rightglass.set_visible(False)
            self.leftglass.set_visible(False)
            self.rightpoot.set_visible(False)
            self.leftpoot.set_visible(False)
            self.glasseson=0
        self.fig.canvas.draw()
   