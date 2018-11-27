$(function () {
    var $limited_skmr = $('.limited-skmr');
    var $check_limited = $('.check-limited');
    var $limited5 = $('.check-limited #limited5');
    var $limited_filter = $('.limited-filter');
    var $twinkle_mode = $('#twinkle-mode');
    var $select_button = $('.select');
    var $twinkle_button = $('.twinkle');
    var $twinkle_party = $('.twinkle-party');
    var $form_div = $('form div');

    $limited_skmr.tooltip();

    $check_limited.click(function () {
        if ($limited5.prop('checked') == true) {
            $limited_filter.removeClass('limited-filter-hide');
            $limited_filter.addClass('limited-filter-show');
        } else {
            $limited_filter.removeClass('limited-filter-show');
            $limited_filter.addClass('limited-filter-hide');
        }
    })

    $twinkle_mode.click(function () {
        $select_button.toggle();
        $twinkle_button.toggle();
        if ($twinkle_party.css("display") == "none") {
            $twinkle_party.removeClass('twinkle-party-hide');
            $twinkle_party.addClass('twinkle-party-show');
        } else {
            $twinkle_party.removeClass('twinkle-party-show');
            $twinkle_party.addClass('twinkle-party-show');
        }
    })
    
    if (window.matchMedia('max-width:767px').matches) {
        $form_div.addClass('btn-group-vertical');
    }
    
    $(window).resize(function () {
        if(window.matchMedia('(min-width:768px)').matches) {
            $form_div.removeClass('btn-group-vertical');
        } else {
            $form_div.addClass('btn-group-vertical');
        }
    })
})
