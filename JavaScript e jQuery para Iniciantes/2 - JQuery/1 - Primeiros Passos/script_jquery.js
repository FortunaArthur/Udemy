/*
sintaxe basico do jquery
$(seletor).ação();
*/

// o comando vai verificar se o documento está pronto, e quando o documento tiver carregado ele vai rodar uma função
$(document).ready(function(){
    // a função é pra verificar se o butão foi apertado
    $("button").click(function(){
        // agora a função hide vai esconder a div
        $("h1").hide()
    });
});

// Uma forma mais simples
$(function(){
    $("button").click(function(){
        $("h1").hide()
    });
});