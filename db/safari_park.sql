DROP TABLE IF EXISTS staff;


CREATE TABLE staff (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);