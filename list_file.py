import os
import glob

#get base dir name
dirpath = os.getcwd()

folders = []

#list files from dir
files = [f for f in glob.glob(dirpath + "**/*", recursive = True)]

for f in files:
    print(f)