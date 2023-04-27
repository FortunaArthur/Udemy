/*Botaõ direito na tabela, escolhe Send to SQL Editor e vai no Create Statement
ele vai colocar o comando de criação p vc, e isso é deverás importante pra essa aula*/

/*Aki vc vai apagar a tabela alunos do banco*/
DROP TABLE alunos;

/*e aki vc reecria ela graças a instro q eu dei no inicio*/
CREATE TABLE `alunos` (
  `id_aluno` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `nascimento` date NOT NULL,
  `endereco` varchar(255) NOT NULL,
  `cidade` varchar(100) NOT NULL,
  `estado` varchar(2) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  PRIMARY KEY (`id_aluno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
