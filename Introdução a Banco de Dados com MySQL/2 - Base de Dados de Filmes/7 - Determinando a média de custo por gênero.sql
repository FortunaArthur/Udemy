# 14. Qual gênero tem a mais alta média de custo?
# Vai ter q rodar 1 por 1 e olhar quem gastou mais nessa bagaça
select avg(custo) as "Comedy" from filmes where genero = "Comedy";
select avg(custo) as "Action" from filmes where genero = "Action";
select avg(custo) as "Drama" from filmes where genero = "Drama";
select avg(custo) as "Horror" from filmes where genero = "Horror";
select avg(custo) as "Thriller" from filmes where genero = "Thriller";
select avg(custo) as "Adventure" from filmes where genero = "Adventure";
select avg(custo) as "Romance" from filmes where genero = "Romance";
# DPS de rodar td isso, da pra ver q o genero "Action" é o mais caro
select * from filmes where genero = "Action" order by custo desc;

# 15. Qual gênero tem a mais alta média de nota para o público?


# 16. Qual gênero tem a mais alta média de nota para a crítica especializada?