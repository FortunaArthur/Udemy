$(function(){
    $("#p1").click(function(){
        $("#i1").show();
        $("#i2").hide();
        $("#i3").hide();
    });

    $("#p2").click(function(){
        $("#i1").hide();
        $("#i2").show();
        $("#i3").hide();
    });

    $("#p3").click(function(){
        $("#i1").hide();
        $("#i2").hide();
        $("#i3").show();
    });
});