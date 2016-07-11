# process theme files
# -*- coding: UTF-8 -*-
import sys
import zipfile
import os
from datetime import datetime
from slugify import slugify

from conf import *

calendarweek = datetime.today().isocalendar()[1]

# read/edit/write theme files
def processtheme(topicnames,topicslugs,themeslug,specialpages,nursery):
    htmlpath = "orig/html/"
    csspath = "orig/css/"
    themepath = "themes/"
    htmlwritepath = "new/html/"
    csswritepath = "new/css/"
    newthemepath = "new/"
    # edit html files
    htmlnames = os.listdir(htmlpath)
    for file in htmlnames:
        with open(htmlpath+file,'r') as f:
            text = f.read()
        if file == 'core.homepage.html':
            text = text.replace(EXTENDS_BASE,'{% extends "' + themeslug + '/base.html" %}')
        elif file == 'base.html':
            text = text.replace(BASE_ABOUT_US,'##')
            text = text.replace(BASE_KEY_INFO,'')
            text = text.replace(BASE_NEWS_EVENTS,'')
            text = text.replace(BASE_PARENTS,'')
            text = text.replace(BASE_CHILDREN,'')
            # if nursery is true add nurserysite text
            text = text.replace(CORP_LINK, new_corp_link(nursery,calendarweek))
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += base_topic(topicslugs[i],topicnames[i])
                i = i + 1
            print newtopics
            text = text.replace('##',newtopics)
        elif file == 'calendar.grid.html' or file == 'diary.detail.html' \
            or file == 'diary.list.html':
            text = text.replace('Calendar',specialpages['calendarName'])
            text = text.replace(BREADCRUMB_NEWS_EVENTS,'    <li><a href="{% topic_url ' + slugify(specialpages['calendarParent'], to_lower=True) + ' %}">' + specialpages['calendarParent'] + '</a></li>')
            text = text.replace(EXTENDS_BASE,'{% extends "' + themeslug + '/base.html" %}')
        elif file == 'special.calendar-breadcrumbs.html':
            text = text.replace('Calendar',specialpages['calendarName'])
            text = text.replace(BREADCRUMB_NEWS_EVENTS,'<li><a href="{% topic_url ' + slugify(specialpages['calendarParent'], to_lower=True) + ' %}">' + specialpages['calendarParent'] + '</a></li>')
            text = text.replace(EXTENDS_BASE,'{% extends "'+themeslug+'/base.html" %}')
        elif file == 'news.aggregate-list.html' or file == 'news.detail.html':
            text = text.replace('Latest News',specialpages['newsName'])
            text = text.replace(BREADCRUMB_NEWS_EVENTS,'    <li><a href="{% topic_url ' + slugify(specialpages['newsParent'], to_lower=True) + ' %}">' + specialpages['newsParent'] + '</a></li>')
            text = text.replace('    <li><a href="{% activity_stream_url full news %}">Latest News</a></li>','    <li><a href="{% activity_stream_url full news %}">' + specialpages['newsName'] + '</a></li>')
            text = text.replace(EXTENDS_BASE,'{% extends "' + themeslug + '/base.html" %}')
        elif file == 'special.brain-builders.html' or file == 'special.english.html' \
            or file == 'special.games.html' or file == 'special.history.html' \
            or file == 'special.ks1-links.html' or file == 'special.ks2-links.html' \
            or file == 'special.maths.html' or file == 'special.science.html' \
            or file == 'special.kidszone.html':
            text = text.replace(BREADCRUMB_CHILDREN,'    <li><a href="{% topic_url ' + slugify(specialpages['kidParent'], to_lower=True) + ' %}">' + specialpages['kidParent'] + '</a></li>')
            text = text.replace('Kids\' Zone',specialpages['kidName'])
            text = text.replace(EXTENDS_BASE,'{% extends "' + themeslug + '/base.html" %}')
        elif file == 'special.sitemap.html':
            text = text.replace(SITEMAP_ABOUT_US,'##')
            text = text.replace(SITEMAP_KEY_INFO,'')
            text = text.replace(SITEMAP_NEWS_EVENTS,'')
            text = text.replace(SITEMAP_PARENTS,'')
            text = text.replace(SITEMAP_CHILDREN,'')
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += sitemap_topic(topicslugs[i])
                i = i + 1
            text = text.replace('##',newtopics)
            text = text.replace(EXTENDS_BASE,'{% extends "' + themeslug + '/base.html" %}')
        elif file == 'special.virtual-tour.html':
            text = text.replace(BREADCRUMB_ABOUT_US,'    <li><a href="{% topic_url ' + slugify(specialpages['tourParent'], to_lower=True) + ' %}">' + specialpages['tourParent'] + '</a></li>')
            text = text.replace('School Tour',specialpages['tourName'])
            text = text.replace(EXTENDS_BASE,'{% extends "' + themeslug + '/base.html" %}')
        else:
            text = text.replace(EXTENDS_BASE,'{% extends "' + themeslug + '/base.html" %}')
        with open(htmlwritepath+file,'w') as f:
            f.write(text)
    # edit css files
    cssnames = os.listdir(csspath)
    for file in cssnames:
        with open(csspath+file,'r') as f:
            text = f.read()
        if file == 'homepage.css':
            text = text.replace('.main-nav .ps_topic_slug_about-us {}\r\n','##')
            text = text.replace('.main-nav .ps_topic_slug_key-information {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_news-and-events {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_parents {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_children {}\r\n','')
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += '.main-nav .ps_topic_slug_' + topicslugs[i] + ' {}\r\n'
                i = i + 1
            text = text.replace('##',newtopics)
        elif file == 'style.css':
            # line 129
            text = text.replace('.main-nav .ps_topic_slug_about-us { background-position: 0 -52px; z-index: 199; }\r\n','##')
            text = text.replace('.main-nav .ps_topic_slug_key-information { background-position: 0 -104px; z-index: 198; }\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_news-and-events { background-position: 0 -156px; z-index: 197; }\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_parents { background-position: 0 -208px; z-index: 196; }\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_children { background-position: 0 -260px; z-index: 195; }\r\n','')
            newtopics = ''
            i = 0
            z = 199
            p = 52
            while i < len(topicslugs):
                newtopics += '.main-nav .ps_topic_slug_' + topicslugs[i] + ' { background-position: 0 -' + str(p) + 'px; z-index: ' + str(z) + '; }\r\n'
                i = i + 1
                z = z-1
                p = p + 52
            text = text.replace('##',newtopics)
            # line 136
            text = text.replace('.main-nav .ps_topic_slug_about-us:focus, .main-nav .ps_topic_slug_about-us:hover { background-position: right -52px; }\r\n','##')
            text = text.replace('.main-nav .ps_topic_slug_key-information:focus, .main-nav .ps_topic_slug_key-information:hover { background-position: right -104px; }\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_news-and-events:focus, .main-nav .ps_topic_slug_news-and-events:hover { background-position: right -156px; }\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_parents:focus, .main-nav .ps_topic_slug_parents:hover { background-position: right -208px; }\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_children:focus, .main-nav .ps_topic_slug_children:hover { background-position: right -260px; }\r\n','')
            newtopics = ''
            i = 0
            p = 52
            while i < len(topicslugs):
                newtopics += '.main-nav .ps_topic_slug_' + topicslugs[i] + ':focus, .main-nav .ps_topic_slug_' + topicslugs[i] + ':hover { background-position: right -' + str(p) + 'px; }\r\n'
                i = i + 1
                p = p + 52
            text = text.replace('##',newtopics)
            # line 204
            text = text.replace('.main-nav .ps_topic_slug_about-us ul {}\r\n','##')
            text = text.replace('.main-nav .ps_topic_slug_key-information ul {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_news-and-events ul {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_parents ul {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_children ul {}\r\n','')
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += '.main-nav .ps_topic_slug_' + topicslugs[i] + ' ul {}\r\n'
                i = i + 1
            text = text.replace('##',newtopics)
            # line 225
            text = text.replace('.main-nav .ps_topic_slug_about-us ul li a {}\r\n','##')
            text = text.replace('.main-nav .ps_topic_slug_key-information ul li a {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_news-and-events ul li a {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_parents ul li a {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_children ul li a {}\r\n','')
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += '.main-nav .ps_topic_slug_' + topicslugs[i] + ' ul li a {}\r\n'
                i = i + 1
            text = text.replace('##',newtopics)
            #line 241
            text = text.replace('.main-nav .ps_topic_slug_about-us ul li:focus, .main-nav .ps_topic_slug_about-us ul li:hover {}\r\n','##')
            text = text.replace('.main-nav .ps_topic_slug_key-information ul li:focus, .main-nav .ps_topic_slug_key-information ul li:hover {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_news-and-events ul li:focus, .main-nav .ps_topic_slug_news-and-events ul li:hover {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_parents ul li:focus, .main-nav .ps_topic_slug_parents ul li:hover {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_children ul li:focus, .main-nav .ps_topic_slug_children ul li:hover {}\r\n','')
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += '.main-nav .ps_topic_slug_' + topicslugs[i] + ' ul li:focus, .main-nav .ps_topic_slug_' + topicslugs[i] + ' ul li:hover {}\r\n'
                i = i + 1
            text = text.replace('##',newtopics)
            # line 249
            text = text.replace('.main-nav .ps_topic_slug_about-us ul a:focus, .main-nav .ps_topic_slug_about-us ul a:hover {}\r\n','##')
            text = text.replace('.main-nav .ps_topic_slug_key-information ul a:focus, .main-nav .ps_topic_slug_key-information ul a:hover {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_news-and-events ul li a:focus, .main-nav .ps_topic_slug_news-and-events ul li a:hover {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_parents ul li a:focus, .main-nav .ps_topic_slug_parents ul li a:hover {}\r\n','')
            text = text.replace('.main-nav .ps_topic_slug_children ul li a:focus, .main-nav .ps_topic_slug_children ul li a:hover {}\r\n','')
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += '.main-nav .ps_topic_slug_' + topicslugs[i] + ' ul a:focus, .main-nav .ps_topic_slug_' + topicslugs[i] + ' ul a:hover {}\r\n'
                i = i + 1
            text = text.replace('##',newtopics)
        else:
            text = text
        with open(csswritepath+file,'w') as f:
            f.write(text)

    # zip up theme, currently has root folder :(
    ziptheme(themeslug)

    # return theme zip name for download
    zipname = themeslug + ".zip"
    return zipname

def ziptheme(themename):

    newthemedirs = os.listdir('new')

    themeZip = zipfile.ZipFile('static/themezips/' + themename + '.zip','w')

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
                    arcname=os.path.join(os.path.relpath(foldername, os.path.dirname(folder)), filename))
    themeZip.close()