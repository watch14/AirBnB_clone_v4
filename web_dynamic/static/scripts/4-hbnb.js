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

    $.ajax({
        type: 'GET',
        url: 'http://0.0.0.0:5001/api/v1/status/',
        success: function (data) {
            if (data.status === 'OK') {
                $('#api_status').addClass('available');
            } else {
                $('#api_status').removeClass('available');
            }
        }
    });

    $('#search-btn').click(function () {
        $.ajax({
            type: 'POST',
            url: '/4-hbnb/search',
            contentType: 'application/json',
            data: JSON.stringify({ amenities: Object.keys(amenityIds) }),
            success: function (data) {
                $('section.places').empty();

                data.forEach(function (place) {
                    const article = $('<article></article>');
                    article.append('<div class="title_box"><h2>' + place.name + '</h2><div class="price_by_night">$' + place.price_by_night + '</div></div>');
                    article.append('<div class="information"><div class="max_guest">' + place.max_guest + ' Guest' + (place.max_guest !== 1 ? 's' : '') + '</div><div class="number_rooms">' + place.number_rooms + ' Bedroom' + (place.number_rooms !== 1 ? 's' : '') + '</div><div class="number_bathrooms">' + place.number_bathrooms + ' Bathroom' + (place.number_bathrooms !== 1 ? 's' : '') + '</div></div>');
                    article.append('<div class="user"><b>Owner:</b> ' + place.user.first_name + ' ' + place.user.last_name + '</div>');
                    article.append('<div class="description">' + place.description + '</div>');
                    $('section.places').append(article);
                });
            }
        });
    });
});
