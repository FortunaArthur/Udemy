<?php 
class Pessoa {
    #aki muda pra protected pois os dados devem ser protegidos e a classe está sendo herdada
    protected $nome;

    public function __construct($tmpNome){
        $this->nome = $tmpNome;
    }


    public function setNome($novoNome){
        $this->nome = $novoNome;
    }

    public function getNome(){
        return $this->nome;
    }
 }