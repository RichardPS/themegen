#define constants
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
'''extends base.html'''
EXTENDS_BASE = '{% extends "BuildTemplate/base.html" %}'
'''BASE.HTML REPLACE STRINGS'''
BASE_ABOUT_US = '                        {% topic_menu_full about-us "About Us" %}\r\n'
BASE_KEY_INFO = '                        {% topic_menu_full key-information "Key Information" %}\r\n'
BASE_NEWS_EVENTS = '                        {% topic_menu_full news-and-events "News and Events" %}\r\n'
BASE_PARENTS = '                        {% topic_menu_full parents "Parents" %}\r\n'
BASE_CHILDREN = '                        {% topic_menu_full children "Children" %}\r\n'
'''SPECIAL.SITEMAP.HTML REPLACE STRINGS'''
SITEMAP_ABOUT_US = '            {% topic_menu_full about-us %}\r\n'
SITEMAP_KEY_INFO = '            {% topic_menu_full key-information %}\r\n'
SITEMAP_NEWS_EVENTS = '            {% topic_menu_full news-and-events %}\r\n'
SITEMAP_PARENTS = '            {% topic_menu_full parents %}\r\n'
SITEMAP_CHILDREN = '            {% topic_menu_full children %}\r\n'
'''BREADCRUMB LINKS'''
BREADCRUMB_NEWS_EVENTS = '    <li><a href="{% topic_url news-and-events %}">News and Events</a></li>'
BREADCRUMB_CHILDREN = '    <li><a href="{% topic_url children %}">Children</a></li>'
BREADCRUMB_ABOUT_US = '    <li><a href="{% topic_url about-us %}">About Us</a></li>'