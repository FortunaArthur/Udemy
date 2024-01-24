# 19. Qual gênero produziu mais filmes em um ano?
select count(ano) as Total, Ano, Genero from filmes group by ano, genero order by Total desc limit 1; 

# 20. Qual o filme mais amado pela audiência e pelos especialistas ao mesmo tempo?
select filme, ano, genero, custo, (nota_audiencia + nota_especialistas)/2 as Nota_Média from filmes order by Nota_Média desc limit 1;