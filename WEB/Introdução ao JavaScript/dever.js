function processarletiavel(letiavel) {
    let novoVetor = [];
  
    for (let x = 0; x < letiavel.length; x++) {
      let subvetor = letiavel[x];
      let soma = 0;
  
      for (let y = 0; y < subvetor.length; y++) {
        soma += subvetor[y];
      }
  
      novoVetor.push(soma);
    }
  
    return novoVetor;
  }


w = [[1,2,3,4], [4,6,8,9], [4,7,3,9]]
console.log(processarletiavel(w));

function processarletiavel(letiavel) {
    let novoVetor = [];
    
    for (let subvetor of letiavel) {
      let soma = subvetor.reduce((acc, curr) => acc + curr, 0);
      novoVetor.push(soma);
    }
    
    return novoVetor;
  }