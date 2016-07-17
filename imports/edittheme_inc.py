from slugify import slugify
''' define constants for html '''
'''SEO TEXT PRIMARY'''
SEOPRIMARY = [
    "Designed by PrimarySite",
    "Design by PrimarySite",
    "Website by PrimarySite",
    "Web Site by PrimarySite",
    "Web Design by PrimarySite",
    "Website Design by PrimarySite",
    "Website Designed by PrimarySite",
    "Web Site Design by PrimarySite",
    "Web Site Designed by PrimarySite",
    "Websites for schools by PrimarySite",
    "Websites for primary schools by PrimarySite",
    "Primary School Websites by PrimarySite",
    "Websites for Primary Schools by PrimarySite",
    "PrimarySite School Website Design",
    "A PrimarySite School Website",
    "A PrimarySite School Website Design",
    "A PrimarySite School Web Site",
    "A PrimarySite School Web Site Design",
    "Unique Websites for schools by PrimarySite",
    "Unique Websites for Unique Schools by PrimarySite",
    "Created by PrimarySite",
    "Created by PrimarySite, school website designers",
    "Created by PrimarySite, primary school website designers",
    "PrimarySite Website Design",
    "PrimarySite Web Design",
    "School Website by PrimarySite",
    "School Website from PrimarySite",
    "School Website Design by PrimarySite",
    "School Website Designed by PrimarySite",
    "PrimarySite - Websites for Schools",
    "PrimarySite - Websites for Primary Schools",
    "PrimarySite - School Website Designers",
    "PrimarySite - the School Website Specialists",
    "PrimarySite - School Websites",
    "PrimarySite - Websites for Schools",
    "PrimarySite - Websites for Primary Schools ",
    "PrimarySite - School Web Site Designers",
    "PrimarySite - the School Web Site Specialists",
    "PrimarySite - School Web Sites",
    "PrimarySite - Web Sites for Schools",
    "PrimarySite - Web Sites for Primary Schools",
    "PrimarySite - Outstanding School Websites",
    "PrimarySite - Outstanding School Web Sites",
    "Web Site by PrimarySite",
    "Web Site Design by PrimarySite",
    "Primary School Websites by PrimarySite",
    "A PrimarySite School Website Design",
    "Unique Websites for Unique Schools by PrimarySite",
    "PrimarySite Website Design",
    "School Website Design by PrimarySite",
    "PrimarySite - School Website Designers",
    "PrimarySite - Websites for Primary Schools",
    "Created by PrimarySite",
    "PrimarySite Website Design",
]
'''SEO TEXT NURSERY'''
SEONURSERY = [
    "Designed by NurserySite",
    "Design by NurserySite",
    "Website by NurserySite",
    "Web Site by NurserySite",
    "Web Design by NurserySite",
    "Website Design by NurserySite",
    "Website Designed by NurserySite",
    "Web Site Design by NurserySite",
    "Web Site Designed by NurserySite",
    "Websites for schools by NurserySite",
    "Websites for primary schools by NurserySite",
    "Nursery School Websites by NurserySite",
    "Websites for Nursery Schools by NurserySite",
    "NurserySite School Website Design",
    "A NurserySite School Website",
    "A NurserySite School Website Design",
    "A NurserySite School Web Site",
    "A NurserySite School Web Site Design",
    "Unique Websites for schools by NurserySite",
    "Unique Websites for Unique Schools by NurserySite",
    "Created by NurserySite",
    "Created by NurserySite, school website designers",
    "Created by NurserySite, Nursery school website designers",
    "NurserySite Website Design",
    "NurserySite Web Design",
    "School Website by NurserySite",
    "School Website from NurserySite",
    "School Website Design by NurserySite",
    "School Website Designed by NurserySite",
    "NurserySite - Websites for Schools",
    "NurserySite - Websites for Nursery Schools",
    "NurserySite - School Website Designers",
    "NurserySite - the School Website Specialists",
    "NurserySite - School Websites",
    "NurserySite - Websites for Schools",
    "NurserySite - Websites for Nursery Schools ",
    "NurserySite - School Web Site Designers",
    "NurserySite - the School Web Site Specialists",
    "NurserySite - School Web Sites",
    "NurserySite - Web Sites for Schools",
    "NurserySite - Web Sites for Nursery Schools",
    "NurserySite - Outstanding School Websites",
    "NurserySite - Outstanding School Web Sites",
    "Web Site by NurserySite",
    "Web Site Design by NurserySite",
    "Nursery School Websites by NurserySite",
    "A NurserySite School Website Design",
    "Unique Websites for Unique Schools by NurserySite",
    "NurserySite Website Design",
    "School Website Design by NurserySite",
    "NurserySite - School Website Designers",
    "NurserySite - Websites for Nursery Schools",
    "Created by NurserySite",
    "NurserySite Website Design",
]
'''CORP LINK'''
CORP_LINK = '<li><a href="http://primarysite.net">Website design by PrimarySite'
NURSERY_URL = 'http://www.nurserysite.co.uk/'
PRIMARY_URL = 'http://primarysite.net/'

