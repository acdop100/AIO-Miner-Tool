import tkinter
import os
import urllib.request

mainWindow = None
packer = []

#An option class which contains a box which text can be put in and the label to describe the box
class Option:
    def __init__(self, label, box):
        self.label = label
        self.box = box

#Sets the window in which the labels, buttons, etc. are created in
def setMainWindow(panel):
	mainWindow = panel

#Adds a thingy to the packer, such as: labels, entries, and buttons
def addToPacker(o):
	packer.append(o)

#Creates and returns a label
def createLabel(txt):
	label = tkinter.Label(mainWindow, text=txt)
	addToPacker(label)
	return label

#Creates a label with a specific font and returns a label
def createLabelWithFont(fnt, txt):
	label = tkinter.Label(mainWindow, text=txt, font=fnt)
	addToPacker(label)
	return label

#Creates and returns a button
def createButton(txt, cmd):
	button = tkinter.Button(mainWindow, text=txt, command=cmd)
	addToPacker(button)
	return button

#Creates and returns an entry
def createBox():
	box = tkinter.Entry(mainWindow)
	addToPacker(box)
	return box

#Creates and returns an option; check the class for more info
def createOption(txt):
	return Option(createLabel(txt), createBox());

#Packs all of the different things placed in the packer in the order that they were put in the packer
def packAll():
	for box in packer:
		box.pack()