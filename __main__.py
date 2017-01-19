# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:24:12 2017

@author: Loes
"""

import wx
from example import ExamplePanel
from design import ShirtDesignPanel

app = wx.App(False)
frame = wx.Frame(None,title="Shirt designer", size=(1000,700))
nb=wx.Notebook(frame)
nb.AddPage(ExamplePanel(nb),"Make your profile")
nb.AddPage(ShirtDesignPanel(nb),"Choose your print")

frame.Show()

app.MainLoop()
