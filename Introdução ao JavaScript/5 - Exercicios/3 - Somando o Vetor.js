function calcularVetor(vetor, numero) {
    let novoVetor = [];
  
    for (let i = 0; i < vetor.length; i++) {
      if (vetor[i] > 5) {
        novoVetor.push(vetor[i] * numero);
      } else {
        novoVetor.push(vetor[i]);
      }
    }
  
    return novoVetor;
  }

