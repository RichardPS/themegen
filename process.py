#PROCESS SITEMAP
# -*- coding: UTF-8 -*-
import re
from slugify import slugify
from edittheme import processtheme

# declare global variables
pageScript = []
topicNames = []
topicSlugs =[]
currentTopic = ""
specialPages = {
	"kidParent":"Children",
	"kidName":"Kids' Zone",
	"newsParent":"News and Events",
	"newsName":"Latest News",
	"letterParent":"News and Events",
	"letterName":"Newsletters",
	"calendarParent":"News and Events",
	"calendarName":"Calendar",
	}

# init function
def sitemapProcess(sitemap,themename,nursery):
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
	# call edit theme function in editTheme.py
	zipName = processtheme(topicNames,topicSlugs,themeslug,specialPages,nursery)
	#populate dictionary
	siteinfo = {
		'theme_name':themename,
		'theme_slug':themeslug,
		'site_map':sitemaparray,
		'page_script':pageScript,
		'specialPages':specialPages,
		'topicNames':topicNames,
		'topicSlugs':topicSlugs,
		'zipName':zipName,
		'nursery':nursery,
		}
	#return site info dictionary
	return siteinfo

# create theme name slug
def slug_theme_name(themename):
	#remove all non alpha characters
	themeslug = re.sub("[^a-zA-Z]","",themename)
	return themeslug

# find pages (bullet point) and mark with ##, these are pages in a topic
def markPages(sitemap):
	#replace bullet points for ##
	markedsitemap = [item.replace('•','##') for item in sitemap]
	return markedsitemap

# loop thgouh sitemap and id topics/pages
def createPages(sitemaparray):
	global pageScript
	global currentTopic
	global topicList
	global topicNames
	global topicSlugs
	for item in sitemaparray:		
		if item[:2] != '##':
			currentTopic = item.strip()
			topicNames.extend([currentTopic])
			topicSlugs.extend([slugify(currentTopic, to_lower=True)])
		else:
			item = re.sub("^[(#\s)]{1,}","",item).strip()
			pageScript.extend([currentTopic+'\\'+slugify(currentTopic, to_lower=True)+'||'+processPage(item)])
	return pageScript

# add elements to special pages for sitemap
def processPage(pageshims):
	global specialPages
	if "**kids" in pageshims:
		specialPages["kidParent"] = currentTopic
		specialPages["kidName"] = pageshims.replace("**kids","")
		pageshims = pageshims.replace("**kids","**/special/kidszone")
	elif "**news" in pageshims:
		specialPages["newsParent"] = currentTopic
		specialPages["newsName"] = pageshims.replace("**news","")
		pageshims = pageshims.replace("**news","**/stream/news/full/1/-//")
	elif "**letter" in pageshims:
		specialPages["letterParent"] = currentTopic
		specialPages["letterName"] = pageshims.replace("**letter","")
		pageshims = pageshims.replace("**letter","**/stream/newsletters/full/1/-//")
	elif "**calendar" in pageshims:
		specialPages["calendarParent"] = currentTopic
		specialPages["calendarName"] = pageshims.replace("**calendar","")
		pageshims = pageshims.replace("**calendar","**calendar_grid")
	elif "**diary" in pageshims:
		specialPages["calendarParent"] = currentTopic
		specialPages["calendarName"] = pageshims.replace("**diary","")
		pageshims = pageshims.replace("**diary","**/diary/list/")
	else:
		pageshims = pageshims
	return pageshims