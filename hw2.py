##################################
#   Lilac Dixon
#   CMPSC 487W
#   Section 002   
#
##################################

import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar 

# connect localhost database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="D@nd31i0n",
  database="hw2database"
)

mycursor = mydb.cursor()

# root window, when closed everything else will close
root = tk.Tk()
root.title('Mr. Johnson\'s Car Reserver!')

# popup window for errors or other informations for the user
def popupfn(txt):
        popup = tk.Toplevel(root)
        popup.title('Popup')
        tk.Label(popup, text=txt, height=10,width=35,padx=10,pady=5).grid(row=0)

# RESERVE PAGE
# for customers placing reservations
def reservepage():
    reserve = tk.Toplevel(root)
    reserve.title('Reservation Form')
    
    
    # create buttons and labels and other entry methods
    tk.Label(reserve, text='First Name', height=5,width=15,padx=10,pady=5).grid(row=0)
    first = tk.Entry(reserve)
    first.grid(row=0, column=1)
    
    tk.Label(reserve, text='Last Name', height=5,width=15,padx=10,pady=5).grid(row=1)
    last = tk.Entry(reserve)
    last.grid(row=1, column=1)
    
    tk.Label(reserve, text='Phone Number', height=5,width=15,padx=10,pady=5).grid(row=2)
    phone = tk.Entry(reserve)
    phone.grid(row=2, column=1)
    
    tk.Label(reserve, text='Car Type', height=5,width=15,padx=10,pady=5).grid(row=3)
    cartype = ttk.Combobox(reserve, values= ['sedan', 'suv', 'pickup', 'van'])
    cartype.set('sedan')
    cartype.grid(row=3, column=1)
    
    tk.Label(reserve, text='Start Date', height=5,width=15,padx=10,pady=5).grid(row=4)
    startcal = Calendar(reserve, selectmode= 'day')
    startcal.grid(row=4, column=1)
    
    tk.Label(reserve, text='End Date', height=5,width=15,padx=10,pady=5).grid(row=5)
    endcal = Calendar(reserve, selectmode= 'day')
    endcal.grid(row=5, column=1)
    
    # function for submitting reservation to database.
    # also makes sure reservation is valid.
    def submitRes():
        daterange = (endcal.selection_get() - startcal.selection_get()).days
        # check for invalid dates
        if daterange < 0:
            popupfn('Error: Date range is invalid!')
        #
        elif (first.get() == "" or last.get() == "" or phone.get() == ""):
            popupfn('Error: Empty fields! Please fill in all entry fields.')
        else:
            price = daterange + 1
            
            # get correct price (discount or full)
            if daterange >= 7:
                mycursor.execute("SELECT discountprice FROM Prices where cartype = \'" + str(cartype.get()) + "\'")
                price *= mycursor.fetchone()[0]
            else:
                mycursor.execute("SELECT price FROM Prices where cartype = \'" + str(cartype.get()) + "\'")
                price *= mycursor.fetchone()[0]
            
            # put entry into the database
            sql = "INSERT INTO Reservations (firstname, lastname, phone, cartype, startdate, enddate) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (first.get(), last.get(), phone.get(), cartype.get(), startcal.get_date(), endcal.get_date())
            
            mycursor.execute(sql, val)
            mydb.commit()
            
            print(mycursor.rowcount, "record inserted.")
            
            # show total price and that reservation was placed.
            popupfn('Reservation placed!\nTotal price will be:  $' + str(price))
            
            # close the reservation window
            reserve.destroy()
    
    # button to commit the reservation
    submit = tk.Button(reserve, text="Submit", command=submitRes, height=5,width=15,padx=10,pady=5)
    submit.grid(row=6, columnspan=2)
    

