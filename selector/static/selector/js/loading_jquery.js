$(function () {
    $('.loading').show();

    const MAX_RETRY_COUNT_FIND_IMAGES = 10;
    var retry_counter = 0;

    var set_interval_id = setInterval($(findTargetElement, 1000));

    function findTargetElement() {
        retry_counter++;

        if(MAX_RETRY_COUNT_FIND_IMAGES < retry_counter) {
            clearInterval(set_interval_id);
            $('.loading').fadeOut(2000, function() {
                $('.loading').remove();
            });
        }
        var loading_images = document.querySelectorAll('.loading-image img');
        if(loading_images.length = 5) {
            clearInterval(set_interval_id);
            $('.loading').fadeOut(2000, function() {
                $('.loading').remove();
            });
        }
    }
})
