$(function () {
    $('#twinkle-popover').popover();
})

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
    })
})
