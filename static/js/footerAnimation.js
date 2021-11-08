$(function(){
    $('.foot-icon').on('click', function(){
        if($(this).children().hasClass('tap')){
            // $(this).children().removeClass('tap');
            // $(this).removeClass('bg-color');
        }else{
            $('.foot-icon').removeClass('bg-color');
            $('.foot-icon').children().removeClass('tap');
            $(this).children().addClass('tap');
            $(this).addClass('bg-color');
        }
    });
});