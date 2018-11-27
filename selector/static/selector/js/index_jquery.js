$(function () {
    var $limited_skmr = $('.limited-skmr');
    var $check_limited = $('.check-limited');
    var $limited5 = $('#limited5');
    var $check_limited5 = $('.check-limited5');
    var $limited_filter = $('.limited-filter');
    var $twinkle_mode = $('#twinkle-mode');
    var $select_button = $('.select');
    var $twinkle_button = $('.twinkle');
    var $twinkle_party = $('.twinkle-party');
    var $window = $(window);
    var $form_div = $('form div');

    // 初期化処理

    $limited_skmr.tooltip();

    if (window.matchMedia('max-width:767px').matches) {
        $form_div.addClass('btn-group-vertical');
    }

    // イベント

    $check_limited5.on("click", function () {
        if ($limited5.prop('checked') == false) {
            $limited_filter.removeClass('limited-filter-hide');
        }
    })

    $check_limited.on("click", function () {
        $limited_filter.addClass('limited-filter-hide');
    })

    $twinkle_mode.on("click", function () {
        $select_button.toggle();
        $twinkle_button.toggle();
        $twinkle_party.toggleClass('twinkle-party-hide');
    })

    if (window.matchMedia('(max-width:767px)').matches) {
        $form_div.addClass('btn-group-vertical');
    }

    $window.resize(function () {
        if(window.matchMedia('(min-width:768px)').matches) {
            $form_div.removeClass('btn-group-vertical');
        } else {
            $form_div.addClass('btn-group-vertical');
        }
    })
})
