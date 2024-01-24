# 17. Quantos filmes foram produzidos por ano?
select ano, count(ano) as Quantidade_Filmes from filmes group by ano order by ano;

# 18. Qual ano foram produzidos mais filmes?
select ano, count(ano) as Total from filmes group by ano order by Total desc limit 1;