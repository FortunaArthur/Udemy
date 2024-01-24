<?php
class Programador extends Pessoa{

    public $linguagem;

    public function __contruct($tmpNome, $tmpLinguagem){
        $this->nome = $tmpNome;
        $this->linguagem = $tmpLinguagem;

        #é uma constante que ja vem no sistema
        
        echo "<br>objeto ".__CLASS__." foi instanciado.<br>";
    }

}

// Constantes mágicas

// __LINE__
// Retorna o número da linha do script na qual ela foi declarada.

// __FILE__
// Retorna o caminho do arquivo PHP.

// __DIR__
// Retorna o diretório.

// __FUNCTION__
// Retorna a function a qual foi declarada.

// __CLASS__
// Retorna a class a qual foi declarada.

// __METHOD__
// Retorna a classe e o método a qual foi declarada.

// __NAMESPACE__
// Retona o namespace a qual foi declarada.

