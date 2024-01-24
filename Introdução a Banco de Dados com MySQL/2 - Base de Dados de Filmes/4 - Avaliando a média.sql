# 6. Qual a média da nota da crítica especializada?
select avg(nota_especialistas) as Média_Especialistas from filmes;

# 7. Qual a média da nota do público?
select avg(nota_audiencia) as Média_Público from filmes;

# 8. Qual a média de custo de filmes?
select avg(custo) as 'Média por Filme' from filmes;

