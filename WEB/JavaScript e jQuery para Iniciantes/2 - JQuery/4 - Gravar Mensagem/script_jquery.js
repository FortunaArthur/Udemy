$(function(){
    $("#Amarelo").click(function(){
        $("p").css("background-color", "yellow")
        $("p").fadeOut(3000)
        $("p").delay(1000)
        $("p").fadeIn(5000)
    });

    $("#Verde").click(function(){
        $("p").css("background-color", "green")
        $("#Mensagem").text("Cor Alterada pra Verde")
        $("#Mensagem").css("color", "green")
        $("#Mensagem").css("border", "3px solid green")
        $("#Mensagem").delay(1000)
        $("#Mensagem").fadeOut("slow")
    });
});