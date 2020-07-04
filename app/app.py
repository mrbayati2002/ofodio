from flask import (
    Flask,
    render_template,
    flash,
    redirect,
    request,
    url_for,
)
from datetime import datetime
import config
from flask_sqlalchemy import SQLAlchemy
from forms import AddMovieForm

app = Flask(__name__)
app.config.update(SECRET_KEY=config.SECRET_KEY)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pubdate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    director = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(16), nullable=False)
    language = db.Column(db.String(16), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    rank = db.Column(db.Float, nullable=True)
    summary = db.Column(db.Text, nullable=True)
    cover = db.Column(db.String(70), nullable=False, default=config.DEFAULT_COVER)
    have_subtitle = db.Column(db.Boolean, nullable=False)
    subtitle = db.Column(db.String(70), nullable=True)
    moviefile = db.Column(db.String(70), nullable=False)

    def __repr__(self):
        return f'{self.name}, {self.pubdate}'



@app.route('/')
@app.route('/home')
def home():
    active = {'home':'active', 'search':'', 'full_list':'', 'addmovie':'', 'about':'',}
    return render_template('home.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'Ofodio(Video platform) | Home', })

@app.route('/search')
def search():
    active = {'home':'', 'search':'active', 'full_list':'', 'addmovie':'', 'about':'',}
    return render_template('search.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'Ofodio | Search', })

@app.route('/full_list')
def full_list():
    active = {'home':'', 'search':'', 'full_list':'active', 'addmovie':'', 'about':'',}
    return render_template('full_list.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'Ofodio | Movies complete list', })

@app.route('/about')
def about():
    active = {'home':'', 'search':'', 'full_list':'', 'addmovie':'', 'about':'active',}
    return render_template('/about.html', data= {'active': active,
                                                    'copyrightmessage': config.COPYRIGHT_MESSAGE,
                                                    'title':'About', })


@app.route('/addmovie', methods=['POST', 'GET'])
def addmovie():
    form = AddMovieForm()
    if request.method=='POST':
        if form.validate_on_submit():
            print('#############################')
            print('#############################')
            return redirect(url_for('home'))
        else:
            print(form.name.data)
            flash('Error','danger')
    active = {'home':'', 'search':'', 'full_list':'', 'addmovie':'active', 'about':'',}
    return render_template('addmovie.html', form=form, data={'active':active,
                                                'copyrightmessage':config.COPYRIGHT_MESSAGE,})


if __name__ == '__main__':
    # app.run(debug = True, port=5005, host='0.0.0.0')
    app.run(debug = True, port=5005)