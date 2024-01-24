# se roda essa linha vc vai alterar TODOS os orçamentos pra 500
update departamento set orcamento = 500;

# alterar de maneira selecionada
update departamento set orcamento = 500 where nome_departamento like "Comercial";
# da pra colocar % na palavra q vc busca no like mais aki n vai fazer diferença

select * from departamento;