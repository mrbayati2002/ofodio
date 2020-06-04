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
    return render_template('home.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/newmovie', methods=['POST', 'GET'])
def newMovie():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file', filename=filename))
            return render_template('seccessful.html', movie_name = filename)
    return render_template('new_movie.html')


if __name__ == '__main__':
   app.run(debug = True, port=5005)