
CREATE DATABASE practicas;

USE practicas;

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);


select * from items;

DROP DATABASE practicas;
