<?php 
class Pessoa {
    private $nome;

    #função contruct ja vai contruir direatemente o obejto
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