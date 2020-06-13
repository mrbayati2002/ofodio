from flask import (
    Flask,
    render_template,
    flash,
    redirect,
    request,
)
from forms import AddMovieForm
import config
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = config.ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config.update(SECRET_KEY=config.SECRET_KEY)

app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER

@app.route('/')
@app.route('/home')
def home():
    active = {'home':'active', 'search':'', 'full_list':'', 'addmovie':'', 'about':'',}
    return render_template('home.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'Ofodio(Video platform) | Home', })

@app.route('/search')
def search():
    active = {'home':'active', 'search':'active', 'full_list':'', 'addmovie':'', 'about':'',}
    return render_template('search.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'Ofodio | Search', })

@app.route('/full_list')
def full_list():
    active = {'home':'active', 'search':'', 'full_list':'active', 'addmovie':'', 'about':'',}
    return render_template('full_list.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'Ofodio | Movies complete list', })

@app.route('/about')
def about():
    active = {'home':'', 'search':'', 'full_list':'', 'addmovie':'', 'about':'active',}
    return render_template('/about.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'About', })

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/addmovie', methods=['POST', 'GET'])
def addmovie():
    form = AddMovieForm()
    active = {'home':'', 'search':'', 'full_list':'', 'addmovie':'active', 'about':'',}
    return render_template('addmovie.html', form=form, data={'active':active,
                                                'copyrightmessage':config.COPYRIGHT_MESSAGE,})

# def database_connection():
#     import sqlite3
#     con = sqlite3.conenct('%s'%config.DB_NAME)
#     c = con.cursor()

if __name__ == '__main__':
    # app.run(debug = True, port=5005, host='0.0.0.0')
    app.run(debug = True, port=5005)

