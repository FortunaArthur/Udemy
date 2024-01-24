<?php
# minha classe programador se estende a classe pessoa
# o programador heradará o nome da classe pessoa
class Programador extends Pessoa{

    public $linguagem;

    public function __contruct($tmpNome, $tmpLinguagem){
        $this->nome = $tmpNome;
        $this->linguagem = $tmpLinguagem;
    }

}