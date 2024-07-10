COPY pet_adoption_data FROM '/data/pet_adoption_data.csv' DELIMITER AS ',' CSV HEADER;
SELECT * FROM pet_adoption_db LIMIT 5;