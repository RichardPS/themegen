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
DBS = '\\'
DP = '||'

def sitemapprocess(sitemap, themename, nursery):
    ''' create new SiteInfo instance '''
    siteinfo = SiteInfo(nursery)
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
    ''' call edit theme function and create zip '''
    zipname = processtheme(
        siteinfo.topicnames,
        siteinfo.topicslugs,
        siteinfo.themeslug,
        siteinfo.specialpages,
        siteinfo.nursery,
        )
    ''' return required site info to page '''
    sitedict = {
        'theme_name': siteinfo.themeslug,
        'page_script': siteinfo.pagescript,
        'zipname': siteinfo.themeslug,
    }
    return sitedict

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
            siteinfo.set_currenttopic(item.strip())
            siteinfo.ext_topicnames(siteinfo.currenttopic)
            siteinfo.ext_topicslugs(slugify(
                siteinfo.currenttopic, to_lower=True))
        else:
            item = re.sub("^[(#\s)]{1,}","",item).strip()
            siteinfo = processpage(item, siteinfo)
    return siteinfo

# add elements to special pages for sitemap
def processpage(pageshims, siteinfo):
    siteinfo = siteinfo
    if '**kids' in pageshims:
        siteinfo.set_kp(siteinfo.currenttopic)
        siteinfo.set_kn(pageshims.replace('**kids',''))
        page = pageshims.replace('**kids', KIDSZONE_SHIM)
        currenttopic = slugify(siteinfo.currenttopic, to_lower=True)
        siteinfo.ext_pagescript('{0}{1}{2}{3}{4}'.format(
            siteinfo.currenttopic, DBS, currenttopic, DP, page))
    elif '**news' in pageshims:
        siteinfo.set_np(siteinfo.currenttopic)
        siteinfo.set_nn(pageshims.replace('**news',''))
        page = pageshims.replace('**news', NEWS_SHIM)
        currenttopic = slugify(siteinfo.currenttopic, to_lower=True)
        siteinfo.ext_pagescript('{0}{1}{2}{3}{4}'.format(
            siteinfo.currenttopic, DBS, currenttopic, DP, page))
    elif '**letter' in pageshims:
        siteinfo.set_lp(siteinfo.currenttopic)
        siteinfo.set_ln(pageshims.replace('**letter',''))
        page = pageshims.replace('**letter', LETTER_SHIM)
        currenttopic = slugify(siteinfo.currenttopic, to_lower=True)
        siteinfo.ext_pagescript('{0}{1}{2}{3}{4}'.format(
            siteinfo.currenttopic, DBS, currenttopic, DP, page))
    elif '**calendar' in pageshims:
        siteinfo.set_cp(siteinfo.currenttopic)
        siteinfo.set_cn(pageshims.replace('**calendar',''))
        page = pageshims.replace('**calendar', CALENDAR_SHIM)
        currenttopic = slugify(siteinfo.currenttopic, to_lower=True)
        siteinfo.ext_pagescript('{0}{1}{2}{3}{4}'.format(
            siteinfo.currenttopic, DBS, currenttopic, DP, page))
    elif '**diary' in pageshims:
        siteinfo.set_cp(siteinfo.currenttopic)
        siteinfo.set_cn(pageshims.replace('**diary',''))
        page = pageshims.replace('**diary', DIARY_SHIM)
        currenttopic = slugify(siteinfo.currenttopic, to_lower=True)
        siteinfo.ext_pagescript('{0}{1}{2}{3}{4}'.format(
            siteinfo.currenttopic, DBS, currenttopic, DP, page))
    elif '**tour' in pageshims:
        siteinfo.set_tp(siteinfo.currenttopic)
        siteinfo.set_tn(pageshims.replace('**tour',''))
        page = pageshims.replace('**tour', TOUR_SHIM)
        currenttopic = slugify(siteinfo.currenttopic, to_lower=True)
        siteinfo.ext_pagescript('{0}{1}{2}{3}{4}'.format(
            siteinfo.currenttopic, DBS, currenttopic, DP, page))
    else:
        page = pageshims
        currenttopic = slugify(siteinfo.currenttopic, to_lower=True)
        siteinfo.ext_pagescript('{0}{1}{2}{3}{4}'.format(
            siteinfo.currenttopic, DBS, currenttopic, DP, page))
    return siteinfo