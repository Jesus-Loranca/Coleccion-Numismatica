$(document).ready(function () {
    $('.zoom').each(function (index, element) {
        $(element).blowup({
            'width' : 400,
            'height': 400,
            'scale' : 0.75,
        });
    });
})
