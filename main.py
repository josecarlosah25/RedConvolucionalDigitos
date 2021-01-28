import eel
import os.path
import math
import shutil
from tkinter import *
from tkinter import filedialog 
from numtel import test 
from cnndir import getNumbers

@eel.expose
def browseFiles(): 
    root = Tk();
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("PNG", 
                                                        "*.png*"), 
                                                       ("All Files", 
                                                        "*.*"))) 
    root.destroy()
    return filename

def browseDirectory(): 
    root = Tk();
    dirPath = filedialog.askdirectory() 
    root.destroy()
    return dirPath

eel.init('web')

@eel.expose
def getData(option):
    if(option==1):
        filepath=browseFiles()
        str1=test(filepath)
        str1=filepath+','+str1
        return str1
    else:
        dirPath=browseDirectory()
        return getNumbers(dirPath)


eel.start('index.html', size=(1280, 669))

