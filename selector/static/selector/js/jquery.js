$(function () {
    $('#twinkle-popover').popover();
})

$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus');
})

$(function () {
    $('[data-toggle="tooltip"]').tooltip();
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
