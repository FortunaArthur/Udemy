/*INSERT INTO "o nome da tabela" (coluna1,coluna2,coluna3.....) VALUES (valor1,valor2,valor3....)*/
#tabela alunos
/*
ALTER TABLE `escolinha_de_cursinhos`.`alunos` 
ADD COLUMN `nome` VARCHAR(100) NOT NULL AFTER `id_aluno`,
ADD COLUMN `nascimento` DATE NOT NULL AFTER `nome`,
ADD COLUMN `endereco` VARCHAR(255) NOT NULL AFTER `nascimento`,
ADD COLUMN `cidade` VARCHAR(100) NOT NULL AFTER `endereco`,
ADD COLUMN `estado` VARCHAR(2) NOT NULL AFTER `cidade`,
ADD COLUMN `cpf` VARCHAR(11) NOT NULL AFTER `estado`;

*/
# ja q tds os campos nessa tabela são obrigatorios, não é nescessario colocar as colunas
# o id_alunos é auto incremente, sendo assim vc coloca default
insert into alunos values 
(default, "Goku", "1987-04-09", "Platena Terra", "Japão", "JP",00000000000);