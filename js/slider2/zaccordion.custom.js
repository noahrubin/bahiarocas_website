$(document).ready(function() {
    $("#slider").zAccordion({
        tabWidth: 100,
        speed: 650,
        slideClass: 'slider',
        animationStart: function () {
            $('#slider').find('li.slider-open div').css('display', 'none');
            $('#slider').find('li.slider-previous div').css('display', 'none');
        },
        animationComplete: function () {
            $('#slider').find('li div').fadeIn(600);
        },
        width: 1200,
        height: 670
    });
});