'''extends base.html'''
EXTENDS_BASE = '{% extends "BuildTemplate/base.html" %}'

'''BASE.HTML REPLACE STRINGS'''
SPACE24 = ''.rjust(24)
SPACE12 = ''.rjust(12)

BASE_ABOUT_US = '{0}{{% topic_menu_full about-us "About Us" %}}\n'.format(SPACE24)
BASE_KEY_INFO = '{0}{{% topic_menu_full key-information "Key Information" %}}\n'.format(SPACE24)
BASE_NEWS_EVENTS = '{0}{{% topic_menu_full news-and-events "News and Events" %}}\n'.format(SPACE24)
BASE_PARENTS = '{0}{{% topic_menu_full parents "Parents" %}}\n'.format(SPACE24)
BASE_CHILDREN = '{0}{{% topic_menu_full children "Children" %}}\n'.format(SPACE24)

'''SPECIAL.SITEMAP.HTML REPLACE STRINGS'''
SITEMAP_ABOUT_US = '{0}{{% topic_menu_full about-us %}}\n'.format(SPACE12)
SITEMAP_KEY_INFO = '{0}{{% topic_menu_full key-information %}}\n'.format(SPACE12)
SITEMAP_NEWS_EVENTS = '{0}{{% topic_menu_full news-and-events %}}\n'.format(SPACE12)
SITEMAP_PARENTS = '{0}{{% topic_menu_full parents %}}\n'.format(SPACE12)
SITEMAP_CHILDREN = '{0}{{% topic_menu_full children %}}\n'.format(SPACE12)

'''BREADCRUMB TOPIC LINKS'''
BREADCRUMB_NEWS_EVENTS = '<li><a href="{% topic_url news-and-events %}">News and Events</a></li>'
BREADCRUMB_CHILDREN = '<li><a href="{% topic_url children %}">Children</a></li>'
BREADCRUMB_ABOUT_US = '<li><a href="{% topic_url about-us %}">About Us</a></li>'

''' Kidszone files list '''
KIDSZONEPAGES = [
    'special.brain-builders.html',
    'special.english.html',
    'special.games.html',
    'special.history.html',
    'special.ks1-links.html',
    'special.ks2-links.html',
    'special.maths.html',
    'special.science.html',
    'special.kidszone.html',
]

''' calendar files list '''
CALENDARPAGES = [
    'calendar.grid.html',
    'diary.detail.html',
    'diary.list.html',
]

''' define constants for css '''
HOME_ABOUT_US = '.main-nav .ps_topic_slug_about-us {}\n'
HOME_KEY_INFO = '.main-nav .ps_topic_slug_key-information {}\n'
HOME_NEW_EVENTS = '.main-nav .ps_topic_slug_news-and-events {}\n'
HOME_PARENTS = '.main-nav .ps_topic_slug_parents {}\n'
HOME_CHILDREN = '.main-nav .ps_topic_slug_children {}\n'

