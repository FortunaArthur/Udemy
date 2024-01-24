# 9. Quantos filmes custaram mais do que o custo médio dos filmes da tabela?
select count(*) as "Quantidade de Filmes mais Caros que a média" from filmes where custo > (select avg(custo) from filmes);

# 10. Quais são os filmes com nota acima da média das notas dadas pela crítica especializada?
select * from filmes where nota_especialistas > (select avg(nota_especialistas) from filmes) order by nota_especialistas desc ;

# 11. Quais são os filmes com nota acima da média das notas dadas pelo público? Quais os melhores?
select * from filmes where nota_audiencia > (select avg(nota_audiencia) from filmes) order by nota_audiencia desc;