
create database flask_crud;


create table if not exists contactos(
    id int not null auto_increment,
    nombre varchar(100) not null,
    telefono varchar(100) not null,
    email varchar(100) not null,
    primary key (id)
);