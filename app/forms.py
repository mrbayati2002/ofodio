from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import (StringField,
                        SubmitField,
                        DateField,
                        IntegerField,
                        FloatField,
                        TextAreaField,
                        FileField,
                        SelectField,
                        RadioField,
                        )
from wtforms.validators import DataRequired, Length, regexp
import config

GENRES = (
    ('none', 'بدون دسته بندی'),
    ('action', 'اکشن'),
    ('historical', 'تاریخی'),
    ('horror', 'ترسناک'),
    ('crime', 'جنایی'),
    ('war', 'جنگی'),
    ('family', 'خانوادگی'),
    ('news', 'خبری'),
    ('drama', 'درام'),
    ('mysterious', 'راز آلود'),
    ('biography', 'زندگی نامه'),
    ('science_fiction', 'علمی-تخیلی'),
    ('fantasy', 'فانتزی'),
    ('comedy', 'کمدی'),
    ('short', 'کوتاه'),
    ('adventure', 'ماجراجویی'),
    ('documentary', 'مستند'),
    ('musical', 'موزیکال'),
    ('thriller', 'هیجان انگیز'),
    ('sport', 'ورزشی'),
    ('western', 'وسترن'),
)


class AddMovieForm(FlaskForm):
    moviefile_validators = [FileRequired(),
                            FileAllowed(config.ALLOWED_EXTENSIONS, message='Choose a movie file!'),]
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    pubdate = DateField('Publish Date', validators=[DataRequired()])
    director = StringField('Director', validators=[DataRequired(), Length(min=0, max=30)])
    country = StringField('Country', validators=[DataRequired(), Length(min=0, max=16)])
    language = StringField('Language', validators=[DataRequired(), Length(min=2, max=16)])
    length = IntegerField('Length', validators=[DataRequired(),])
    category = SelectField('Category', choices=GENRES, validators=[DataRequired()])
    rank = FloatField('Rank', validators=[])
    summary = TextAreaField('Summary', validators=[Length(max=1000)])
    # cover = FileField('Cover', validators=[regexp(r'^[^/\\]\.jpg$')])
    cover = FileField('Cover', validators=[])
    # have_subtitle = RadioField('Subtitle ?', choices=['yes','no'], validators=[DataRequired()])
    # subtitle = FileField('Subtitle File', validators=[])
    moviefile = FileField('Movie File', validators=[])
    submit = SubmitField('Add')
