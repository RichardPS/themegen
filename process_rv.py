# PROCESS SITEMAP
# -*- coding: UTF-8 -*-
import re
from slugify import slugify
from edittheme import processtheme
from process_inc import SiteInfo

KIDSZONE_SHIM = '**/special/kidszone'
NEWS_SHIM = '**/stream/news/full/1/-//'
LETTER_SHIM = '**/stream/newsletters/full/1/-//'
CALENDAR_SHIM = '**calendar_grid'
DIARY_SHIM = '**/diary/list/'
TOUR_SHIM = '**/special/virtual-tour'

def sitemapprocess(sitemap, themename, nursery):
    ''' create new SiteInfo instance '''
    siteinfo = SiteInfo()
    ''' split sitemap into list '''
    sitemaparray = sitemap.split('\n')
    ''' remove blank items in list '''
    sitemaparray = filter(None, sitemaparray)
    ''' call mark page function and push sitemaparray to instance '''
    siteinfo.set_sitemaparray(markpages(sitemaparray))
    ''' set themename '''
    siteinfo.set_themeslug(slugthemename(themename))
    ''' generate pagescript in SiteInfo instance '''
    siteinfo = createpages(siteinfo)

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
def createpages(siteinfo):
    siteinfo = siteinfo
    sitemaparray = siteinfo.sitemaparray
    for item in sitemaparray:       
        if item[:2] != '##':
            siteinfo.set_currenttopic = item.strip()
            siteinfo.ext_topicnames.extend([siteinfo.currenttopic])
            siteinfo.ext_topicslugs.extend([slugify(
                siteinfo.currenttopic, to_lower=True)])
        else:
            item = re.sub("^[(#\s)]{1,}","",item).strip()
            siteinfo.ext_pagescript.extend(
                [siteinfo.currenttopic + '\\' + slugify(siteinfo.currenttopic, \
                to_lower=True) + '||' + processpage(item, siteinfo)])
    return siteinfo

# add elements to special pages for sitemap
def processpage(pageshims, siteinfo):
    siteinfo = siteinfo
    if '**kids' in pageshims:
        siteinfo.set_kp(siteinfo.currenttopic)
        siteingo.set_kn(pageshims.replace('**kids',''))
        siteinfo.ext_pagescript(pageshims.replace('**kids', KIDSZONE_SHIM))
    elif '**news' in pageshims:
        siteinfo.set_np(siteinfo.currenttopic)
        siteinfo.set_nn(pageshims.replace('**news',''))
        siteinfo.ext_pagescript(pageshims.replace('**news', NEWS_SHIM))
    elif '**letter' in pageshims:
        siteinfo.set_lp(siteinfo.currenttopic)
        siteinfo.set_ln(pageshims.replace('**letter',''))
        siteinfo.ext_pagescript(pageshims.replace('**letter', LETTER_SHIM))
    elif '**calendar' in pageshims:
        specialpages['calendarParent'] = currenttopic
        specialpages['calendarName'] = pageshims.replace('**calendar','')
        pageshims = pageshims.replace('**calendar','**calendar_grid')
    elif '**diary' in pageshims:
        specialpages['calendarParent'] = currenttopic
        specialpages['calendarName'] = pageshims.replace('**diary','')
        pageshims = pageshims.replace('**diary','**/diary/list/')
    elif '**tour' in pageshims:
        specialpages['tourParent'] = currenttopic
        specialpages['tourName'] = pageshims.replace('**tour','')
        pageshims = pageshims.replace('**tour','**/special/virtual-tour')
    else:
        pageshims = pageshims
    return siteinfo