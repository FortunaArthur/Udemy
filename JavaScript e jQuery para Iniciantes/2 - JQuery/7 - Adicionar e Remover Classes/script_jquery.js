$(function(){
    $("#Amarelo").click(function(){
        $("p")
            .css("background-color", "yellow")
            .fadeOut(3000)
            .delay(1000)
            .fadeIn(5000)
    });

    $("#Verde").click(function(){
        $("p").css("background-color", "green");
        $("#Mensagem")
            .text("Cor Alterada pra Verde")
            .css({color:"green", border:"3px solid red"})
            .addClass("purple")
        $("button").removeClass("verdinha")
    });
});