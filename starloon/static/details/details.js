$(".nav-link").click(function() {
    var href = $(this).attr('href'); 
    scrollAmount = 0;
    if (href == "#home")
      scrollAmount = 0;
    else
      scrollAmount = $(href).offset().top - 50;
    
    $('html, body').animate({
        scrollTop: scrollAmount
    }, 1000);
});

// scrollbar