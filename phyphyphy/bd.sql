create database DB_PY;

use DB_PY;

create table tb_contatos(
	
    ID int auto_increment primary key,
    LED_COR varchar(10),
    DATA_LED datetime default now()

);

select * from TB_LED