STYLE129_ABOUT_US = '.main-nav .ps_topic_slug_about-us { background-position: 0 -52px; z-index: 199; }\n'
STYLE129_KEY_INFO = '.main-nav .ps_topic_slug_key-information { background-position: 0 -104px; z-index: 198; }\n'
STYLE129_NEW_EVENTS = '.main-nav .ps_topic_slug_news-and-events { background-position: 0 -156px; z-index: 197; }\n'
STYLE129_PARENTS = '.main-nav .ps_topic_slug_parents { background-position: 0 -208px; z-index: 196; }\n'
STYLE129_CHILDREN = '.main-nav .ps_topic_slug_children { background-position: 0 -260px; z-index: 195; }\n'


STYLE136_ABOUT_US = '.main-nav .ps_topic_slug_about-us:focus, .main-nav .ps_topic_slug_about-us:hover { background-position: right -52px; }\n'
STYLE136_KEY_INFO = '.main-nav .ps_topic_slug_key-information:focus, .main-nav .ps_topic_slug_key-information:hover { background-position: right -104px; }\n'
STYLE136_NEW_EVENTS = '.main-nav .ps_topic_slug_news-and-events:focus, .main-nav .ps_topic_slug_news-and-events:hover { background-position: right -156px; }\n'
STYLE136_PARENTS = '.main-nav .ps_topic_slug_parents:focus, .main-nav .ps_topic_slug_parents:hover { background-position: right -208px; }\n'
STYLE136_CHILDREN = '.main-nav .ps_topic_slug_children:focus, .main-nav .ps_topic_slug_children:hover { background-position: right -260px; }\n'

STYLE204_ABOUT_US = '.main-nav .ps_topic_slug_about-us ul {}\n'
STYLE204_KEY_INFO = '.main-nav .ps_topic_slug_key-information ul {}\n'
STYLE204_NEW_EVENTS = '.main-nav .ps_topic_slug_news-and-events ul {}\n'
STYLE204_PARENTS = '.main-nav .ps_topic_slug_parents ul {}\n'
STYLE204_CHILDREN = '.main-nav .ps_topic_slug_children ul {}\n'

STYLE225_ABOUT_US = '.main-nav .ps_topic_slug_about-us ul li a {}\n'
STYLE225_KEY_INFO = '.main-nav .ps_topic_slug_key-information ul li a {}\n'
STYLE225_NEW_EVENTS = '.main-nav .ps_topic_slug_news-and-events ul li a {}\n'
STYLE225_PARENTS = '.main-nav .ps_topic_slug_parents ul li a {}\n'
STYLE225_CHILDREN = '.main-nav .ps_topic_slug_children ul li a {}\n'

STYLE241_ABOUT_US = '.main-nav .ps_topic_slug_about-us ul li:focus, .main-nav .ps_topic_slug_about-us ul li:hover {}\n'
STYLE241_KEY_INFO = '.main-nav .ps_topic_slug_key-information ul li:focus, .main-nav .ps_topic_slug_key-information ul li:hover {}\n'
STYLE241_NEW_EVENTS = '.main-nav .ps_topic_slug_news-and-events ul li:focus, .main-nav .ps_topic_slug_news-and-events ul li:hover {}\n'
STYLE241_PARENTS = '.main-nav .ps_topic_slug_parents ul li:focus, .main-nav .ps_topic_slug_parents ul li:hover {}\n'
STYLE241_CHILDREN = '.main-nav .ps_topic_slug_children ul li:focus, .main-nav .ps_topic_slug_children ul li:hover {}\n'

STYLE249_ABOUT_US = '.main-nav .ps_topic_slug_about-us ul a:focus, .main-nav .ps_topic_slug_about-us ul a:hover {}\n'
STYLE249_KEY_INFO = '.main-nav .ps_topic_slug_key-information ul a:focus, .main-nav .ps_topic_slug_key-information ul a:hover {}\n'
STYLE249_NEW_EVENTS = '.main-nav .ps_topic_slug_news-and-events ul li a:focus, .main-nav .ps_topic_slug_news-and-events ul li a:hover {}\n'
STYLE249_PARENTS = '.main-nav .ps_topic_slug_parents ul li a:focus, .main-nav .ps_topic_slug_parents ul li a:hover {}\n'
STYLE249_CHILDREN = '.main-nav .ps_topic_slug_children ul li a:focus, .main-nav .ps_topic_slug_children ul li a:hover {}\n'


