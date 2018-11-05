$(function () {
    $('.loading').show();
    $('.index-body').hide();

    const MAX_RETRY_COUNT_FIND_IMAGES = 10;
    var retry_counter = 0;
    var set_interval_id = setInterval($(findTargetElement, 1000));
    function findTargetElement() {
        retry_counter++;

        if(retry_counter > MAX_RETRY_COUNT_FIND_IMAGES) {
            clearInterval(set_interval_id);
            $('.loading').fadeOut(2000, function() {
                $('.loading').remove();
            });
            $('.index-body').show();
        }
        var loading_images = document.querySelectorAll('.loading-image img');
        if(loading_images.length = 5) {
            clearInterval(set_interval_id);
            $('.loading').fadeOut(2000, function() {
                $('.loading').remove();
            });
            $('.index-body').show();
        }
    }
})
