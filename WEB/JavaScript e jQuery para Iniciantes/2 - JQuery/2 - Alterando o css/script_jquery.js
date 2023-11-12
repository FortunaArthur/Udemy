$(function(){
    $("button").click(function(){
        // o css recebe 2 parametros, oq vc quer mudar e pra qual é
        $("h1").css("color", "red")
        // agora mudar 1 separado, ele se orienta pelo id, tem q colocar o # na frente pra chamar
        $("#unico").css("color", "blue")
    });
});


$(function(){
    $("#Azul").click(function(){
        $("p").css("color", "blue")
    });

    $("#Verde").click(function(){
        $("p").css("color", "green")
    });
});