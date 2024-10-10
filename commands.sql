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
    plate VARCHAR(10),
    orderdate DATETIME,
    startdate VARCHAR(30),
    enddate VARCHAR(30),
    PRIMARY KEY (resID)
    );

CREATE TABLE Cars (
    plate VARCHAR(10),
    cartype VARCHAR(10)
    PRIMARY KEY (plate)
);

CREATE TABLE Prices (
    cartype VARCHAR(10),
    price FLOAT,
    discountprice FLOAT,
    PRIMARY KEY (cartype)
);

ALTER TABLE Reservations
ADD FOREIGN KEY (plate) REFERENCES Cars(plate);
ALTER TABLE Reservations
ADD FOREIGN KEY (cartype) REFERENCES Prices(cartype);

-- Add sample entries to the car database
INSERT INTO Cars VALUES ('ABC1111', 'sedan');
INSERT INTO Cars VALUES ('DEF2222', 'sedan');
INSERT INTO Cars VALUES ('GHI3333', 'suv');
INSERT INTO Cars VALUES ('JKL4444', 'suv');
INSERT INTO Cars VALUES ('MNO5555', 'pickup');
INSERT INTO Cars VALUES ('PQR6666', 'pickup');
INSERT INTO Cars VALUES ('STU7777', 'van');
INSERT INTO Cars VALUES ('VWX8888', 'van');

-- Initial prices
INSERT INTO Prices VALUES ('sedan', 40.0, 32.0);
INSERT INTO Prices VALUES ('suv', 50.0, 40.0);
INSERT INTO Prices VALUES ('pickup', 80.0, 64.0);
INSERT INTO Prices VALUES ('van', 60.0, 48.0);