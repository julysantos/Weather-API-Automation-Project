create database if not exists weather_db;

use weather_db;

create table if not exists weather_data (
    id int not null primary key auto_increment, 
    city varchar(50) not null, 
    temperature float not null, 
    description varchar(255), 
    humidity int not null, 
    timestamp timestamp default current_timestamp
    );