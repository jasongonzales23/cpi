/* Author: Jason Gonzales

*/
function languageChooser(){
    //$('.language').hover(
    //    function(){$(this).children().show();},
    //    function(){$(this).children().hide();}
    //)
    
}


UTIL = {
 
  fire : function(func,funcname, args){
 
    var namespace = CPI;  // indicate your obj literal namespace here
 
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



CPI = {
    common : {
        init : function(){
            languageChooser();
            
            },
        finalize : function(){}
    },
    home : {
        init : function(){},
        someID : function(){}
    }
}



$(document).ready(function(){
    //this only goes on pages that get a sidebar nav
    var heading = $('.nav').find('.ancestor').eq(1).text();
    $('.secondaryAncestor').text(heading);
    
    //to put text onto the image for banners
    //pulls it from an H1 within the banner container
    //this is mainly for demoing right now
    var caption = $('.banner').find('h1');
    var bannerImg = $('.banner').find('img');
    caption.addClass('imageCaption60');
});



// kick it all off here 
//$(document).ready(UTIL.loadEvents);

/*
function(){
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
            */
