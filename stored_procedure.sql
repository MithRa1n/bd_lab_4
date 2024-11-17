USE iot_db;

DROP PROCEDURE IF EXISTS get_clients_after_number;
DELIMITER //
CREATE PROCEDURE get_clients_after_number(
    IN in_num int
)
BEGIN
    SELECT *
    FROM client WHERE number >= in_num ORDER BY number;
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS get_clients_with_name_and_number_filter;
DELIMITER //
CREATE PROCEDURE  get_clients_with_name_and_number_filter(
    IN first_letters_of_name char(30),
    IN in_num int
)
BEGIN
    SELECT * FROM client WHERE name RLIKE concat('^', first_letters_of_name) and number >= in_num ORDER BY name;
END //
DELIMITER ;