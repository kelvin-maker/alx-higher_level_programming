-- create the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- grant user_0d_1 all permissions
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
