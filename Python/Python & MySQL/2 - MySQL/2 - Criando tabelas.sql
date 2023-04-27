# Tabela Aluno
# Identificador de Aluno (Chave Primária - Tipo Número)
CREATE TABLE `escolinha_de_cursinhos`.`alunos` (
  `id_aluno` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_aluno`));

# Tabela Cursos
# Identificador de Cursos (Chave Primária - Tipo Número)
CREATE TABLE `escolinha_de_cursinhos`.`cursos` (
  `id_curso` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_curso`));
  
# Tabela Notas
# Identificador de Notas (Chave Primária - Tipo Número)
CREATE TABLE `escolinha_de_cursinhos`.`notas` (
  `id_nota` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_nota`));