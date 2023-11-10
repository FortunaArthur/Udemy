#24
alunos = {}

c = 0

while True:

    id = int(input("Id do Aluno: "))

    if alunos.get(id):
        print("Ja existe o ID ", id)

    else:
        h = float(input("H do Aluno: "))
        alunos[id] = h
        c += 1

    if c == 3:
        False
        break

max_key = max(alunos, key = alunos.get)
max_value = alunos.get(max_key)

min_key = min(alunos, key = alunos.get)
min_value = alunos.get(min_key)

print("Id do aluno mais alto:", max_key, "\n"
"altura:", max_value, "\n"
"Id do aluno mais baixo:", min_key, "\n"
"altura do aluno mais baixo:", min_value)