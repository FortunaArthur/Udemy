<?php
#classe sempre começa com letra MAIUSCULA
 class Pessoa {
    public $nome;
    public $site;

    #função começa com letra minuscula seguida de Maiuscula se tiver outra paalvra pra definir
    public function falarNome(){
        #this indica o atributo para o escopo local
        echo $this->nome;
    }

    public function falarSite(){
        echo $this->site;
    }
 }
#criando um objeto com new (um novo objeto)
#criando um novo objeto (uma_pessoa) que recebe a isntancia de uma classe (Pessoa)
$uma_pessoa = new Pessoa;
#uma pessoa na posição "nome" recebe Arthur
#neste objeto vc atribuindo o nome
$uma_pessoa->nome = "Arthur";
$uma_pessoa->site = "www.arthur.com.br";

#função var_dump imprimi o objeto
var_dump($uma_pessoa);
echo "<br>";

#agora mostrar o valor do objeto, no caso o nome, chamando a função
$uma_pessoa->falarNome();
echo "<br>";
$uma_pessoa->falarSite();