/* Author: Jason Gonzales
*/


$(document).ready(function(){
    
    $('#slideshow-container').flexslider({
        slideshow: false,
        manualControls: '#slideshow-controls li a',
        controlsContainer: '#slideshow-container'
    });
    
    $('.visual-nav').flexslider({
        slideshow: false,
        manualControls: '.custom-controls li',
        controlsContainer: '.flex-container'
    });
    
    $("a[href^='http://']").attr("target","_blank");

});


