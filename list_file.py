import os, shutil
import glob
import re
from pathlib import Path

#get base dir name
dirpath = os.getcwd()

folders = []
extensions = []

#list files from dir
files = [f for f in os.listdir('.') if os.path.isfile(f)]

#list files by their extensions
for f in files: 
    aux = f.split('.', 1)
    
    #this means it is a file not a folder, and if the folder do not exists
    if(f != "list_file.py" and len(aux) > 1): #preventing creation only by the script extension
        if(not os.path.exists(aux[1])): 
            os.mkdir(aux[1])
        
        shutil.move(dirpath + "/" + f, dirpath + "/" + aux[1] + "/" + f)
        
        
