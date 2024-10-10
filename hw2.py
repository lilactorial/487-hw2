import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="D@nd31i0n",
  database="hw2database"
)

mycursor = mydb.cursor()

root = tk.Tk()
root.title('Mr. Johnson\'s Car Reserver!')

# RESERVE PAGE
def reservepage():
    reserve = tk.Toplevel(root)
    reserve.title('Reservation Form')
    
    tk.Label(reserve, text='First Name', height=5,width=15,padx=10,pady=5).grid(row=0)
    tk.Label(reserve, text='Last Name', height=5,width=15,padx=10,pady=5).grid(row=1)
    first = tk.Entry(reserve)
    last = tk.Entry(reserve)
    first.grid(row=0, column=1)
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
    
    def popup(txt):
        popup = tk.Toplevel(reserve)
        popup.title('Information')
        tk.Label(popup, text=txt, height=10,width=35,padx=10,pady=5).grid(row=0)
    
    
    def submitRes():
        daterange = (endcal.selection_get() - startcal.selection_get()).days
        if daterange < 0:
            popup('Error: Date range is invalid!')
        else:
            price = daterange
            if daterange >= 7:
                mycursor.execute("SELECT discountprice FROM Prices where cartype = \'" + str(cartype.get()) + "\'")
                price *= mycursor.fetchone()[0]
            else:
                mycursor.execute("SELECT price FROM Prices where cartype = \'" + str(cartype.get()) + "\'")
                price *= mycursor.fetchone()[0]
                
            popup('Total price will be:  $' + str(price))
            
            
        
            
    
    submit = tk.Button(reserve, text="Submit", command=submitRes, height=5,width=15,padx=10,pady=5)
    submit.grid(row=6, column=1)


# BROWSE PAGE
def browsepage():
    browse = tk.Toplevel(root)
    browse.title('Browse Reservations')
    print("JOHNSON!")


# LOGIN PAGE
customerbtn = tk.Button(root, text="Continue as Customer", command=reservepage, height=5,width=15,padx=10,pady=5)
customerbtn.grid(row=0)

johnsonbtn = tk.Button(root, text="Login as Mr. Johnson", command=browsepage, height=5,width=15,padx=10,pady=5)
johnsonbtn.grid(row=1)

exitbtn = tk.Button(root, text="Exit", command=root.destroy, height=5,width=15,padx=10,pady=5)
exitbtn.grid(row=2)


root.mainloop()