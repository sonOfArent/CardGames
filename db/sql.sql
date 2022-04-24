-- CREATE TABLE users (
--     username TEXT NOT NULL PRIMARY KEY,
--     password,
--     email,
--     age
--     );

-- INSERT INTO users (username, password, email, age)
-- VALUES (
--     'Isaac',
--     'IsaacPassw0rd',
--     'isaacdonley@gmail.com',
--     19
-- );

-- INSERT INTO users (username, password, email, age)
-- VALUES (
--     'Exodus',
--     'passw0rd',
--     'exodusdonley@gmail.com',
--     21
-- );

-- SELECT password FROM users
-- WHERE username = 'Exodus';

-- SELECT username FROM users
-- WHERE password IN ('passw0rd', 'IsaacPassw0rd');

-- UPDATE users SET email = 'isaac@gmail.com'
-- WHERE username = 'Isaac';

SELECT * FROM users;
