# OR, selecione quem tiver nessa condição OU quem tiver na outra, com OR só 1 condição tem q ser verdadeira
select * from alunos where id_aluno = 2 or id_aluno = 5;

# AND, selecione quem tiver nessa condição E TAMBÉM quem tiver na outra, com AND tds as condições tem qser verdadeiras
select * from alunos where cidade = "BELO HORIZONTE" and estado = "MG";

# Sinais
select * from alunos where nascimento > "1990-01-01";# MAIOR QUE
select * from alunos where nascimento >= "1990-01-01";# MAIOR OU IGUAL
select * from alunos where nascimento < "1990-01-01";# MENOR QUE
select * from alunos where nascimento <= "1990-01-01";# MENOR OU IGUAL
select * from alunos where nascimento <> "1990-01-01";# MENOR E MAIOR AO MESMO TEMPO
select * from alunos where nascimento = "1990-01-01";# IGUAL
select * from alunos where nascimento != "1990-01-01";# MENOR QUE