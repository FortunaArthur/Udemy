/*Tabela Alunos
-Identificador de Aluno (Chave Primária - Tipo Número)
-------> Nome (tipo texto)
-------> Data de Nascimento (tipo data)
-------> Endereço (tipo texto)
-------> CPF (tipo texto)*/
ALTER TABLE alunos
ADD COLUMN `nome` VARCHAR(100) NOT NULL AFTER `id_aluno`,
ADD COLUMN `data_nascimento` DATE NOT NULL AFTER `nome`,
ADD COLUMN `endereco` VARCHAR(255) NOT NULL AFTER `data_nascimento`,
ADD COLUMN `cidade` VARCHAR(100) NOT NULL AFTER `endereco`,
ADD COLUMN `estado` VARCHAR(2) NOT NULL AFTER `cidade`,
ADD COLUMN `cpf` VARCHAR(11) NOT NULL AFTER `estado`;

/*Tabela Cursos
Identificador de Cursos (Chave Primária - Tipo Número)
-------> Nome (tipo texto)*/
ALTER TABLE cursos
ADD COLUMN `nome` VARCHAR(100) NOT NULL AFTER `id_curso`;

/*Tabela Notas
Identificador de Notas (Chave Primária - Tipo Número)
-------> Descrição de Atividade (tipo texto)
-------> Nota (tipo número)*/
ALTER TABLE notas
ADD COLUMN `drescricao_atividade` VARCHAR(100) NOT NULL AFTER `id_nota`,
ADD COLUMN `vlr_nota` DECIMAL(5,2) NOT NULL AFTER `id_nota`;