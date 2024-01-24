<?php
require "Pessoa.php";
require "Programador.php";

$programador = new Programador("Arthur", "PHP");

echo $programador->getNome();

echo $programador::ESPECIE;