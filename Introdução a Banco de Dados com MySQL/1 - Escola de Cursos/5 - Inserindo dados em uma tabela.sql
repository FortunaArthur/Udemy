/* Campos Para Orientação
CREATE TABLE `alunos` (
  `id_aluno` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `data_nascimento` date NOT NULL,
  `endereco` varchar(255) NOT NULL,
  `cidade` varchar(100) NOT NULL,
  `estado` varchar(2) NOT NULL, #AKI BEM Q EU PODIA TER COLOCADO SÓ "UF" MSM, MAIS VIDA Q SEGUE
  `cpf` varchar(11) NOT NULL,
  PRIMARY KEY (`id_aluno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;*/

# DEFAULT para os auto_increment
INSERT INTO alunos VALUES (Default, "Arthur Sanchez Fortuna", "1999-09-18", "Asa Norte", "Brasília", "DF", "19990915123");