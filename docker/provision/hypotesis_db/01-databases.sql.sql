# create databases
CREATE DATABASE IF NOT EXISTS `hypotesis_manager`;
CREATE DATABASE IF NOT EXISTS `hypotesis_context`;
CREATE DATABASE IF NOT EXISTS `hypotesis_item`;
CREATE DATABASE IF NOT EXISTS `hypotesis_enrol`;
CREATE DATABASE IF NOT EXISTS `hypotesis_grade`;
CREATE DATABASE IF NOT EXISTS `hypotesis_report`;
CREATE DATABASE IF NOT EXISTS `hypotesis_competence`;
CREATE DATABASE IF NOT EXISTS `hypotesis_chat`;
CREATE DATABASE IF NOT EXISTS `hypotesis_forum`;

GRANT ALL ON `hypotesis_manager`.* TO 'hypotesis'@'%';
GRANT ALL ON `hypotesis_context`.* TO 'hypotesis'@'%';
GRANT ALL ON `hypotesis_item`.* TO 'hypotesis'@'%';
GRANT ALL ON `hypotesis_enrol`.* TO 'hypotesis'@'%';
GRANT ALL ON `hypotesis_grade`.* TO 'hypotesis'@'%';
GRANT ALL ON `hypotesis_report`.* TO 'hypotesis'@'%';
GRANT ALL ON `hypotesis_competence`.* TO 'hypotesis'@'%';
GRANT ALL ON `hypotesis_chat`.* TO 'hypotesis'@'%';
GRANT ALL ON `hypotesis_forum`.* TO 'hypotesis'@'%';

