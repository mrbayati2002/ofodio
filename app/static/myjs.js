var items = {
    'm_name':'Movie Name',
    'm_pubdate': 'Pub Date',
    'm_director': 'Director',
    'm_country': 'Country',
    'm_language': 'Language',
    'm_length': 'Length',
    'm_genre': 'Genre',
    'm_cover': 'Cover',
    'm_file': 'Movie File',
  };
var fileds_name = ['m_name',
                'm_pubdate',
                'm_director',
                'm_country',
                'm_language',
                'm_length',
                'm_genre',
                'm_cover',
                'm_file',
                ]
function parse(str) {
    var args = [].slice.call(arguments, 1),
        i = 0;

    return str.replace(/%s/g, () => args[i++]);
}
function validateForm() {
    for(name in fileds_name) {
        if(document.forms["movie_details"][name].value == "") {
            alert(parse("%s must be fillllllllllled out!", items[name]));
            return false;
        }
    }
}