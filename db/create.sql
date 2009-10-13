CREATE DATABASE zeit;
CREATE USER 'zeit'@'localhost' IDENTIFIED BY 'zeit';
GRANT ALL ON zeit.* TO 'zeit'@'localhost';
FLUSH PRIVILEGES;