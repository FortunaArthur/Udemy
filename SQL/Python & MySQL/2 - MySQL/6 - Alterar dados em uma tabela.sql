# UPATE "nome da tabela" SET "coluna1 = valor1", "coluna2 = valor 2" WHERE condição
# insert into alunos values (default, "Goku", "1987-04-09", "Platena Terra", "Japão", "JP",00000000000);
update alunos set nome = "Kakashi" where nome = "Goku";
/*Ele vai trocar o valor(nome) pelo  outro, no caso a condição é, troke o valor da coluna nome ONDE o valor da coluna nome é igual a "Goku"*/
# da pra fazer com + segurança assim
update alunos set nome = "Kakashi" where id_aluno = 1;
/*PORRRQQUUUEEEE, pode ter mais de 1 aluno com msm nome, mais o id não muda, assim vc não erra*/