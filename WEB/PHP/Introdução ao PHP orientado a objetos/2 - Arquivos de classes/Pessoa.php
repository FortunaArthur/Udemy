<?php 
class Pessoa {
    public $nome;
    public $site;

    public function falarNome(){
        echo $this->nome;
    }

    public function falarSite(){
        echo $this->site;
    }
 }