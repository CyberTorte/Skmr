$(function () {
    $('.limited-skmr').tooltip();
})

$(function () {
    $('.check-limited').click(function () {
        if ($('#limited5').prop('checked') == true) {
            $('.limited-filter').show();
        } else {
            $('.limited-filter').hide();
        }
    })
})

$(function () {
    $('#twinkle-mode').click(function () {
        $('.select').toggle();
        $('.twinkle').toggle();
        $('.twinkle-party').toggle();
    })
})

$(window).resize(function () {
    if(window.matchMedia('(min-width:768px)').matches) {
        $('form div').removeClass('btn-group-vertical');
    } else {
        $('form div').addClass('btn-group-vertical');
    }
})
