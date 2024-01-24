<?php 
class Pessoa {
    protected $nome;
    # const declara uma variavel que é constante e não vai mudar, e nela nãose coloca $
    const ESPECIE = "Humana";

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