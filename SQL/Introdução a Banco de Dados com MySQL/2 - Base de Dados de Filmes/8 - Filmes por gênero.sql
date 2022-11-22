# 15. Qual gênero tem a mais alta média de nota para o público?
select avg(nota_audiencia) as "Comedy" from filmes where genero = "Comedy";
select avg(nota_audiencia) as "Action" from filmes where genero = "Action";
select avg(nota_audiencia) as "Drama" from filmes where genero = "Drama";
select avg(nota_audiencia) as "Horror" from filmes where genero = "Horror";
select avg(nota_audiencia) as "Thriller" from filmes where genero = "Thriller";
select avg(nota_audiencia) as "Adventure" from filmes where genero = "Adventure";
select avg(nota_audiencia) as "Romance" from filmes where genero = "Romance";
# Quem ganho essa foi o genero "Thriller"
select * from filmes where genero = "Thriller" order by nota_audiencia desc;

# 16. Qual gênero tem a mais alta média de nota para a crítica especializada?
select avg(nota_especialistas) as "Comedy" from filmes where genero = "Comedy";
select avg(nota_especialistas) as "Action" from filmes where genero = "Action";
select avg(nota_especialistas) as "Drama" from filmes where genero = "Drama";
select avg(nota_especialistas) as "Horror" from filmes where genero = "Horror";
select avg(nota_especialistas) as "Thriller" from filmes where genero = "Thriller";
select avg(nota_especialistas) as "Adventure" from filmes where genero = "Adventure";
select avg(nota_especialistas) as "Romance" from filmes where genero = "Romance";
# "Thriller" Ganho aki tb
select * from filmes where genero = "Thriller" order by nota_especialistas desc;