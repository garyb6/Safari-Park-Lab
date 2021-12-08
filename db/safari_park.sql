DROP TABLE IF EXISTS animals:
DROP TABLE IF EXISTS staff_list;


CREATE TABLE staff_list (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_date VARCHAR(255),
    department VARCHAR(255),
    rating INT 
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    staff_id INT REFERENCES staff_list(id) 
);