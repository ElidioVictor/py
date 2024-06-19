create database db_agenda;

use db_agenda;

create table tb_contatos(
	id int not null auto_increment primary key,
    nome varchar(150),
    email varchar(150),
    telefone varchar(11),
    tipoTelefone enum('residencial','celular','nao especificado')
);

select * from tb_contatos