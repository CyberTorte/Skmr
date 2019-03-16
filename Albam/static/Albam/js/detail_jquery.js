$(function() {
    var jumbotron = $('.jumbotron')
    var thunnail_photo = $('#first-card');

    jumbotron.css({
        'background': 'linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)), url("' + thunnail_photo.attr('src') + '")',
        'background-size': 'contain',
        'background-repeat': 'no-repeat',
        'background-position': 'center 60%',
        'background-color': 'white'
    });
})