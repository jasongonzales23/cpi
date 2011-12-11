/* Author: Jason Gonzales

*/
UTIL = {
 
  fire : function(func,funcname, args){
 
    var namespace = RUFFIN;  // indicate your obj literal namespace here
 
    funcname = (funcname === undefined) ? 'init' : funcname;
    if (func !== '' && namespace[func] && typeof namespace[func][funcname] == 'function'){
      namespace[func][funcname](args);
    } 
 
  }, 
 
  loadEvents : function(){
 
    var bodyId = document.body.id;
 
    // hit up common first.
    UTIL.fire('common');
 
    // do all the classes too.
    $.each(document.body.className.split(/\s+/),function(i,classnm){
      UTIL.fire(classnm);
      UTIL.fire(classnm,bodyId);
    });
 
    UTIL.fire('common','finalize');
 
  } 
 
};



RUFFIN = {
    common : {
        init : function(){},
        finalize : function(){}
    },
    home : {
        init : function(){
            i = 0;
            function runIt(){
                var slides = $('.slideshow').find('img');
                var n = slides.length;
                if ( i === n ) { i = 0 }
                $thisSlide = slides.eq(i)
                $thisSlide.fadeIn(500);
                $thisSlide.siblings().fadeOut(300);
                i++;
            }
            
            runIt();
            var t=setInterval(runIt,5000);
            
            $('audio,video').mediaelementplayer({
            audioWidth: 240
            
            });
            },
        someID : function(){}
    },
    gallery : {
        init : function(){
            $(".galleryLink").colorbox({
                rel:'galleryLink',
                maxWidth: '85%',
                maxHeight: '85%'
                });
        }
    }
}



// kick it all off here 
$(document).ready(UTIL.loadEvents);

