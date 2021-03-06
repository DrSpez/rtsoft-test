import os

INDEX_FILE = os.path.join('static', '_index.json')

APP_HOST = '127.0.0.1'
APP_PORT = 2016
APP_DEBUG = True

SECRET_KEY = 'topsecret2-30r9_*(@*R&(S@(#*)))'

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(basedir, 'static')
ALLOWED_EXTENSIONS = set(['xlsx'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
