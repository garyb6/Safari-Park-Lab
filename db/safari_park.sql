DROP TABLE IF EXISTS staff_list;


CREATE TABLE staff_list (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    start_date VARCHAR(255),
    department VARCHAR(255),
    rating INT 
);