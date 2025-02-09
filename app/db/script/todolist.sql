CREATE DATABASE IF NOT EXISTS todolist CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE todolist;
CREATE TABLE IF NOT EXISTS Users (
	idUsers INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50),
	email VARCHAR(50),
	password VARCHAR(60)
);
CREATE TABLE IF NOT EXISTS Tasks (
	idTask INT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(50),
	description VARCHAR(250),
    idUser INT,
    FOREIGN KEY (idUser) REFERENCES Users(idUsers)
);
