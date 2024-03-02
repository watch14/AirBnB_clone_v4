$(document).ready(function () {
    const amenityIds = {};

    $('input[type="checkbox"]').change(function () {
        if (this.checked) {
            amenityIds[$(this).data('id')] = $(this).data('name');
        } else {
            delete amenityIds[$(this).data('id')];
        }

        const amenityList = Object.values(amenityIds).join(', ');
        $('div.Amenities h4').text('Amenities: ' + amenityList);
    });

    $.get('http://0.0.0.0:5001/api/v1/status/', function (data) {
        if (data.status === 'OK') {
            $('#api_status').addClass('available');
        } else {
            $('#api_status').removeClass('available');
        }
    });
});
