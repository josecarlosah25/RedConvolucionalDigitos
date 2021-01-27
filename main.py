import eel
import math
from tkinter import *
from tkinter import filedialog 
from numtel import test 
from cnndir import getNumbers

@eel.expose
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("PNG", 
                                                        "*.png*"), 
                                                       ("All Files", 
                                                        "*.*"))) 
    return filename

def browseDirectory(): 
    dirPath = filedialog.askdirectory() 
    return dirPath

eel.init('web')

@eel.expose
def getData(option):
    if(option==1):
        filepath=browseFiles()
        return test(filepath)
    else:
        dirPath=browseDirectory()
        return getNumbers(dirPath)


 


eel.start('index.html', size=(1280, 669))

