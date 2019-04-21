
create database flask_crud;

use flask_crud;

create table if not exists contactos(
    id int not null auto_increment,
    nombre varchar(100) not null,
    telefono varchar(100) not null,
    email varchar(100) not null,
    primary key (id)
);

insert into contactos (nombre, telefono, email) 
values('Oscar Escamilla','7751306549','oscar@oscar');

CREATE USER  'heroku'@'localhost' IDENTIFIED BY 'heroku.2019';
GRANT ALL PRIVILEGES ON flask_crud.* TO 'heroku'@'localhost';
FLUSH PRIVILEGES;