from flask import (
    Flask,
    render_template,
    flash,
    redirect,
    request,

)
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
    active = {'home':'active', 'search':'', 'full_list':'', 'newmovie':'', 'about':'',}
    return render_template('home.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'Ofodio(Video platform) | Home',
                                                    })

@app.route('/search')
def search():
    active = {'home':'active', 'search':'active', 'full_list':'', 'newmovie':'', 'about':'',}
    return render_template('search.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'Ofodio | Search',
                                                    })

@app.route('/full_list')
def full_list():
    active = {'home':'active', 'search':'', 'full_list':'active', 'newmovie':'', 'about':'',}
    return render_template('full_list.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'Ofodio | Movies complete list',
                                                    })

@app.route('/about')
def about():
    active = {'home':'', 'search':'', 'full_list':'', 'newmovie':'', 'about':'active',}
    return render_template('/about.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'About',
                                                    })

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/newmovie', methods=['POST', 'GET'])
def newmovie():
    form_items = config.FORM_ITEMS_TO_EMPTY_CHECK
    # print(request.form['m_cover'])
    if request.method == 'POST':
        # check if the post request has the file part
        # for item in form_items.items():
        #     if request.form[item[0]] == '':
        #         flash('Please fill out %s field,  just Summary and Rank are optional.'%item[1], 'danger')
        #         return redirect(request.url)
        if 'm_file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['m_file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file', filename=filename))
            # return render_template('seccessful.html', movie_name = filename)
            flash('Seccussfully created :)', 'success')
            return redirect('/newmovie')
    active = {'home':'', 'search':'', 'full_list':'', 'newmovie':'active', 'about':'',}
    return render_template('newmovie.html', data={'active':active,
                                                'copyrightmessage':config.COPYRIGHT_MESSAGE,})

def database_connection():
    import sqlite3
    con = sqlite3.conenct('%s'%config.DB_NAME)
    c = con.cursor()

if __name__ == '__main__':
    app.run(debug = True, port=5005, host='0.0.0.0')
    # app.run(debug = True, port=5005)

