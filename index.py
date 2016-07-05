from bottle import *
from process import sitemapProcess

# setup static folder routes
# javascript
@get('/<filename:re:.*\.js>')
def javascript(filename):
	return static_file(filename, root='static/js')
# stylesheets
@get('/<filename:re:.*\.css>')
def stylesheet(filename):
	return static_file(filename, root='static/css')
# images
@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def image(filename):
	return static_file(filename, root='static/images')
# fonts
@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def font(filename):
	return static_file(filename, root='static/fonts')

# custom 404
@error(404)
@view('404')
def error404(page_title='404 Error'):
	return dict(page_title=page_title)

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
	nursery = request.forms.get('nursery')
	siteinfo = sitemapProcess(sitemap,themename,nursery)
	return dict(siteinfo=siteinfo)

# run host
run(host='0.0.0.0', port=8080, debug=True)