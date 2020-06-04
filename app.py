from flask import (
    Flask,
    render_template
)

UPLOAD_DIR = '/files'
ALLOWED_EXTENSIONS = {'mp4', 'mkv', 'avi', 'flv', 'mov', 'wmv', 'webm', }

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLO

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/newmovie')
def newMovie():
    return 'new movie creation'



if __name__ == '__main__':
   app.run(debug = True, port=5005)