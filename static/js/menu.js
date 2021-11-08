$(document).ready(function(){
    $(".sub-menu").on('click', function() {

        var c = $(".sub-menu");
        if(c.hasClass('menu-active')) {
            c.removeClass('menu-active');
            c.addClass('menu-inactive');
        }
        $(this).removeClass('menu-inactive');
        $(this).addClass('menu-active');

        var id = $(this).attr('id');
        $(".sub-container").hide();
        $("#sub-container-"+id).show();
    });

});