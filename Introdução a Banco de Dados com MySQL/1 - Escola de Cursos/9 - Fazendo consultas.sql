# SELECIONAR TUDO
SELECT * FROM alunos;

# SELECIONAR POR CAMPO E ORDEM
SELECT cidade, data_nascimento, cpf FROM alunos;

# SELECIONAR POR CONDIÇÃO
SELECT nome, cidade, data_nascimento, cpf FROM alunos WHERE cidade = "BELO HORIZONTE";

# ORDEM ALFÁETICA OU ACENDETE
SELECT * FROM alunos ORDER BY nome;

# ORDEM INVERSA OU DECENDENTE
SELECT * FROM alunos ORDER BY nome DESC;

# ORDEM POR NUMERO 
SELECT nome, data_nascimento, endereco FROM alunos ORDER BY 2 DESC;