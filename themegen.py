from bottle import *

# index page call
@route('/')
@view('index')
def index(page_title='Index'):
	return dict(page_title=page_title)

# process post from index
@route('/process', method='post')
@view('process')
def process(page_title='Process'):
	sitemap = request.forms.get('sitemap')
	themename = request.forms.get('themename')
	from process import sitemapProcess
	siteinfo = sitemapProcess(sitemap,themename)
	return dict(siteinfo=siteinfo)

# run host
run(host='0.0.0.0', port=8080, debug=True)