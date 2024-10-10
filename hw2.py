import mysql.connector
import tkinter

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="D@nd31i0n",
  database="hw2database"
)

mycursor = mydb.cursor()

mycursor.execute("""
    CREATE TABLE Cars (
    plate VARCHAR(10),
    cartype VARCHAR(10),
    resID INTEGER,
    PRIMARY KEY (plate)
);

ALTER TABLE Reservations
ADD FOREIGN KEY (cartype) REFERENCES Prices(cartype);

ALTER TABLE Reservations
ADD FOREIGN KEY (plate) REFERENCES Cars(plate);

ALTER TABLE Cars
ADD FOREIGN KEY (resID) REFERENCES Reservations(resID);
""")