function somarSubVetores(vetor){
    let novoVetor = [];

    for (let x = 0; x < vetor.length; x++) {
      let subvetor = vetor[x];
      let soma = 0;
  
      for (let y = 0; y < subvetor.length; y++) {
        soma += subvetor[y];
      }
  
      novoVetor.push(soma);
    }
  
    return novoVetor;
  }