#PROCESS SITEMAP
# -*- coding: UTF-8 -*-
import re
from slugify import slugify
from edittheme import processtheme

# declare global variables
pagescript = []
topicnames = []
topicslugs =[]
currenttopic = ""
specialpages = {
    "kidParent":"Children",
    "kidName":"Kids' Zone",
    "newsParent":"News and Events",
    "newsName":"Latest News",
    "letterParent":"News and Events",
    "letterName":"Newsletters",
    "calendarParent":"News and Events",
    "calendarName":"Calendar",
    "tourParent":"About Us",
    "tourName":"School Tour",
    }

# init function
def sitemapprocess(sitemap,themename,nursery):
    # clear pagescript list if page resubmitted
    global pagescript
    global topicslugs
    global topicnames
    # clear global variables
    topicslugs = []
    topicnames = []
    pagescript = []
    #split sitemap to list
    sitemaparray = sitemap.split('\n')
    #remove blank items in list
    sitemaparray = filter(None, sitemaparray)
    #call function to generate theme name (no spaces or numbers)
    themeslug = slugthemename(themename)
    #call function to replace bullet points for ##
    sitemaparray = markpages(sitemaparray)
    #generate pagescript
    createpages(sitemaparray)
    # call edit theme function in editTheme.py
    zipName = processtheme(topicnames, topicslugs,
        themeslug, specialpages, nursery)
    #populate dictionary with test variables
    '''siteinfo = {
        'theme_name':themename,
        'theme_slug':themeslug,
        'site_map':sitemaparray,
        'page_script':pagescript,
        'specialpages':specialpages,
        'topicnames':topicnames,
        'topicslugs':topicslugs,
        'zipName':zipName,
        'nursery':nursery,
        }'''
    # populate dictionary for live env
    siteinfo = {
        'theme_name':themename,
        'page_script':pagescript,
        'zipName':zipName,
    }
    #return site info dictionary
    return siteinfo

# create theme name slug
def slugthemename(themename):
    #remove all non alpha characters
    themeslug = re.sub("[^a-zA-Z]","",themename)
    return themeslug

# find pages (bullet point) and mark with ##, these are pages in a topic
def markpages(sitemap):
    #replace bullet points for ##
    markedsitemap = [item.replace('•','##') for item in sitemap]
    return markedsitemap

# loop thgouh sitemap and id topics/pages
def createpages(sitemaparray):
    global pagescript
    global currenttopic
    global topicList
    global topicnames
    global topicslugs
    for item in sitemaparray:       
        if item[:2] != '##':
            currenttopic = item.strip()
            topicnames.extend([currenttopic])
            topicslugs.extend([slugify(currenttopic, to_lower=True)])
        else:
            item = re.sub("^[(#\s)]{1,}","",item).strip()
            pagescript.extend([currenttopic + '\\' + slugify(currenttopic, \
                to_lower=True) + '||' + processpage(item)])
    return pagescript

# add elements to special pages for sitemap
def processpage(pageshims):
    global specialpages
    if "**kids" in pageshims:
        specialpages["kidParent"] = currenttopic
        specialpages["kidName"] = pageshims.replace("**kids","")
        pageshims = pageshims.replace("**kids","**/special/kidszone")
    elif "**news" in pageshims:
        specialpages["newsParent"] = currenttopic
        specialpages["newsName"] = pageshims.replace("**news","")
        pageshims = pageshims.replace("**news","**/stream/news/full/1/-//")
    elif "**letter" in pageshims:
        specialpages["letterParent"] = currenttopic
        specialpages["letterName"] = pageshims.replace("**letter","")
        pageshims = pageshims.replace("**letter","**/stream/newsletters/full/1/-//")
    elif "**calendar" in pageshims:
        specialpages["calendarParent"] = currenttopic
        specialpages["calendarName"] = pageshims.replace("**calendar","")
        pageshims = pageshims.replace("**calendar","**calendar_grid")
    elif "**diary" in pageshims:
        specialpages["calendarParent"] = currenttopic
        specialpages["calendarName"] = pageshims.replace("**diary","")
        pageshims = pageshims.replace("**diary","**/diary/list/")
    elif "**tour" in pageshims:
        specialpages["tourParent"] = currenttopic
        specialpages["tourName"] = pageshims.replace("**tour","")
        pageshims = pageshims.replace("**tour","**/special/virtual-tour")
    else:
        pageshims = pageshims
    return pageshims