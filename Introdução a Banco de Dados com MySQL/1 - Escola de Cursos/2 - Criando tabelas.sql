# Tabela Aluno
# Identificador de Aluno (Chave Primária - Tipo Número)
CREATE TABLE alunos (
  id_aluno INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id_aluno));

# Tabela Cursos
# Identificador de Cursos (Chave Primária - Tipo Número)
CREATE TABLE cursos (
  id_curso INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id_curso));
  
# Tabela Notas
# Identificador de Notas (Chave Primária - Tipo Número)
CREATE TABLE notas (
  id_nota INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id_nota));