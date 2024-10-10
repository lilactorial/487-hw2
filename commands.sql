-- delete tables to empty database
DELETE TABLE Reservations;
DELETE TABLE Prices;
DELETE TABLE Cars;

-- make the tables

CREATE TABLE Reservations (
    resID INTEGER,
    name VARCHAR(255), 
    address VARCHAR(255),
    phone VARCHAR(255),
    cartype VARCHAR(10),
    plate VARCHAR(10),
    orderdate DATETIME,
    startdate DATE,
    enddate DATE,
    PRIMARY KEY (resID)
    );

CREATE TABLE Prices (
    cartype VARCHAR(255),
    price INTEGER,
    discountprice INTEGER,
    PRIMARY KEY(cartype)
);

CREATE TABLE Cars (
    plate VARCHAR(10),
    cartype VARCHAR(10),
    reserved 
    PRIMARY KEY (plate)
);

ALTER TABLE Reservations
ADD FOREIGN KEY (cartype) REFERENCES Prices(cartype);

ALTER TABLE Reservations
ADD FOREIGN KEY (plate) REFERENCES Cars(plate);

-- Add sample entries to the databases
INSERT INTO Cars 