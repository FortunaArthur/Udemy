<?php 
class Pessoa {
    // 3 tipos de propriedade
    # public - qualquer 1 pode acessar
    # private - só pode ser acessada por dentro da classe
    # protected - só pode ser acessada pela classe e por classes que herdaram suas caracteristicas

    private $nome;

    public function setNome($novoNome){
        $this->nome = $novoNome;
    }

    public function getNome(){
        return $this->nome;
    }
 }