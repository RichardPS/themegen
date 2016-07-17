''' process theme files '''
# -*- coding: UTF-8 -*-
import sys
import zipfile
import os
from datetime import datetime
from slugify import slugify

from edittheme_inc import *

calendarweek = datetime.today().isocalendar()[1]

''' read/edit/write theme files '''
def processtheme(topicnames,topicslugs,themeslug,specialpages,nursery):
    htmlpath = "sourcefiles/orig/html/"
    csspath = "sourcefiles/orig/css/"
    themepath = "themes/"
    htmlwritepath = "sourcefiles/new/html/"
    csswritepath = "sourcefiles/new/css/"
    newthemepath = "sourcefiles/new/"

    print topicnames
    print topicslugs

    # edit html files
    htmlnames = os.listdir(htmlpath)
    ''' loop through all html files and edit as required '''
    for file in htmlnames:
        with open(htmlpath+file,'r') as f:
            text = f.read()
            ''' remove windows charage return '''
            text = text.replace('\r\n', '\n')
        if file == 'core.homepage.html':
            ''' changes to core.homepahe.html '''
            text = text.replace(EXTENDS_BASE, extends_theme(themeslug))
        elif file == 'base.html':
            ''' changes to base.html '''
            ''' remove default topics '''
            text = text.replace(BASE_ABOUT_US, '##')
            text = text.replace(BASE_KEY_INFO, '')
            text = text.replace(BASE_NEWS_EVENTS, '')
            text = text.replace(BASE_PARENTS, '')
            text = text.replace(BASE_CHILDREN, '')
            ''' replace corp link '''
            text = text.replace(CORP_LINK, new_corp_link(nursery,calendarweek))
            ''' write new topics '''
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += base_topic(topicslugs[i], topicnames[i])
                i = i + 1
            print newtopics
            text = text.replace('##',newtopics)
        elif file in CALENDARPAGES:
            ''' changes to calendar/dairy pages '''
            text = text.replace('Calendar', specialpages['calendarname'])
            text = text.replace(BREADCRUMB_NEWS_EVENTS, \
                topic_breadcrumb(specialpages['calendarparent']))
            text = text.replace(EXTENDS_BASE, extends_theme(themeslug))
        elif file == 'special.calendar-breadcrumbs.html':
            ''' changes to special.calendar-breadcrumbs.html '''
            text = text.replace('Calendar', specialpages['calendarname'])
            text = text.replace(BREADCRUMB_NEWS_EVENTS, \
                topic_breadcrumb(specialpages['calendarparent']))
            text = text.replace(EXTENDS_BASE, extends_theme(themeslug))
        elif file == 'news.aggregate-list.html' or file == 'news.detail.html':
            ''' changes to news pages '''
            text = text.replace('Latest News', specialpages['newsname'])
            text = text.replace(BREADCRUMB_NEWS_EVENTS, \
                topic_breadcrumb(specialpages['newsparent']))
            text = text.replace('Latest News', specialpages['newsname'])
            text = text.replace(EXTENDS_BASE, extends_theme(themeslug))
        elif file in KIDSZONEPAGES:
            ''' changes to kidszone pages '''
            text = text.replace(BREADCRUMB_CHILDREN, \
                topic_breadcrumb(specialpages['kidparent']))
            text = text.replace('Kids\' Zone', specialpages['kidname'])
            text = text.replace(EXTENDS_BASE, extends_theme(themeslug))
        elif file == 'special.sitemap.html':
            ''' changes to special.sitemap.html page '''
            ''' remove default topics '''
            text = text.replace(SITEMAP_ABOUT_US, '##')
            text = text.replace(SITEMAP_KEY_INFO, '')
            text = text.replace(SITEMAP_NEWS_EVENTS, '')
            text = text.replace(SITEMAP_PARENTS, '')
            text = text.replace(SITEMAP_CHILDREN, '')
            ''' write new topics '''
            newslugs = ''
            i = 0
            while i < len(topicslugs):
                newslugs += sitemap_topic(topicslugs[i])
                i = i + 1
            text = text.replace('##', newslugs)
            text = text.replace(EXTENDS_BASE, extends_theme(themeslug))
        elif file == 'special.virtual-tour.html':
            ''' changes to special.virtual-tour.html '''
            text = text.replace(BREADCRUMB_ABOUT_US, \
                tour_breadcrumb(specialpages['tourparent']))
            text = text.replace('School Tour', specialpages['tourname'])
            text = text.replace(EXTENDS_BASE, extends_theme(themeslug))
        elif file == 'newsletters.aggregate-list.html':
            ''' changes to newsletters.aggregate-list.html '''
            text = text.replace(BREADCRUMB_NEWS_EVENTS, \
                topic_breadcrumb(specialpages['letterparent']))
            text = text.replace('Newsletters', specialpages['lettername'])
            text = text.replace(EXTENDS_BASE, extends_theme(themeslug))
        else:
            ''' replace template name in all other files '''
            text = text.replace(EXTENDS_BASE, extends_theme(themeslug))
        ''' write edited template to files '''
        with open(htmlwritepath+file,'w') as f:
            f.write(text)
    ''' edit css files '''
    cssnames = os.listdir(csspath)
    ''' loop through css files '''
    for file in cssnames:
        with open(csspath+file,'r') as f:
            text = f.read()
            ''' remove windows charage return '''
            text = text.replace('\r\n', '\n')
        if file == 'homepage.css':
            ''' changes to homepage.css '''
            text = text.replace(HOME_ABOUT_US, '##')
            text = text.replace(HOME_KEY_INFO, '')
            text = text.replace(HOME_NEW_EVENTS, '')
            text = text.replace(HOME_PARENTS, '')
            text = text.replace(HOME_CHILDREN, '')
            ''' add new topic styles '''
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += homecss(topicslugs[i])
                i = i + 1
            text = text.replace('##', newtopics)
        elif file == 'style.css':
            ''' changes to style.css '''
            ''' remove default rules line 129 '''
            text = text.replace(STYLE129_ABOUT_US, '##')
            text = text.replace(STYLE129_KEY_INFO, '')
            text = text.replace(STYLE129_NEW_EVENTS, '')
            text = text.replace(STYLE129_PARENTS, '')
            text = text.replace(STYLE129_CHILDREN, '')
            ''' generate new rules for add to file '''
            newtopics = ''
            i = 0
            z = 199
            p = 52
            while i < len(topicslugs):
                newtopics += style129(topicslugs[i], p, z)
                i = i + 1
                z = z-1
                p = p + 52
            text = text.replace('##', newtopics)
            ''' remove default rules  line 136 '''
            text = text.replace(STYLE136_ABOUT_US, '##')
            text = text.replace(STYLE136_KEY_INFO, '')
            text = text.replace(STYLE136_NEW_EVENTS, '')
            text = text.replace(STYLE136_PARENTS, '')
            text = text.replace(STYLE136_CHILDREN, '')
            ''' generate new rules for add to file '''
            newtopics = ''
            i = 0
            p = 52
            while i < len(topicslugs):
                newtopics += style136(topicslugs[i], p)
                i = i + 1
                p = p + 52
            text = text.replace('##', newtopics)
            ''' remove default rules  line 204 '''
            text = text.replace(STYLE204_ABOUT_US, '##')
            text = text.replace(STYLE204_KEY_INFO, '')
            text = text.replace(STYLE204_NEW_EVENTS, '')
            text = text.replace(STYLE204_PARENTS, '')
            text = text.replace(STYLE204_CHILDREN, '')
            ''' generate new rules for add to file '''
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += style204(topicslugs[i])
                i = i + 1
            text = text.replace('##',newtopics)
            ''' remove default rules  line 225 '''
            text = text.replace(STYLE225_ABOUT_US, '##')
            text = text.replace(STYLE225_KEY_INFO, '')
            text = text.replace(STYLE225_NEW_EVENTS, '')
            text = text.replace(STYLE225_PARENTS, '')
            text = text.replace(STYLE225_CHILDREN, '')
            ''' generate new rules for add to file '''
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += style225(topicslugs[i])
                i = i + 1
            text = text.replace('##', newtopics)
            ''' remove default rules line 241 '''
            text = text.replace(STYLE241_ABOUT_US, '##')
            text = text.replace(STYLE241_KEY_INFO, '')
            text = text.replace(STYLE241_NEW_EVENTS, '')
            text = text.replace(STYLE241_PARENTS, '')
            text = text.replace(STYLE241_CHILDREN, '')
            ''' generate new rules for add to file '''
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += style241(topicslugs[i])
                i = i + 1
            text = text.replace('##',newtopics)
            ''' remove default rules line 249 '''
            text = text.replace(STYLE249_ABOUT_US, '##')
            text = text.replace(STYLE249_KEY_INFO, '')
            text = text.replace(STYLE249_NEW_EVENTS, '')
            text = text.replace(STYLE249_PARENTS, '')
            text = text.replace(STYLE249_CHILDREN, '')
            ''' generate new rules for add to file '''
            newtopics = ''
            i = 0
            while i < len(topicslugs):
                newtopics += style249(topicslugs[i])
                i = i + 1
            text = text.replace('##',newtopics)
        else:
            text = text
        with open(csswritepath+file,'w') as f:
            f.write(text)

    ''' zip up theme, currently has root folder '''
    ziptheme(themeslug)

    ''' return theme zip name for download '''
    zipname = themeslug + ".zip"
    return zipname

def ziptheme(themename):
    newthemedirs = os.listdir('sourcefiles/new')
    themeZip = zipfile.ZipFile('static/themezips/{0}.zip','w').format(themename)
    for item in newthemedirs:
        folder = 'sourcefiles/new/{0}/'.format(item)
        folder = os.path.relpath(folder)
        for foldername, subfolders, filenames in os.walk(folder):
            ''' Add the current folder to the ZIP file if not root folder '''
            if foldername != folder:
                themeZip.write(foldername,
                    arcname=os.path.relpath(foldername, os.path.dirname(folder)))
            ''' Add all the files in this folder to the ZIP file. '''
            for filename in filenames:
                themeZip.write(os.path.join(foldername, filename),
                    arcname=os.path.join(os.path.relpath(foldername, \
                            os.path.dirname(folder)), filename))
    themeZip.close()