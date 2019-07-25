import os
import glob
import re

#get base dir name
dirpath = os.getcwd()

folders = []
extensions = []

#list files from dir
files = [f for f in glob.glob(dirpath + "**/*", recursive = True)]

#list file extensions
for f in files: 
    aux = f.split('.', 1)
    
    #this means it is a file not a folder, and if the folder do not exists
    if(len(aux) > 1 and not os.path.exists(aux[1])): 
        os.mkdir(aux[1])