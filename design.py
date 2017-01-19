# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:28:40 2017

@author: Loes
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import wx
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Polygon
import time


class ShirtDesignPanel(wx.Panel):             ##### this class is the second page of the notebook
 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.quote = wx.StaticText(self, label="Design your profile here, then go the the next step.")
        grid.Add(self.quote, pos=(0,0))
        g = open('tpm.txt', 'r')
        for line in g:
            self.keus = line.strip().split()
        self.keuze=int(float(self.keus[0]))
        print 'keuze is', self.keuze
        print 'type is', type(self.keuze)
        self.shcol=0

        self.fig = Figure(figsize=(2, 3), dpi=100)
        self.axes = self.fig.add_subplot(111)
        self.fig, ax = plt.subplots()      

        #####shirt  
        self.shirtcolor='darkgray'
        self.shmid=0.5#shirtmid
        self.shw=0.4#shirtwidth
        self.shh=0.9
        self.shirtlist=[(self.shmid-self.shw,self.shh),(self.shmid-self.shw-0.07,self.shh-0.15),(self.shmid-self.shw-0.02,self.shh-0.2),(self.shmid-self.shw,self.shh-0.15),(self.shmid-self.shw,self.shh-0.8),(self.shmid+self.shw,self.shh-0.8),(self.shmid+self.shw,self.shh-0.15),(self.shmid+self.shw+0.02,self.shh-0.2),(self.shmid+self.shw+0.07,self.shh-0.15),(self.shmid+self.shw,self.shh)]
        self.shirt = Polygon(self.shirtlist,True, color=self.shirtcolor)
        self.shirtcontour = Polygon(self.shirtlist,True, color='black',fill=False)
        self.axes2 = self.fig.add_axes([0.3, 0.4, 0.4, 0.3]) # inset axes
        #####image on the shirt
        self.im = mpimg.imread('profile.png')
        self.axes2.imshow(self.im)
        self.axes2.axis('off')
        #####add shirt to figure
        ax.add_artist(self.shirt)
        ax.add_artist(self.shirtcontour)
        ax.axis('off')
        #####draw the canvas
        self.fig.canvas.draw() 
        self.canvas = FigureCanvas(self, -1, self.fig)

        grid.Add((10, 40), pos=(2,0))

        #Refresh button
        self.button =wx.Button(self, label="Refresh")
        self.Bind(wx.EVT_BUTTON, self.Go0,self.button)
        grid.Add(self.button, pos=(1,0))       
        
        #orderbutton
        self.orderbutton = wx.Button(self,label="Order!")
        self.Bind(wx.EVT_BUTTON,self.order,self.orderbutton)
        grid.Add(self.orderbutton, pos=(5,0))

        #select your favourite galaxy
        radioList3 = ['Milky Way', 'Andromeda', 'NGC 1300']
        rb3 = wx.RadioBox(self, label="What is your favorite galaxy", pos=(20, 210), choices=radioList3,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        grid.Add(rb3, pos=(3,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox3, rb3)
   
        hSizer.Add(grid, 0, wx.ALL, 5)
        hSizer.Add(self.canvas) 
        
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)

    def Go0(self,event):#checks which type of thing should be plotted upon refresh, activates correct next step
        g = open('tpm.txt', 'r')
        for line in g:
            self.keus = line.strip().split()
        self.keuze=int(float(self.keus[0]))
        print 'keuze is', self.keuze
        print 'type is', type(self.keuze)
        if self.keuze is 1: 
            self.Go1(event)
        elif self.keuze is 2: 
            self.Go2(event)
        elif self.keuze is 3:
            self.Go3(event)
        
    def Go1(self,event):#plots the profile 
        self.axes2.axis('off')
        print 'Go1 activated due to keuze=',self.keuze
        self.im = mpimg.imread('profile.png')
        self.axes2.imshow(self.im)
        self.fig.canvas.draw() 

    def Go2(self,event):#plots the preferred galaxy
        self.axes2.axis('off')
        print 'Go2 activated due to keuze=',self.keuze
        print 'From radiobox use galaxy:', self.shcol
        if self.keuze is 2:
            if self.shcol is 0:
                self.im = mpimg.imread('galaxy2.jpg')
            elif self.shcol is 1: 
                self.im = mpimg.imread('galaxy1.jpg')
            elif self.shcol is 2:
                self.im = mpimg.imread('galaxy3.jpg')
        self.axes2.imshow(self.im)
        self.fig.canvas.draw() 
        
    def Go3(self,event): #plots a graph
        print 'Go3 activated due to keuze=',self.keuze
        self.axes2.axis('on')
        x = np.arange(0,1,0.1)
        y = x**2
        self.axes2.plot(y, x, 'g')
        self.fig.canvas.draw() 

    def EvtRadioBox3(self, event): #reads preferred galaxy from radiobox
        self.shcol=event.GetInt()
        print "Galaxy nr ",self.shcol
        self.Go2(event)
        
    def order(self,event): #saves the order to a file
        tijd1=time.strftime("%I:%M:%S")
        print tijd1
        tijd2=tijd1[0:2]+tijd1[3:5]+tijd1[6:8]
        print tijd2
        h = open('tmpname.txt', 'r')
        for line in h:
            self.naam = line.strip().split()
        self.username=self.naam[0]
        print 'username=', self.username
        ordername = 'order'+self.username+tijd2+'.png'
        self.fig.savefig(ordername)



