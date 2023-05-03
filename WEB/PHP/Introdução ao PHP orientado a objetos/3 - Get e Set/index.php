<?php
require "Pessoa.php";

$uma_pessoa = new Pessoa;
$uma_pessoa->setNome("Arthur");

echo $uma_pessoa->getNome();