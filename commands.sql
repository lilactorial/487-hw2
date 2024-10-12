-- delete tables to empty database
DROP TABLE Reservations;
DROP TABLE Prices;
DROP TABLE Cars;

-- make the tables

CREATE TABLE Reservations (
    resID INTEGER NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    phone VARCHAR(255),
    cartype VARCHAR(10),
    startdate VARCHAR(30),
    enddate VARCHAR(30),
    PRIMARY KEY (resID)
    );

CREATE TABLE Prices (
    cartype VARCHAR(10),
    price FLOAT,
    discountprice FLOAT,
    PRIMARY KEY (cartype)
);

ALTER TABLE Reservations
ADD FOREIGN KEY (cartype) REFERENCES Prices(cartype);

-- Initial prices
INSERT INTO Prices VALUES ('sedan', 40.0, 32.0);
INSERT INTO Prices VALUES ('suv', 50.0, 40.0);
INSERT INTO Prices VALUES ('pickup', 80.0, 64.0);
INSERT INTO Prices VALUES ('van', 60.0, 48.0);