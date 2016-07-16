# build generic template
import sys
import zipfile
import os

def buildgeneric():
    themeName = 'BuildTemplate'
    newthemedirs = os.listdir('sourcefiles/new')

    themeZip = zipfile.ZipFile('static/themezips/' + themeName + '.zip','w')

    for item in newthemedirs:
        #print item
        folder = 'new/' + item + '/'

        folder = os.path.relpath(folder)

        for foldername, subfolders, filenames in os.walk(folder):
            # Add the current folder to the ZIP file if not root folder
            if foldername != folder:
                themeZip.write(foldername,
                    arcname=os.path.relpath(foldername, os.path.dirname(folder)))
            # Add all the files in this folder to the ZIP file.
            for filename in filenames:
                themeZip.write(os.path.join(foldername, filename),
                    arcname=os.path.join(os.path.relpath(foldername,
                    os.path.dirname(folder)), filename))
    themeZip.close()