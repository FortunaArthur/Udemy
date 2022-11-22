/*LEMBRETE
É OS MSM MALAKOS DO INTRO A DBA, E TEM QFAZER A PUTA MARACUTAIA PRA RODAR OS JOINS PQ ELES NÃO POVOAM A TABELAS EMORDEM COM BASE O CURSO, BANDO DE LARÁPIOS
*/

# 1 - Aluno associados ao ids de seus cursos
SELECT A.nome, AC.id_curso 
# especificar que determinado campo faz parte de uma tabela
FROM alunos A, alunos_cursos AC
# Join entra aki, o A case como id do aluno e que seja igual ao id aluno da tabela alunos_cursos AC
WHERE A.id_aluno = AC.id_aluno;

# 2 - Aluno associados ao ids de seus cursos mostrando os nomes dos cursos 
SELECT A.id_aluno ,A.nome, C.id_curso, C.nome 
# adcionando nova tabela: cursos C
FROM alunos A, cursos C, alunos_cursos AC
WHERE A.id_aluno = AC.id_aluno AND C.id_curso = AC.id_curso;

# 3
SELECT A.nome, C.nome, N.descricao_atividade, N.vlr_nota
FROM alunos as A, alunos_cursos as AC, cursos as C, notas as N
WHERE A.id_aluno = AC.id_aluno AND C.id_curso = AC.id_curso AND AC.id_aluno_curso = N.id_aluno_curso

# o cara num explico bem esses joins não, se se orienta pelo qele fala, já q o cara n comenta nd e vc q se vire