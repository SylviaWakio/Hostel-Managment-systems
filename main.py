from gui import *
from database import *
from tkinter.messagebox import showinfo, askokcancel

app = App()
dbm = DataBaseManager()

def check_authentication(username, password):
    admin_document = dbm.AdminCollection.find_one({"username": username, "password": password})
    if admin_document and "username" in admin_document:
        # dbusername = admin_document["username"]
        # ... rest of your code
        return True
    else:
        showinfo("Authentication Error", "Invalid Username or password")
        return False

def login(username, password):
    if check_authentication(username=username, password=password):
        app.log_in()  # Make sure app.log_in() is defined in your App class
    else:
        showinfo("Login Error", "Invalid Username or password")

def logout():
    yes = askokcancel(title="Info", message="Are you sure you want to log out? ")
    if yes:
        app.log_out()  # Make sure app.log_out() is defined in your App class

# ... (rest of your functions)

app.loginframe.set_logincommand(login)
app.mainframe.set_command_for_button(5, logout)
app.mainframe.set_command_for_button(4, createusernamepassword)
app.mainframe.set_command_for_button(1, start_feedback)
app.mainframe.set_command_for_button(2, create_employeemanager)
app.mainframe.set_command_for_button(0, create_roommanager)
app.mainframe.set_command_for_button(3, create_viewstudents)
app.feedbackmanager.set_commandforaddfeedbackbuttons(add_feedback)
app.feedbackmanager.set_commandforbackbutton(lambda: app.backtomainframe())
app.employeemanager.set_commandforbackbutton(lambda: app.backtomainframe())
app.viewstudentsframe.set_commandforbackbutton(lambda: app.backtomainframe())
app.roommanager.set_commandforbackbutton(lambda: app.backtomainframe())
app.roommanager.set_commandforremoveroombutton(create_removeroomtoplevel)
app.roommanager.set_commandforaddroombutton(create_addroomtoplevel)
app.roommanager.set_commandforbookroombutton(create_bookroomtoplevel)
app.employeemanager.set_commandforaddemployees(create_addemployees_toplevel)
app.employeemanager.set_commandforremoveemployees(create_removeemployees_toplevel)

app.mainloop()
