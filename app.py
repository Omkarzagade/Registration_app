from tkinter import *
from tkinter import messagebox
import pyodbc

login = Tk()
login.title("Registration Form by Omkar")
login.config(bg="black")
login.geometry("500x520")
login.resizable(0, 0)

# --------------------------------------------- FUNCTIONS ---------------------------------------------


def reset():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
    E5.delete(0, END)
    selected_state.set("---- Select State ----")
    E1.focus()


def validate():
    user_name = E1.get().capitalize()
    pswd = E2.get()
    conf_pswd = E3.get()
    e_mail = E4.get().lower()
    contact = str(E5.get())
    m_f = gender.get()
    user_state = selected_state.get()
    if pswd != conf_pswd or (pswd == "" and conf_pswd == ""):
        messagebox.showerror(
            "Match Error", "Please Check if password matches with confirm password")
        return
    if "@gmail.com" not in e_mail:
        messagebox.showerror(
            "Wrong Email", "It must be Gmail\nEnding with @gmail.com")
        return
    if not contact.isdigit() or len(contact) != 10:
        messagebox.showerror(
            "Alert", "Enter 10 digit mobile number without prefix +91")
        return
    submit(user_name, pswd, e_mail, contact, m_f, user_state)


def submit(user_name, pswd, e_mail, contact, m_f, user_state):
    cnxn = pyodbc.connect(Driver='{ODBC Driver 17 for SQL Server};',
                          Server='LAPTOP-1TREIDNA;',
                          Database='Users_database;',
                          Trusted_Connection='yes;')
    cursor = cnxn.cursor()
    try:
        cursor.execute('INSERT INTO Users VALUES((?),(?),(?),(?),(?),(?))',
                   user_name, pswd, e_mail, contact, m_f, user_state)
        cnxn.commit()
        messagebox.showinfo("Registered", "User {} is succesfully registered!!".format(user_name))
    except:
        messagebox.showerror("Registered", "User {} is already registered!!".format(user_name))

# ------------------------------------ LABELS ------------------------------------------


heading = Label(login, text="Submit Details", fg="#00FFFF",
                bg="black", font=("Maiandra GD", 28)).pack(pady=10)
EL1 = Label(login, text="Username", fg="#00FFFF", bg="black",
            font=("Maiandra GD", 15)).place(x=30, y=80)
EL2 = Label(login, text="Password", fg="#00FFFF", bg="black",
            font=("Maiandra GD", 15)).place(x=30, y=130)
EL3 = Label(login, text="Confirm Password", fg="#00FFFF",
            bg="black", font=("Maiandra GD", 15)).place(x=30, y=180)
EL4 = Label(login, text="E-mail", fg="#00FFFF", bg="black",
            font=("Maiandra GD", 15)).place(x=30, y=230)
EL5 = Label(login, text="Contact", fg="#00FFFF", bg="black",
            font=("Maiandra GD", 15)).place(x=30, y=280)
RL = Label(login, text="Gender", fg="#00FFFF", bg="black",
           font=("Maiandra GD", 15)).place(x=30, y=330)
OML = Label(login, text="Location", fg="#00FFFF", bg="black",
            font=("Maiandra GD", 15)).place(x=30, y=380)

# ---------------------------------- ENTRIES ----------------------------------------

E1 = Entry(login, fg="#39FF14", bg="black", font=("Maiandra GD", 15),
           highlightbackground="#00FFFF", highlightthickness=2, highlightcolor="#39FF14")
E1.place(x=230, y=80)
E1.focus()
E2 = Entry(login, fg="#39FF14", bg="black", font=("Maiandra GD", 15),
           highlightbackground="#00FFFF", highlightthickness=2, highlightcolor="#39FF14", show="*")
E2.place(x=230, y=130)
E3 = Entry(login, fg="#39FF14", bg="black", font=("Maiandra GD", 15), highlightbackground="#00FFFF",
           highlightthickness=2, highlightcolor="#39FF14")
E3.place(x=230, y=180)
E4 = Entry(login, fg="#39FF14", bg="black", font=("Maiandra GD", 15), highlightbackground="#00FFFF",
           highlightthickness=2, highlightcolor="#39FF14")
E4.place(x=230, y=230)
E5 = Entry(login, fg="#39FF14", bg="black", font=("Maiandra GD", 15), highlightbackground="#00FFFF",
           highlightthickness=2, highlightcolor="#39FF14")
E5.place(x=230, y=280)

# ----------------------------------------------------------------- RADIO BUTTON ------------------------------------------------------------------

gender = StringVar(login, "M")
R1 = Radiobutton(login, text="Male", fg="#00FFFF", activeforeground="#39FF14", bg="black",
                 activebackground="black", font=("Maiandra GD", 11), selectcolor="black", variable=gender, value="M").place(x=230, y=330)
R2 = Radiobutton(login, text="Female", fg="#00FFFF", activeforeground="#39FF14",
                 bg="black", activebackground="black", font=("Maiandra GD", 11), selectcolor="black", variable=gender, value="F").place(x=330, y=330)

# ------------------------------------ OPTION MENU ---------------------------------------

states = ["Maharashtra", "Gujarat", "Tamil Nadu", "Uttar Pradesh", "Karnataka",
          "Rajasthan", "Andhra Pradesh", "Madhya Pradesh", "Kerala", "Delhi"]
selected_state = StringVar(login, "---- Select State ----")
OM = OptionMenu(login, selected_state, *states)
OM.place(x=230, y=380, width=200)
OM.config(fg="#00FFFF", bg="black", activebackground="black",
          activeforeground="#00FFFF", font=("Maiandra GD", 11))
OM["menu"].config(fg="#39FF14", bg="black", activeforeground="black",
                  activebackground="#39FF14", font=("Maiandra GD", 11))

# ------------------------------------------------- BUTTONS -------------------------------------------------

Reset = Button(login, text="Reset", fg="#00FFFF", font=("Maiandra GD", 15), bg="black",
               activebackground="#39FF14", activeforeground="black", command=reset).place(x=130, y=450)
Submit = Button(login, text="Submit", fg="#00FFFF", font=("Maiandra GD", 15), bg="black",
                activebackground="#39FF14", activeforeground="black", command=validate).place(x=330, y=450)

login.mainloop()
