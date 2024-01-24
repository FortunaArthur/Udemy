# create database escola;
use escola;

create table departamento (
nome_departamento varchar(20),
predio 			  varchar(15),
orcamento		  numeric(12,2),
primary key (nome_departamento)
);

create table curso (
id_curso 			varchar(7),
titulo				varchar(50),
curso_departamento	varchar(20),
creditos			numeric(2,0),
primary key (id_curso),
foreign key (curso_departamento) references departamento (nome_departamento)
);

create table instrutor (
id_instrutor			varchar(5),
nome					varchar(20) not null,
instrutor_departamento	varchar(20),
salario 				numeric(8,2),
primary key (id_instrutor),
foreign key (instrutor_departamento) references departamento (nome_departamento)
);

create table secao (
id_curso_secao		varchar(8),
id_secao			varchar(7),
semestre			varchar(6),
ano					numeric(4,0),
predio				varchar(15),
numero_sala			varchar(7),
id_periodo			varchar(4),
primary key (id_curso_secao, id_secao, semestre, ano),
foreign key (id_curso_secao) references curso (id_curso)
);

create table ministra (
id_ministra			varchar(5),
id_curso_ministra	varchar(7),
id_secao_ministra	varchar(8),
ministra_semestre	varchar(6),
ministra_ano		numeric(4,0),
primary key (id_ministra, id_curso_ministra, id_secao_ministra, ministra_semestre, ministra_ano),
foreign key (id_curso_ministra, id_secao_ministra, ministra_semestre, ministra_ano) references  
			secao (id_curso_secao, id_secao, semestre, ano),
foreign key (id_ministra) references instrutor (id_instrutor)
);