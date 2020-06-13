from flask_wtf import FlaskForm
from wtforms import (StringField,
                        SubmitField,
                        DateField,
                        IntegerField,
                        FloatField,
                        TextAreaField,
                        FileField,
                        SelectField,
                        BooleanField,
                        SubmitField,)
from wtforms.validators import DataRequired, Length, regexp

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
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    pubdate = DateField('pubdate', validators=[DataRequired()])
    director = StringField('director', validators=[DataRequired(), Length(min=0, max=30)])
    country = StringField('country', validators=[DataRequired(), Length(min=0, max=16)])
    language = StringField('language', validators=[DataRequired(), Length(min=2, max=16)])
    length = IntegerField('length', validators=[DataRequired(), Length(min=0, max=3)])
    category = SelectField('category', choices=GENRES, validators=[DataRequired()])
    rank = FloatField('Rank', validators=[Length(min=0, max=10)])
    summary = TextAreaField('Summary', validators=[Length(max=1000)])
    cover = FileField('Cover', validators=[regexp(r'^[^/\\]\.jpg$')])
    have_subtitle = BooleanField('Subtitle ?', validators=[DataRequired()])
    subtitle = FileField('Subtitle')
    moviefile = FileField('Movie File', validators=[DataRequired()])
    submit = SubmitField('Add')