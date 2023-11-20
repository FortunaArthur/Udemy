# selecionar tudo
select * from departamento;

# selecionar especifico
select nome_departamento, orcamento from departamento;

# selecionar com outro nome
select (nome_departamento) as "Departamento", (orcamento) as "Saldo Passado", (orcamento * 4) as "Orçamento Atual" from departamento;