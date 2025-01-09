CREATE DATABASE IF NOT EXISTS xemp_db;

USE xemp_db;

GRANT ALL PRIVILEGES ON xemp_db.* TO 'user'@'%';

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane@example.com');


