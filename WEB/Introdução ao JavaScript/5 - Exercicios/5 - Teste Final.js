function testeFinal(umaString, umNumero){
    // Aqui criei uma variavel para retornar no final da função, mas você pode
    // retornar o valor diretamente dentro de cada "case"
    let retorno;
 
    switch(umaString){
 
        //1) “mundojs”: Exibirá "MundoJS" no console e retornará o parâmetro Número.
        case "mundojs":
            // Bem simples, exibir o texto (cuidado com letras maiúsculas) e retornar o número
            console.log("MundoJS");
 
            // Atribui o número para a variável "retorno"
            retorno = umNumero;
            break;
 
        // 2) “soma”: Retornará o resultado da soma da metade do parâmetro número com o quadrado dele mesmo.
        case "soma":
            // Pegando a metade do parâmetro número
            let metadeNumero = (umNumero/2);
 
            // Pegando o quadrado do parâmetro número
            let quadradoNumero = (umNumero*umNumero);
 
            // atribuindo a soma das variáveis a variável retorno
            retorno = metadeNumero + quadradoNumero;
            break;
 
        // 3) “vetor”: Criará e retornará um vetor com 5 elementos.
                            // Cada elemento é igual ao parâmetro número mais o dobro do índice do vetor:
        case "vetor":
 
            // Criada a variavel com um vetor vazio (importante para o FOR abaixo)
            let vetor = [];
 
            // Utilizado o for para fazer 5 loops no vetor
            for(let i = 0; i< 5; i++){
 
                // Atribuído umNumero  mais o dobro do índice.
                vetor[i] = umNumero + (i * 2);
            }
 
            // armazenado  o vetor na variável de retorno
            retorno = vetor;
            break;
 
         // 4) “booleano”: Faça o mesmo vetor do caso vetor e retorne true 
                        // se a soma dos elementos deste vetor for maior que 35, do contrário, exibe false.
        case "booleano":
 
            // Criado um vetor. Observe que o nome é diferente do vetor anterior pois se for igual da erro de escopo.
            let array = [];
 
            // Criada variavel total para teste no retorno;
            let total = 0;
 
            // Feito 5 loops no vetor
            for(let i = 0; i < 5; i++){
 
                // Atribuído umNumero  mais o dobro do índice.
                array[i] = umNumero + (i * 2);
                
                // Adicionando o total
                total = total + array[i];
            }
 
            //Testa se o total é mair que 35
            retorno = total > 35;
            break;
      
         // Caso o parâmetro String seja diferente das opções acima, retornará -1.
        default:
            // Retorno padrão
            retorno = -1;
    }
    // Retorno da função
    return retorno;
}