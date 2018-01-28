#resize.py
#Nathan Kennedy

from PIL import Image as IMAGE
import sys
from tkinter import *


def setAspectRatio(width, height):
    global img
    newWidth = size[0] - (size[0] % width)
    newHeight = int(newWidth/width) * height
    img = img.resize((newWidth, newHeight),IMAGE.ANTIALIAS)

def setSize(width, height):
    global img
    img = img.resize((width,height),IMAGE.ANTIALIAS)


def process():
    if selection.get() == 1:
        setAspectRatio(16,9)
    elif selection.get() == 2:
        setAspectRatio(4,3)
    elif selection.get() == 3:
        setSize(1920,1080)
    elif selection.get() == 4:
        setSize(128,128)
    elif selection.get() == 5:
        setAspectRatio(int(ratioWidth.get()),int(ratioHeight.get()))
    else:
        setSize(int(resolutionWidth.get()),int(resolutionHeight.get()))
    img.save("output.png")
    root.destroy()



img = IMAGE.open(sys.argv[1])
size = img.size 



#tkinter window
root = Tk()
root.geometry("220x126")
root.title("resize.py")
mainFrame = Frame(root)

selection = IntVar()
selection.set(1)
ratioWidth = StringVar()
ratioWidth.set("0")
ratioHeight = StringVar()
ratioHeight.set("0")
resolutionWidth = StringVar()
resolutionWidth.set("0")
resolutionHeight = StringVar()
resolutionHeight.set("0")

#16:9 image window
radioA = Radiobutton(mainFrame, variable = selection, value = 1)
labelA = Label(mainFrame, text = "16:9")

#4:3 image window
radioB = Radiobutton(mainFrame, variable = selection, value = 2)
labelB = Label(mainFrame, text = "4:3")

#1920x1080 image window
radioC = Radiobutton(mainFrame, variable = selection, value = 3)
labelC = Label(mainFrame, text = "1920x1080")

#128x128 image window
radioD = Radiobutton(mainFrame, variable = selection, value = 4)
labelD = Label(mainFrame, text = "128x128")

#custom ratio
radioE = Radiobutton(mainFrame, variable = selection, value = 5)
labelE = Label(mainFrame, text = "Custom Ratio")
entryWidthE = Entry(mainFrame, textvariable = ratioWidth,width = 5)
entryHeightE = Entry(mainFrame, textvariable = ratioHeight,width = 5)
labelColonE = Label(mainFrame, text = ":")

#custom resolution
radioF = Radiobutton(mainFrame, variable = selection, value = 6)
labelF = Label(mainFrame, text = "Custom Resolution")
entryWidthF = Entry(mainFrame, textvariable = resolutionWidth,width = 5)
entryHeightF = Entry(mainFrame, textvariable = resolutionHeight,width = 5)
labelXF = Label(mainFrame, text = "x")


#select button
processButton = Button(mainFrame, text = "Process Image", command = process, width = 30)





radioA.grid(row = 1, column = 1, sticky = W)
labelA.grid(row = 1, column = 0, sticky = E)

radioB.grid(row = 2, column = 1, sticky = W)
labelB.grid(row = 2, column = 0, sticky = E)

radioC.grid(row = 1, column = 2,sticky = W)
labelC.grid(row = 1, column = 2, sticky = W,padx = 20)

radioD.grid(row = 2, column = 2, sticky = W)
labelD.grid(row = 2, column = 2, sticky = W, padx = 20)

radioE.grid(row = 3, column = 1, sticky = W)
labelE.grid(row = 3, column = 0, sticky = E)
entryWidthE.grid(row = 3, column = 2 ,sticky = W,padx = 0)
labelColonE.grid(row = 3, column = 2, sticky = W,padx = 35)
entryHeightE.grid(row = 3, column = 2, sticky = W, padx = 45)


radioF.grid(row = 4, column = 1, sticky = W)
labelF.grid(row = 4, column = 0, sticky = E)
entryWidthF.grid(row = 4, column = 2 ,sticky = W,padx = 0)
labelXF.grid(row = 4, column = 2, sticky = W,padx = 34)
entryHeightF.grid(row = 4, column = 2, sticky = W, padx = 45)

processButton.grid(row = 5, columnspan = 3,sticky = W)
mainFrame.grid()




root.mainloop()

