# OR
SELECT * FROM alunos WHERE id_aluno = 2 OR id_aluno = 5;

# AND
SELECT * FROM alunos WHERE cidade = "BELO HORIZONTE" AND estado = "MG";

# MAIOR 
SELECT * FROM alunos WHERE data_nascimento > "1990-01-01";

#MENOR
SELECT * FROM alunos WHERE data_nascimento < "1990-01-01";

# MAIOR OU IGUAL
SELECT * FROM alunos WHERE data_nascimento >= "1990-01-01";

#MENOR OU IGUAL
SELECT * FROM alunos WHERE data_nascimento <= "1990-01-01";

# DIFERENTE
SELECT * FROM alunos WHERE data_nascimento <> "1990-01-01";