''' functions to create html topics, slugs and breadcrumbs '''
def extends_theme(themename):
    ''' replace theme name function '''
    a = '{% extends "'
    b = '/base.html" %}'
    return '{0}{1}{2}'.format(a, themename, b)

def base_topic(slug,name):
    ''' create topic code for base.html '''
    a = '{% topic_menu_full '
    b = ' "'
    c = '" %}\n'
    return '{0}{1}{2} "{3}{4}'.format(SPACE24, a, slug, name, c)

def sitemap_topic(slug):
    ''' create topic code for special.sitemap.html  '''
    return '{0}{{% topic_menu_full {1} %}}\n'.format(SPACE12, str(slug))

def topic_breadcrumb(parent):
    ''' generate parent topic breadcrumb '''
    newcrumb = '<li><a href="{% topic_url '
    newcrumb += slugify(parent, to_lower=True)
    newcrumb += ' %}">'
    newcrumb += str(parent)
    newcrumb += '</a></li>'
    return newcrumb

def tour_breadcrumb(tourpagename):
    ''' create breadcrumb for tour page '''
    tourcrumb = '<li><a href="{% topic_url '
    tourcrumb += slugify(tourpagename, to_lower=True)
    tourcrumb += ' %}">'
    tourcrumb += str(tourpagename)
    tourcrumb += '</a></li>'
    return tourcrumb

def new_corp_link(nursery,calendarweek):
    ''' create new corp link '''
    if nursery:
        url = NURSERY_URL
        link = SEONURSERY[calendarweek]
    else:
        url = PRIMARY_URL
        link = SEOPRIMARY[calendarweek]
    return '<li><a href="{0}">"{1}'.format(url,link)

def homecss(topicslug):
    ''' function to create new css rules for new topics '''
    homerule = '.main-nav .ps_topic_slug_'
    homerule += str(topicslug)
    homerule += ' {}\n'
    return homerule

def style129(slug,p,z):
    ''' create css rule to replace line 129 onwards '''
    stylerule = '.main-nav .ps_topic_slug_'
    stylerule += str(slug)
    stylerule += ' { background-position: 0 -'
    stylerule += str(p)
    stylerule += 'px; z-index: '
    stylerule += str(z)
    stylerule += '; }\n'
    return stylerule

def style136(slug,p):
    ''' create css rule to replace line 136 onwards '''
    stylerule = '.main-nav .ps_topic_slug_'
    stylerule += str(slug)
    stylerule += ':focus, .main-nav .ps_topic_slug_'
    stylerule += str(slug)
    stylerule += ':hover { background-position: right -'
    stylerule += str(p)
    stylerule += 'px; }\n'
    return stylerule

def style204(slug):
    ''' create css rule to replace line 204 onwards '''
    stylerule = '.main-nav .ps_topic_slug_'
    stylerule += str(slug)
    stylerule += ' ul {}\n'
    return stylerule

def style225(slug):
    ''' create css rule to replace line 225 onwards '''
    stylerule = '.main-nav .ps_topic_slug_'
    stylerule += str(slug)
    stylerule += ' ul li a {}\n'
    return stylerule

def style241(slug):
    ''' create css rule to replace line 241 onwards '''
    stylerule = '.main-nav .ps_topic_slug_'
    stylerule += str(slug)
    stylerule += ' ul li:focus, .main-nav .ps_topic_slug_'
    stylerule += str(slug)
    stylerule += ' ul li:hover {}\n'
    return stylerule

def style249(slug):
    ''' create css rule to replace line 249 onwards '''
    stylerule = '.main-nav .ps_topic_slug_'
    stylerule += str(slug)
    stylerule += ' ul a:focus, .main-nav .ps_topic_slug_'
    stylerule += str(slug)
    stylerule += ' ul a:hover {}\n'
    return stylerule