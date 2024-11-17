USE iot_db;

INSERT INTO iot_db.client_type(id, type)
VALUES
(1, 'customer'), (2, 'staff'), (3, 'manager'), (4, 'friend');

INSERT INTO iot_db.client (name, number, client_type_id)
VALUES
('Pavelchak Andrii', 10023,  4),
('Veres Zenovii', 10026, 1),
('Yatsuk Yurii', 10030, 1),
('Samotyi Volodymyr', 20011, 2),
('Shevchenko Petro', 30028, 3);
