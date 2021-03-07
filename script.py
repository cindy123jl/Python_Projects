import shutil
import os

#set where the source of the files are
source = '/Users/cindylara/Desktop/FolderA/'

#set the destination path to FolderB
destination = '/Users/cindylara/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
    #we are saying move the files by 'i' to their new destination
    shutil.move(source+i, destination)
