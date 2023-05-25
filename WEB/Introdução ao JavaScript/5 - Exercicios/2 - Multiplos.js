let carro = {
    rodas: 4,
    portas: 2,
    cor: "cinza",
    ano: 2012,
    estado: "novo"
};

function mudarPropriedade(nomePropriedade, novoValor){
    switch(nomePropriedade){
        case "rodas":
            if(novoValor >  1){
                carro.rodas = novoValor;    
            }
            else{
                return "Minimo de rodas precisa ser 2";
            }
            break;
        case "portas":
            if (novoValor > 0){
                carro.portas = novoValor;
            } else {
                return "Minimo de portas precisa ser 1"
            }
            break;
        case "cor":
            if (novoValor == "cinza" || novoValor == "preto" || novoValor == "vermelho"){
                    carro.cor = novoValor;
                } else {
                    return "Cor invalida"
                }
            break;
        case "ano":
            carro.ano = novoValor
            
            if (novoValor <= 2019){
                carro.estado = "novo"
                return "Alteracao concluida"
            } else {
                carro.estado = "usado"
                return "Alteracao concluida"
            }
        default:
            return "Propriedade invalida"
    }
    
    return "Alteracao concluida"
}