$('.garantiya').click(function(e){
    $(this).addClass('active');
    $('.techical').removeClass('active');
    $('.tech').removeClass('view');
    $('.tech').addClass('hide');
    $('.garant').removeClass('hide');
    $('.garant').addClass('view');

});
$('.techical').click(function(e){
    $(this).addClass('active');
    $('.garantiya').removeClass('active');
    $('.tech').addClass('view');
    $('.tech').addClass('hide');
    $('.garant').removeClass('view');
    $('.garant').addClass('hide');

});
$('.dryk').click(function(e){

    var inter = 'techical';
    var gar = 'vidhuk'
    var dryk = 'dryk'
    var gar_but = document.getElementsByClassName("garantiya")
    var inter_but = document.getElementsByClassName("techical")
    var dryk_but = document.getElementsByClassName("dryk")
    var gar_name = document.getElementById(gar);
    var dryk_name = document.getElementById(dryk);
    var name = document.getElementById(inter);
    if (dryk_name.className == 'hide'){
        dryk_but.classlist.add('active');
        inter_but.classlist.remove('active');
        gar_but.classlist.remove('active');
        dryk_name.classList.remove('hide');
        dryk_name.classList.add("view");
        name.classList.add("hide");
        name.classList.remove('view');
        gar_name.classList.add("hide");
    }
});
$(document).ready(function() {
    var $button = $(".technical").click(function (e) {
        var $this = $(this).addClass('active');
        var id = $(this).data('id');
        var ids = '#technical_' + id;
        var $th = $(this);
        var $rev = $(ids);
        var $that = $rev.addClass( 'view');
        $button.not($this).removeClass('active');
        $rev.removeClass('view');
        $rev.addClass('hide');
        $rev.not($that).addClass('view');
        $rev.not($that).removeClass('hide');
        console.log($rev);
    });
});

