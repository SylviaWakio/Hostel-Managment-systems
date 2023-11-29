from gui import *
from database import *
from tkinter.messagebox import showinfo, askokcancel

app = App()
dbm = DataBaseManager()

def check_authentication(username, password):
    admin_document = dbm.AdminCollection.find_one({"username": username, "password": password})
    if admin_document:
        dbusername = admin_document["username"]
        # ... rest of your code
        return True
    else:
        return False

def login(username, password):
    if dbm.check_authentication(username=username, password=password):
        app.log_in()
    else:
        showinfo("Login Error", "Invalid Username or password")

def logout():
    yes = askokcancel(title="Info", message="Are you sure you want to log out? ")
    if yes:
        app.log_out()

def createusernamepassword():
    app.create_changeusernamepassword()
    app.changeusernamepasswordtoplevel.set_changebuttoncommand(changeusernamepassword)

def changeusernamepassword(oldusername, oldpassword, newusername, newpassword):
    if dbm.check_authentication(oldusername, oldpassword):
        dbm.change_authentication_details(newusername, newpassword)
        showinfo(title="Changed", message="Changed Username and Password")
        app.changeusernamepasswordtoplevel.destroy()

def start_feedback():
    app.start_feedbackmanager()
    app.feedbackmanager.display_feedbacks(dbm.get_feedbacks())

def add_feedback(dict):
    dbm.insert_feedback(dict)

def add_employees(dict):
    dict_2 = {}
    for key, value in dict.items():
        dict_2[key] = value.get()

    print(dict_2)
    dbm.add_employee(dict_2)
    app.addemployeestoplevel.destroy()

def remove_employee(entry):
    dbm.EmployeeCollection.delete_one({"Name": entry.get()})
    app.removeemployeestoplevel.destroy()

def remove_room(entry):
    dbm.RoomsCollection.delete_one({"Room Id": entry.get()})
    app.removeroomtoplevel.destroy()

def add_room(dict):
    dict_2 = {}
    for key, value in dict.items():
        dict_2[key] = value.get()
    dbm.add_room(dict_2)
    app.addroomtoplevel.destroy()

def book_room(dict):
    dict_2 = {}
    for key, value in dict.items():
        dict_2[key] = value.get()
    dbm.book_room(dict_2)
    app.bookroomroplevel.destroy()

def create_addemployees_toplevel():
    app.create_addemployeestoplevel()
    app.addemployeestoplevel.set_addemployeebuttoncommand(add_employees)

def create_removeemployees_toplevel():
    app.create_removeemployeestoplevel()
    app.removeemployeestoplevel.set_removeemployeebuttoncommand(remove_employee)

def create_employeemanager():
    app.create_employeemanager()
    app.employeemanager.display_employees(dbm.get_employees())

def create_addroomtoplevel():
    app.create_addroomtoplevel()
    app.addroomtoplevel.set_addroombuttoncommand(add_room)

def create_removeroomtoplevel():
    app.create_removeroomtoplevel()
    app.removeroomtoplevel.set_removeroombuttoncommand(remove_room)

def create_bookroomtoplevel():
    app.create_bookroomtoplevel()
    app.bookroomroplevel.set_bookroombuttoncommand(book_room)

def create_roommanager():
    app.create_roommanager()
    app.roommanager.display_rooms(dbm.get_rooms())

def create_viewstudents():
    app.create_viewstudents()
    app.viewstudentsframe.display_students(dbm.get_students())

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
