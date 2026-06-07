CREATE DATABASE devana_estimator;

USE devana_estimator;

CREATE TABLE projects(
id INT PRIMARY KEY AUTO_INCREMENT,
project_name VARCHAR(100),
area FLOAT,
total_cost FLOAT
);