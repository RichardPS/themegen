# process theme files
# -*- coding: UTF-8 -*-
import os, sys, zipfile

htmlFiles = []
cssFiles = []

def processTheme(topicNames,topicSlugs,themeslug):
	htmlPath = "orig/html/"
	cssPath = "orig/css/"
	htmlWritePath = "new/html/"
	htmlNames = os.listdir(htmlPath)
	for file in htmlNames:
		fileContents = open(htmlPath+file,'r')
		wf = open(htmlWritePath+file,'w')
		for line in fileContents:
			if file == "core.homepage.html":
				wf.write(line.replace('{% extends "Richard/base.html" %}','{% extends "HomePage/base.html" %}'))
			else:
				wf.write(line.replace('{% extends "Richard/base.html" %}','{% extends "'+themeslug+'/base.html" %}'))
		fileContents.close()
		wf.close()
	zipName = "MyTheme.zip"
	return zipName