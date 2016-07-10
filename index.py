# 3rd-party
from bottle import error
from bottle import get
from bottle import redirect
from bottle import request
from bottle import route
from bottle import run
from bottle import static_file
from bottle import view

# Local
from generictemplate import buildgeneric
from process import sitemapprocess


@get('/<filename:re:.*\.js>')
def javascript(filename):
    """Static route for javascript."""
    return static_file(filename, root='static/js')


@get('/<filename:re:.*\.css>')
def stylesheet(filename):
    """Static route for stylesheets."""
    return static_file(filename, root='static/css')


@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def image(filename):
    """Static route for images."""
    return static_file(filename, root='static/images')


@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def font(filename):
    """Static route for fonts."""
    return static_file(filename, root='static/fonts')


@get('/<filename:re:.*\.zip>')
def zip(filename):
    """Static route for zipped themes."""
    return static_file(filename, root='static/themezips')


@error(404)
@view('404')
def error404(page_title='404 Error'):
    """Generate our custom 404 Error page."""
    return dict(page_title=page_title)


@route('/')
@view('index')
def index(page_title='Index'):
    """Generate the main index page."""
    return dict(page_title=page_title)


@route('/process', method='post')
@view('process')
def process(page_title='Site Theme Info'):
    """Process POSTed form for theme info."""
    sitemap = request.forms.get('sitemap')
    themename = request.forms.get('themename')
    nursery = request.forms.get('nursery')
    siteinfo = sitemapprocess(sitemap, themename, nursery)
    return dict(siteinfo=siteinfo, page_title=page_title)


@route('/process', method='get')
def processget():
    """Redirect if request method is GET."""
    redirect('/')


@route('/generic')
def generic():
    """Redirect to build template."""
    buildgeneric()
    redirect('/BuildTemplate.zip')


# run host
run(host='0.0.0.0', port=8080, debug=True)
