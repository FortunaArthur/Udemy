<?php
#Importar classe de outro arquivo php
# require "Pessoa.php";
#o once vai impedir que a classe seja carregada masi vezes
# require_once "Pessoa.php";

# include "Pessoa.php";

#include não dara falal erro caso não exista o arquivo
# include "Pessoa123.php";

#se colocar um @ ele ignora os warnings 

@include "Pessoa.php";

$uma_pessoa = new Pessoa;
$uma_pessoa->nome = "Arthur";
$uma_pessoa->site = "www.arthur.com.br";
$uma_pessoa->falarNome();
echo "<br>";
$uma_pessoa->falarSite();