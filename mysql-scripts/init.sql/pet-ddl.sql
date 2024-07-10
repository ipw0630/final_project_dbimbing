DROP TABLE IF EXISTS pet_adoption_db;
CREATE TABLE pet_adoption_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    breed VARCHAR(100),
    adopted BOOLEAN
);
