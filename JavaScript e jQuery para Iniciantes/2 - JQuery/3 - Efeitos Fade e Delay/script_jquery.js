$(function(){
    $("#Amarelo").click(function(){
        $("p").css("background-color", "yellow")
        $("p").fadeOut(3000)
        $("p").delay(1000)
        $("p").fadeIn(5000)
    });

    $("#Verde").click(function(){
        $("p").css("background-color", "green")
        $("p").fadeOut("slow")
        $("p").delay(2000)
        $("p").fadeIn("fast")
    });
});