$(document).ready(function () {
    // Home page magnifiying effect.
    $('.home .zoom').each(function (index, element) {
        $(element).blowup({
            'width' : 400,
            'height': 400,
            'scale' : 0.75,
        });
    });

    // Single item images slider.
    $('.slider').lightSlider({
        item: 1,
        gallery: true,
    });

    // Single item magnifiying effect.
    $('.item .zoom').each(function (index, element) {
        $(element).blowup({
            'width' : 500,
            'height': 500,
        });
    });
})
