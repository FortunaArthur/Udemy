<?php
require "Pessoa.php";
require "Programador.php";

$programador = new Programador("Arthur", "PHP");

echo $programador->getNome();

#pegar o objeto da constante
echo $programador::ESPECIE;