# page for mr johnson to pick between his options
def johnsonpage():
    johnson = tk.Toplevel(root)
    johnson.title('Pick Action')

    # BROWSE PAGE
    # to look at all the reservations
    def browsepage():
        browse = tk.Toplevel(johnson)
        browse.title('Browse Reservations')
        browse.geometry('400x400')
        
        # make scrollbar to scroll through the entries
        scrollbar = tk.Scrollbar(browse)
        scrollbar.pack(side='right', fill='y')
        
        # listbox to easily display the entries
        reservationlist = tk.Listbox(browse, yscrollcommand=scrollbar.set)
        
        mycursor.execute("SELECT * FROM Reservations")
        myresult = mycursor.fetchall()
        
        reservationlist.insert(tk.END, "First Name | Last Name | Phone | Car Type | Start Date | End Date")
        reservationlist.insert(tk.END, "-----------------------------------------------------------------")
        
        # print all the reservations in the listbox
        for x in myresult:
            string = str(x[1]) + '  |  ' + str(x[2]) + '  |  ' + str(x[3]) + '  |  ' + str(x[4]) + '  |  ' + str(x[5]) + '  |  ' + str(x[6])
            reservationlist.insert(tk.END, string)
            
        reservationlist.pack(side='left', fill='both')
        reservationlist['width'] = 400
        scrollbar.config(command=reservationlist.yview)
    
    # PAGE TO CHANGE PRICES
    def changeprice():
        pricepage = tk.Toplevel(johnson)
        pricepage.title('Change Prices')
        
        # label and entrybox for each price
        tk.Label(pricepage, text='Sedan Price/Day', height=5,width=20,padx=10,pady=5).grid(row=0, column=0)
        sedanreg = tk.Entry(pricepage)
        sedanreg.grid(row=1, column=0)
        mycursor.execute("SELECT price FROM Prices WHERE cartype = \'sedan\'")
        sedanreg.insert(0, mycursor.fetchone()[0])
        
        tk.Label(pricepage, text='Sedan Discount Price/Day', height=5,width=20,padx=10,pady=5).grid(row=0, column=1)
        sedandis = tk.Entry(pricepage)
        sedandis.grid(row=1, column=1)
        mycursor.execute("SELECT discountprice FROM Prices WHERE cartype = \'sedan\'")
        sedandis.insert(0, mycursor.fetchone()[0])
        
        tk.Label(pricepage, text='SUV Price/Day', height=5,width=20,padx=10,pady=5).grid(row=2, column=0)
        suvreg = tk.Entry(pricepage)
        suvreg.grid(row=3, column=0)
        mycursor.execute("SELECT price FROM Prices WHERE cartype = \'suv\'")
        suvreg.insert(0, mycursor.fetchone()[0])
        
        tk.Label(pricepage, text='SUV Discount Price/Day', height=5,width=20,padx=10,pady=5).grid(row=2, column=1)
        suvdis = tk.Entry(pricepage)
        suvdis.grid(row=3, column=1)
        mycursor.execute("SELECT discountprice FROM Prices WHERE cartype = \'suv\'")
        suvdis.insert(0, mycursor.fetchone()[0])
        
        tk.Label(pricepage, text='Pick-up Price/Day', height=5,width=20,padx=10,pady=5).grid(row=4, column=0)
        pickupreg = tk.Entry(pricepage)
        pickupreg.grid(row=5, column=0)
        mycursor.execute("SELECT price FROM Prices WHERE cartype = \'pickup\'")
        pickupreg.insert(0, mycursor.fetchone()[0])
        
        tk.Label(pricepage, text='Pick-up Discount Price/Day', height=5,width=20,padx=10,pady=5).grid(row=4, column=1)
        pickupdis = tk.Entry(pricepage)
        pickupdis.grid(row=5, column=1)
        mycursor.execute("SELECT discountprice FROM Prices WHERE cartype = \'pickup\'")
        pickupdis.insert(0, mycursor.fetchone()[0])
        
        tk.Label(pricepage, text='Van Price/Day', height=5,width=20,padx=10,pady=5).grid(row=6, column=0)
        vanreg = tk.Entry(pricepage)
        vanreg.grid(row=7, column=0)
        mycursor.execute("SELECT price FROM Prices WHERE cartype = \'van\'")
        vanreg.insert(0, mycursor.fetchone()[0])
        
        tk.Label(pricepage, text='Van Discount Price/Day', height=5,width=20,padx=10,pady=5).grid(row=6, column=1)
        vandis = tk.Entry(pricepage)
        vandis.grid(row=7, column=1)
        mycursor.execute("SELECT discountprice FROM Prices WHERE cartype = \'van\'")
        vandis.insert(0, mycursor.fetchone()[0])
        
        # commit changes of price to database
        def updateprices():
            # make sure values are floats
            try:
                ser = float(sedanreg.get())
                sed = float(sedandis.get())
                sur = float(suvreg.get())
                sud = float(suvdis.get())
                pur = float(pickupreg.get())
                pud = float(pickupdis.get())
                vnr = float(vanreg.get())
                vnd = float(vandis.get())
            # show the error msg
            except ValueError:
                print('Update price is invalid!')
                popupfn('Update price is invalid!\nPlease make sure it is a number.')
            # update the prices
            else:
                sql = "UPDATE Prices SET price = %s, discountprice = %s WHERE cartype = %s;"
                mycursor.execute(sql, (ser, sed, 'sedan'))
                mycursor.execute(sql, (sur, sud, 'suv'))
                mycursor.execute(sql, (pur, pud, 'pickup'))
                mycursor.execute(sql, (vnr, vnd, 'van'))
                
                mydb.commit()
                
                print('Prices successfully updated!')
                popupfn('Prices sucessfully updated!')
                pricepage.destroy()
        
        updatebtn = tk.Button(pricepage, text="Update Prices", command=updateprices, height=5,width=15,padx=10,pady=5)
        updatebtn.grid(row=8, columnspan=2)
    
    browsebtn = tk.Button(johnson, text="Browse Reservations", command=browsepage, height=5,width=15,padx=10,pady=5)
    browsebtn.grid(row=0, column=0)
    
    pricebtn = tk.Button(johnson, text="Change Prices", command=changeprice, height=5,width=15,padx=10,pady=5)
    pricebtn.grid(row=0, column=1)
    


# LOGIN PAGE
customerbtn = tk.Button(root, text="Continue as Customer", command=reservepage, height=5,width=15,padx=10,pady=5)
customerbtn.grid(row=0)

johnsonbtn = tk.Button(root, text="Login as Mr. Johnson", command=johnsonpage, height=5,width=15,padx=10,pady=5)
johnsonbtn.grid(row=1)

exitbtn = tk.Button(root, text="Exit", command=root.destroy, height=5,width=15,padx=10,pady=5)
exitbtn.grid(row=2)


root.mainloop()