# selecionar tudo
select * from departamento;

# selecionar especifico
select nome_departamento, orcamento from departamento;

# selecionar com outro nome
select (nome_departamento) as "Departamento", (orcamento) as "Saldo Passado", (orcamento * 4) as "Orçamento Atual" from departamento;

# selecionar valores de mais de uma tabela
select nome, id_curso_ministra from instrutor, ministra where instrutor.id_instrutor = ministra.id_ministra;