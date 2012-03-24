/* Author: Jason Gonzales
*/


$(document).ready(function(){
    
    $('#slideshow').flexslider({
      manualControls: '#slideshow-controls li',
      controlsContainer: '.flex-container'
    });
    

    $('div.visual-nav .flexslider').flexslider({
      slideshow: false,
      manualControls: '.custom-controls li',
      controlsContainer: '.flex-container'
    });

});


