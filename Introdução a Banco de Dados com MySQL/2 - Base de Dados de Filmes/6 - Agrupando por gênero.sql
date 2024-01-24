# 12. Quais são os tipos de categoria (gêneros) existentes?
select genero from filmes; # assim ele vai mostrar todos, até os repetidos
# Agrupando
select genero from filmes group by genero;

# 13. Quais são os gêneros com maior quantidade de filmes?
select genero, count(genero) as Total from filmes group by genero order by Total desc;