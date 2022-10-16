# LEMBRESE DE CRIAR A TEBELA 1°, dps se diz oqq é kd coisa

/*Tabela Alunos Cursos
Identificador de alunos e cursos (chave primária - tipo número)
Identificador de alunos (chave estrangeira - tipo numero)
Identificador de cursos (chave estrangeira - tipo numero)*/
ALTER TABLE `escolinha_de_cursinhos`.`alunos_cursos` 
ADD INDEX `fk_id_aluno_idx` (`id_aluno` ASC) VISIBLE,
ADD INDEX `fk_id_curso_idx` (`id_curso` ASC) VISIBLE;
;
ALTER TABLE `escolinha_de_cursinhos`.`alunos_cursos` 
ADD CONSTRAINT `fk_id_aluno`
  FOREIGN KEY (`id_aluno`)
  REFERENCES `escolinha_de_cursinhos`.`alunos` (`id_aluno`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_id_curso`
  FOREIGN KEY (`id_curso`)
  REFERENCES `escolinha_de_cursinhos`.`cursos` (`id_curso`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

/*Tabela Notas
Identificador de notas (chave primária - tipo número)
Identificador de alunos e cursos (chave estrangeira - tipo numero)*/
ALTER TABLE `escolinha_de_cursinhos`.`notas` 
ADD COLUMN `id_aluno_curso` INT NOT NULL AFTER `id_nota`,
ADD INDEX `fk_id_aluno_curso_idx` (`id_aluno_curso` ASC) VISIBLE;
;
ALTER TABLE `escolinha_de_cursinhos`.`notas` 
ADD CONSTRAINT `fk_id_aluno_curso`
  FOREIGN KEY (`id_aluno_curso`)
  REFERENCES `escolinha_de_cursinhos`.`alunos_cursos` (`id_alunos_cursos`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
