-- create
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'Secure1Pass!';
GRANT SELECT
ON *.*
TO user_0d_1@localhost;
FLUSH PRIVILEGES;
