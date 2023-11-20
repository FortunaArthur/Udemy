# isso aki faz a ms coisa q isso aki: select nome, id_curso_ministra from instrutor, ministra where instrutor.id_instrutor = ministra.id_ministra;
select nome, id_curso_ministra from instrutor NATURAL JOIN ministra;
select nome, titulo from instrutor natural join curso;

