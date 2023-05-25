function testarTamanho(valor) {
    if (valor > 15) {
        return "maior";
    } else if (valor < 3) {
        return "menor";
    } else {
        return "na faixa";
    }
}

console.log(testarTamanho(4));