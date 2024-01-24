let x = 1;
// ISSO DAKI VAI DA ERRO, o y com Let é variavel local
if (x==1){
    let y = 99;
}
console.log(y);

// Jeito certo
if (x==1){
    var y = 99;
}
console.log(y);
//  VAR tem escopo global