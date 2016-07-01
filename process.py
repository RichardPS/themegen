#PROCESS SITEMAP
# -*- coding: UTF-8 -*-
import re
from slugify import slugify

pageScript = []
topicList = []
currentTopic = ""
specialPages = {
	"kidParent":"Children",
	"kidName":"Kids' Zone",
	"newsParent":"News and Events",
	"newsName":"Latest News",
	"letterParent":"News and Events",
	"letterName":"Newsletters",
	"calendarParent":"Calendar",
	"calendarName":"News and Events",
	}

#init function
def sitemapProcess(sitemap,themename):
	#split sitemap to list
	sitemaparray = sitemap.split('\n')
	#remove blank items in list
	sitemaparray = filter(None, sitemaparray)
	#call function to generate theme name (no spaces or numbers)
	themeslug=slug_theme_name(themename)
	#call function to replace bullet points for ##
	sitemaparray = markPages(sitemaparray)
	#generate pagescript
	createPages(sitemaparray)
	#populate dictionary
	siteinfo = {
		'theme_name':themename,
		'theme_slug':themeslug,
		'site_map':sitemaparray,
		'page_script':pageScript,
		'specialPages':specialPages,
		}
	#return site info dictionary
	return siteinfo

#create theme name slug
def slug_theme_name(_themename):
	#remove all non alpha characters
	_themeslug = re.sub("[^a-zA-Z]","",_themename)
	return _themeslug

#find pages (bullet point) and mark with ##
def markPages(_sitemap):
	#replace bullet points for ##
	sitemap = [item.replace('•','##') for item in _sitemap]
	return sitemap

def createPages(_sitemaparray):
	global pageScript
	global currentTopic
	global topicList
	for item in _sitemaparray:		
		if item[:2] != '##':
			currentTopic = item.strip()
			topicList.extend([currentTopic])
		else:
			item = re.sub("^[(#\s)]{1,}","",item).strip()
			pageScript.extend([currentTopic+'\\'+slugify(currentTopic.strip(), to_lower=True)+'||'+processPage(item)])
	return pageScript

def processPage(input):
	global specialPages

	if "**kids" in input:
		specialPages["kidParent"] = currentTopic
		specialPages["kidName"] = input.replace("**kids","")
		input = input.replace("**kids","**/special/kidszone")
	elif "**news" in input:
		specialPages["newsParent"] = currentTopic
		specialPages["newsName"] = input.replace("**news","")
		input = input.replace("**news","**/stream/news/full/1/-//")
	elif "**letter" in input:
		specialPages["letterParent"] = currentTopic
		specialPages["letterName"] = input.replace("**letter","")
		input = input.replace("**letter","**/stream/newsletters/full/1/-//")
	elif "**calendar" in input:
		specialPages["calendarParent"] = currentTopic
		specialPages["calendarName"] = input.replace("**calendar","")
		input = input.replace("**calendar","**calendar_grid")
	elif "**diary" in input:
		specialPages["calendarParent"] = currentTopic
		specialPages["calendarName"] = input.replace("**diary","")
		input = input.replace("**diary","**/diary/list/")
	else:
		input = input
	return input