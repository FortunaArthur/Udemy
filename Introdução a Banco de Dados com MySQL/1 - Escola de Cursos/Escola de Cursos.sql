# APAGANDO AS TABELAS
DROP TABLE IF EXISTS notas;
DROP TABLE IF EXISTS alunos_cursos;
DROP TABLE IF EXISTS alunos;
DROP TABLE IF EXISTS cursos;
 
# RECRIANDO TABELA ALUNOS
CREATE TABLE `alunos` (
  `id_aluno` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `data_nascimento` date NOT NULL,
  `endereco` varchar(255) NOT NULL,
  `cidade` varchar(100) NOT NULL,
  `estado` varchar(2) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  PRIMARY KEY (`id_aluno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
 
CREATE TABLE `cursos` (
  `id_curso` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  PRIMARY KEY (`id_curso`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
 
CREATE TABLE `alunos_cursos` (
  `id_aluno_curso` int(11) NOT NULL AUTO_INCREMENT,
  `id_aluno` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  PRIMARY KEY (`id_aluno_curso`),
  KEY `fk_alunos_cursos_1_idx` (`id_aluno`),
  KEY `fk_alunos_cursos_2_idx` (`id_curso`),
  CONSTRAINT `fk_alunos_cursos_1` FOREIGN KEY (`id_aluno`) REFERENCES `alunos` (`id_aluno`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_alunos_cursos_2` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
 
CREATE TABLE `notas` (
  `id_nota` int(11) NOT NULL AUTO_INCREMENT,
  `id_aluno_curso` int(11) NOT NULL,
  `descricao_atividade` varchar(100) NOT NULL,
  `vlr_nota` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id_nota`),
  KEY `fk_notas_1_idx` (`id_aluno_curso`),
  CONSTRAINT `fk_notas_1` FOREIGN KEY (`id_aluno_curso`) REFERENCES `alunos_cursos` (`id_aluno_curso`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
 
# POVOANDO TABELAS ALUNOS
INSERT INTO alunos VALUES
(DEFAULT,'Pedro Martins', '1987-07-17', 'Av. Ant. Carlos, 6673', 'BELO HORIZONTE', 'MG', '12345678911'),
(DEFAULT,'Diego Mariano', '1990-01-01', 'Av. Ant. Carlos, 6673', 'BELO HORIZONTE', 'MG', '01234567891'),
(DEFAULT,'Fliper Ama', '2017-01-01', 'Av. Ant. Carlos, 6600', 'BELO HORIZONTE', 'MG', '11111111111'),
(DEFAULT,'Pedro Martins', '1997-02-13', 'Av. Brasil, 1000', 'CABO FRIO', 'RJ', '22222222222'),
(DEFAULT,'REGINA CAZÉ', '1920-01-01', 'Rua do Mar', 'SALVADOR', 'BA', '33333333333');
 
# POVOANDO TABELAS CURSOS
INSERT INTO cursos VALUES
(DEFAULT, "Codeigniter"),
(DEFAULT, "Python"),
(DEFAULT, "MySQL");
 
# POVOANDO TABELAS alunos_cursos
INSERT INTO alunos_cursos VALUES
(DEFAULT, 1, 1), # Pedro (id_aluno = 1) esta inscrito em Codeigniter (id_curso = 1)
(DEFAULT, 1, 2), # Pedro (id_aluno = 1) esta inscrito em Python (id_curso = 2)
(DEFAULT, 2, 1), # Diego (id_aluno = 2) esta inscrito em Codeigniter (id_curso = 1)
(DEFAULT, 2, 3), # Diego (id_aluno = 1) esta inscrito em Mysql (id_curso = 3)
(DEFAULT, 3, 1), # Fliper (id_aluno = 3) esta inscrito em Codeigniter (id_curso = 1)
(DEFAULT, 3, 2), # Fliper (id_aluno = 3) esta inscrito em Python (id_curso = 2)
(DEFAULT, 4, 1), # Ricardo (id_aluno = 1) esta inscrito em Codeigniter (id_curso = 1)
(DEFAULT, 5, 1); # Regina (id_aluno = 1) esta inscrito em Codeigniter (id_curso = 1)
 
# POVOANDO TABELAS notas
INSERT INTO 
notas VALUES
(DEFAULT, 1, 'Prova 1', 28.0), # Pedro fez a atividade Prova 1 no Codeigniter e tirou 28.0
(DEFAULT, 1, 'Prova 2', 25.0), # Pedro fez a atividade Prova 2 no Codeigniter e tirou 25.0
(DEFAULT, 2, 'Prova 2', 20.0), # Pedro fez a atividade Prova 2 no Python e tirou 20.0
(DEFAULT, 2, 'Prova 2', 20.0), # Pedro fez a atividade Exercício 2 no Python e tirou 10.0
(DEFAULT, 3, 'Prova 1', 25.0), # Diego fez a atividade Prova 1 no Codeigniter e tirou 25.0
(DEFAULT, 5, 'Prova 1', 28.0), # Fliper fez a atividade Prova 1 no Codeigniter e tirou 28.0
(DEFAULT, 6, 'Exercicio 2', 12.0); # Fliper fez a atividade Exercicio 2 no Python e tirou 12.0