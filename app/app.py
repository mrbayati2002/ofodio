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
def home():
    return render_template('home.html', data={'copyrightmessage':config.COPYRIGHT_MESSAGE,})

@app.route('/search')
def search():
    return render_template('search.html', data={'copyrightmessage':config.COPYRIGHT_MESSAGE,})

@app.route('/full_list')
def full_list():
    return render_template('full_list.html', data={'copyrightmessage':config.COPYRIGHT_MESSAGE,})

@app.route('/about')
def about():
    return render_template('/about.html', data={'copyrightmessage':config.COPYRIGHT_MESSAGE,})

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
    return render_template('newmovie.html', data={'copyrightmessage':config.COPYRIGHT_MESSAGE,})

def database_connection():
    import sqlite3
    con = sqlite3.conenct('%s'%config.DB_NAME)
    c = con.cursor()

if __name__ == '__main__':
    # app.run(debug = True, port=5005, host='0.0.0.0')
    app.run(debug = True, port=5005)

