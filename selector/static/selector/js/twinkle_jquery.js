$(window).resize(function() {
    if(window.matchMedia('(min-width:768px)').matches) {
        $('.twinkle-content').show();
        $('.twinkle-content-mobile').hide();
    } else {
        $('.twinkle-content').hide();
        $('.twinkle-content-mobile').show();
    }
})
