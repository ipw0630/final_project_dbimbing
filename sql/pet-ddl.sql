DROP TABLE IF EXISTS pet_adoption_db;
CREATE TABLE IF NOT EXISTS pet_adoption_db (
    PetID INTEGER,
    PetType TEXT,
    Breed TEXT,
    AgeMonths INTEGER,
    Color TEXT,
    Size TEXT,
    WeightKg FLOAT,
    Vaccinated INTEGER,
    HealthCondition INTEGER,
    TimeInShelterDays INTEGER,
    AdoptionFee INTEGER,
    PreviousOwner INTEGER,
    AdoptionLikelihood INTEGER
);