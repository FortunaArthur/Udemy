# 5. Qual filme com maior custo e qual filme com menor custo?
SELECT * FROM filmes order by custo desc limit 1;
SELECT * FROM filmes order by custo limit 1;
# OUTRA FORMA
SELECT * FROM filmes where custo = (select max(custo) from filmes);
# SE VC COLCOAR SOMENTE """ select max(custo) from filmes""" ele só vai te retornar o valor maximo, MSM COISA PRO MIN
SELECT * FROM filmes where custo = (select min(custo) from filmes); # neste caso vai aparecer mais de 1 resultado PQ, tem mais de 1 filme com custo = 0