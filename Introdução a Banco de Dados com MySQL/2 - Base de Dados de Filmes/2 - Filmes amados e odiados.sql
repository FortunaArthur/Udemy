# 1. Quais são os 10 filmes mais apreciados pelo público?
SELECT * FROM filmes order by nota_audiencia desc limit 10;

# 2. Quais são os 10 filmes mais apreciados pela crítica especializada?
SELECT * FROM filmes order by nota_especialistas desc limit 10;

# 3. Quais são os 10 filmes mais odiados pelo público?
SELECT * FROM filmes order by nota_audiencia limit 10;

# 4. Quais são os 10 filmes mais odiados pela crítica especializada?
SELECT * FROM filmes order by nota_especialistas limit 10;