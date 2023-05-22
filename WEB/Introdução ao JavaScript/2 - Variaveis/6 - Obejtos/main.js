let carro = {
    rodas: 4,
    portas: 2,
    nome: "carro",
    aVenda: true
};
console.log(carro);

// alterar
carro.portas = 2;
// ou
carro["portas"] = 4;

carro.nome = "TIIIAAAAAOO"


console.log(carro.portas, carro.nome);