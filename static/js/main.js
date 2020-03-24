$(document).ready(function () {
    // Home page magnifiying effect.
    if ($('.home .zoom').length > 1) {
        $('.home .zoom').each(function (index, element) {
            $(element).blowup({
                'width' : 400,
                'height': 400,
                'scale' : 0.75,
            });
        });
    }

    // Single item images slider.
    if ($('.slider').length > 1) {
        $('.slider').lightSlider({
            item: 1,
            controls: false,
            gallery: true,
        });
    }

    // Single item magnifiying effect.
    if ($('.item .zoom').length > 1) {
        $('.item .zoom').each(function (index, element) {
            $(element).blowup({
                'width' : 500,
                'height': 500,
            });
        });
    }
})
