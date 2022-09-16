/*Agora que aprendemos como inserir múltiplos registros em uma tabela.
Vamos povoar a tabela alunos. Iremos primeiramente limpar os registros da tabela alunos e depois povoar a mesma com 5 alunos:
Primeiro vamos limpar a tabela com o comando TRUNCATE TABLE:*/

TRUNCATE TABLE alunos;

# Agora vamos povoar a tabela com 5 alunos:

INSERT INTO alunos VALUES
(DEFAULT,'Pedro Martins', '1987-07-17', 'Av. Ant. Carlos, 6673', 'BELO HORIZONTE', 'MG', '12345678911'),
(DEFAULT,'Diego Mariano', '1990-01-01', 'Av. Ant. Carlos, 6673', 'BELO HORIZONTE', 'MG', '01234567891'),
(DEFAULT,'Fliper Ama', '2017-01-01', 'Av. Ant. Carlos, 6600', 'BELO HORIZONTE', 'MG', '11111111111'),
(DEFAULT,'Pedro Martins', '1997-02-13', 'Av. Brasil, 1000', 'CABO FRIO', 'RJ', '22222222222'),
(DEFAULT,'REGINA CAZÉ', '1920-01-01', 'Rua do Mar', 'SALVADOR', 'BA', '33333333333');