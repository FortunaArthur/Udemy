# vamos inseirir uns dados pra fazer umas consultas
INSERT INTO alunos VALUES
(DEFAULT,'Goku Martins', '1987-07-17', 'Av. Ant. Carlos, 6673', 'BELO HORIZONTE', 'MG', '12345678911'),
(DEFAULT,'Diego Era do Gelo', '1990-01-01', 'Av. Ant. Carlos, 6673', 'BELO HORIZONTE', 'MG', '01234567891'),
(DEFAULT,'Kakashi Ama', '2017-01-01', 'Av. Ant. Carlos, 6600', 'BELO HORIZONTE', 'MG', '11111111111'),
(DEFAULT,'Goku Martins', '1997-02-13', 'Av. Brasil, 1000', 'CABO FRIO', 'RJ', '22222222222'),
(DEFAULT,'REGINA CAZÉ', '1920-01-01', 'Rua do Mar', 'SALVADOR', 'BA', '33333333333');

# Bora lá, o comando é SELECT "os campos q vc quer" FROM "Nome da tabela":
# se vc colcoar SELECT *, ele vai trazer tds os dados dakela tabela
select * from alunos;
select nome, estado, nascimento from alunos;

# Usando o WHERE, vai fazer uma filtragem devido a condição
select nome, nascimento,cpf from alunos where estado != "MG";
# selecione o nome, data de nascimento e o cpf de todos da tabela alunos cujo o estado seja diferenet de MG

# Ordem Alfabetica, ORDER BY, se vai escolher 1 campo e ordenalo por ele
select * from alunos order by nome;
# com cidade agr
select * from alunos order by cidade;

# Ordem Inversa, DESC, invertendo a ordem pelo ORDER BY;
select * from alunos order by nome desc;

# Ordenar pelo Campo
select nome, estado, nascimento from alunos order by 3;
# ele vai ordernar o 3 campo q vc esolheu, nesse caso o campo nascimento
select nome, estado, nascimento from alunos order by 3 desc; # invertendo campo nascimento
