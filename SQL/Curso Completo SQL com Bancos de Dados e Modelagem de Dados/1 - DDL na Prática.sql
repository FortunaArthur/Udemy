# create database escola
use escola;

create table departamento(
nome_departamento varchar(20),
predio 			  varchar(15),
orcamento		  numeric(12,2),
primary key(nome_departamento)
);

create table curso (
id_curso 			varchar(7),
titulo				varchar(50),
curso_departamento	varchar(20),
creditos			numeric(2,0),
primary key(id_curso),
foreign key(curso_departamento) references departamento (nome_departamento)
);