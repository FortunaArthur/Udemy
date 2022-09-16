# 1
SELECT nome, AC.id_curso 
FROM alunos as A, alunos_cursos as AC 
WHERE A.id_aluno = AC.id_aluno;

# 2
SELECT A.id_aluno ,A.nome, C.id_curso, C.nome 
FROM alunos as A, alunos_cursos as AC, cursos as C
WHERE A.id_aluno = AC.id_aluno AND C.id_curso = AC.id_curso;

# 3
SELECT A.nome, C.nome, N.descricao_atividade, N.vlr_nota
FROM alunos as A, alunos_cursos as AC, cursos as C, notas as N
WHERE A.id_aluno = AC.id_aluno AND C.id_curso = AC.id_curso AND AC.id_aluno_curso = N.id_aluno_curso