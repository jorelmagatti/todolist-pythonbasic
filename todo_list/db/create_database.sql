CREATE DATABASE IF NOT EXISTS todo;
USE todo;
CREATE TABLE todo (
    id integer not null auto_increment primary key,
    name varchar(200),
    description varchar(200),
    created_date datetime,
    executed boolean
);
SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;
INSERT INTO todo (name, description, created_date, executed) VALUES ('First Task','Example Task', "2023-10-03", 0);