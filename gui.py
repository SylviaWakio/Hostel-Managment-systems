from tkinter import *
from tkinter.scrolledtext import ScrolledText

class Base():
    """
    Class to be inherited by all the widgets in GUI for uniformity
    """
    background = "#191919"
    foreground = "#ECDBBA"
    labelframefont = "halvatica 10"
    normalfont = "halvatica 30"
    normalfont2 = "halvatica 10 "
    entryforeground = "#ECDBBA"
    entrybackground = "#C84B31"
    buttonbackground = "#2D4263"
    buttonforeground = "#ECDBBA"

    def Create_Welcome_Label(self, master):
        """
        Shows welcome label
        """
        Label(master, text="Hostel Management System", foreground=self.foreground, background=self.background,
              font="Halvatica 50").pack(pady="30")


class LoginFrame(LabelFrame, Base):
    def __init__(self, master):
        """
        Class for handling login page in GUI
        Inherited from LabelFrame
        """
        super().__init__(master=master, background=self.background, foreground=self.foreground,
                         font=self.labelframefont, text="Login")
        self.Create_Welcome_Label(self.master)
        self.loginbutton, self.usernameentry, self.passwordentry = self.Create_Entrys_And_Buttons()

    def Create_Entrys_And_Buttons(self):
        """
        Creates entry, buttons and returns necessary ones
        :return loginbutton, usernameentry, passwordentry:
        """
        usernameentry = Entry(self, foreground=self.entryforeground, background=self.entrybackground,
                              font=self.normalfont)
        passwordentry = Entry(self, foreground=self.entryforeground, background=self.entrybackground,
                              font=self.normalfont, show="*")
        Label(self, text="Username : ", foreground=self.foreground, background=self.background,
              font=self.normalfont).grid(row=0, column=0, padx=20, pady=5)
        Label(self, text="Password : ", foreground=self.foreground, background=self.background,
              font=self.normalfont).grid(row=1, column=0, padx=20, pady=5)
        usernameentry.grid(row=0, column=1, padx=20, pady=5, sticky=EW)
        passwordentry.grid(row=1, column=1, padx=20, pady=5, sticky=EW)
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)
        loginbutton = Button(self, text="Login", background=self.buttonbackground, foreground=self.buttonforeground,
                             font=self.normalfont)
        loginbutton.grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky='ew')
        return loginbutton, usernameentry, passwordentry

    def set_logincommand(self, command):
        self.loginbutton["command"] = lambda: command(self.usernameentry.get(), self.passwordentry.get())

    def rebuild(self):
        """
        Function to clear entries after log out
        """
        self.usernameentry.delete(0, END)
        self.passwordentry.delete(0, END)


class MainFrame(LabelFrame, Base):
    def __init__(self, master):
        """
        Class to create MainPage of the app
        """
        super().__init__(master=master, background=self.background, font=self.labelframefont, text="Functions",
                         labelanchor="n", foreground=self.foreground)
        self.master = master
        self.create_buttons_and_welcome_label()

    def create_buttons_and_welcome_label(self):
        self.roommanagementbutton = Button(self, text="Room Management", background=self.buttonbackground,
                                           foreground=self.buttonforeground, font=self.normalfont,)
        self.feedbackmanagementbutton = Button(self, text="FeedBack Management", background=self.buttonbackground,
                                               foreground=self.buttonforeground, font=self.normalfont,)
        self.empolyeemanagementbutton = Button(self, text="Employee Management", background=self.buttonbackground,
                                               foreground=self.buttonforeground, font=self.normalfont,)
        self.viewstudentbutton = Button(self, text="View Students", background=self.buttonbackground,
                                        foreground=self.buttonforeground, font=self.normalfont,)
        self.changeUPbutton = Button(self, text="Change Username/Password", background=self.buttonbackground,
                                     foreground=self.buttonforeground, font=self.normalfont,)
        self.logoutbutton = Button(self, text="Log-out", background=self.buttonbackground,
                                   foreground=self.buttonforeground, font=self.normalfont,)
        self.buttons = (self.roommanagementbutton, self.feedbackmanagementbutton, self.empolyeemanagementbutton,
                        self.viewstudentbutton, self.changeUPbutton, self.logoutbutton)
        for i in self.buttons:
            i.pack(expand=True, fill=X, pady=5, padx=7)

    def pack1(self, *arr):
        self.Create_Welcome_Label(self.master)
        self.pack(*arr)

    def set_command_for_button(self, buttoncode, command):
        """
        Class to set commands for button.
        :param buttoncode: (int) code to distinguish number and button
        :param command: function
        """
        self.buttons[buttoncode]["command"] = command


class ChangeUsernamePassword(Toplevel, Base):
    def __init__(self):
        """
        Class to handle GUI for changing usernames and passwords
        """
        super().__init__(background=self.background)
        self.title = "ChangeUsernamePassword"

        self.changebutton, self.oldusernameentry, self.oldpasswordentry, self.newusernameentry, self.newpasswordentry = self.create_entrysandbuttons()

    def create_entrysandbuttons(self):
        """
        Creates buttons and entries and returns some of them
        :return changebutton, oldusernameentry, oldpasswordentry, newusernameentry, newpasswordentry:
        """
        oldpasswordentry = Entry(self, foreground=self.entryforeground, background=self.entrybackground,
                                 font=self.normalfont2, show="*")
        oldusernameentry = Entry(self, foreground=self.entryforeground, background=self.entrybackground,
                                 font=self.normalfont2)
        newusernameentry = Entry(self, foreground=self.entryforeground, background=self.entrybackground,
                                 font=self.normalfont2)
        newpasswordentry = Entry(self, foreground=self.entryforeground, background=self.entrybackground,
                                 font=self.normalfont2, show="*")

        Label(self, text="OldUsername : ", foreground=self.foreground, background=self.background,
              font=self.normalfont2).grid(row=0, column=0, padx=20, pady=5)
        Label(self, text="NewUsername : ", foreground=self.foreground, background=self.background,
              font=self.normalfont2).grid(row=1, column=0, padx=20, pady=5)
        Label(self, text="OldPassword : ", foreground=self.foreground, background=self.background,
              font=self.normalfont2).grid(row=2, column=0, padx=20, pady=5)
        Label(self, text="NewPassword : ", foreground=self.foreground, background=self.background,
              font=self.normalfont2).grid(row=3, column=0, padx=20, pady=5)

        oldusernameentry.grid(row=0, column=1, padx=20, pady=5, sticky=EW)
        newusernameentry.grid(row=1, column=1, padx=20, pady=5, sticky=EW)
        oldpasswordentry.grid(row=2, column=1, padx=20, pady=5, sticky=EW)
        newpasswordentry.grid(row=3, column=1, padx=20, pady=5, sticky=EW)
        changebutton = Button(self, text="Change", background=self.buttonbackground, foreground=self.buttonforeground,
                              font=self.normalfont2,)
        changebutton.grid(row=4, column=0, columnspan=2, padx=20, pady=5, sticky='ew')

        return changebutton, oldusernameentry, oldpasswordentry, newusernameentry, newpasswordentry

    def set_changebuttoncommand(self, command):
        self.changebutton["command"] = lambda: command(self.oldusernameentry.get(), self.oldpasswordentry.get(),
                                                       self.newusernameentry.get(), self.newpasswordentry.get())
class FeedbackManager(Frame, Base):

    def __init__(self):
        """
        Class to display and add feedbacks
        """
        super().__init__(background=self.background)
        self.create_widgets()

    def create_widgets(self):
        L1 = LabelFrame(self, font=self.labelframefont, background=self.background, foreground=self.foreground,
                        text="FeedBacks")
        old_feedbacks = ScrolledText(L1, background=self.entrybackground, foreground=self.entryforeground,
                                     font=self.normalfont2)
        self.old_feedbacks = old_feedbacks
        self.old_feedbacks['state'] = DISABLED
        self.old_feedbacks.pack(fill="both", expand=True)

        L1.grid(row=0, column=0, sticky=NSEW, rowspan=2, padx=5, pady=5)

        L2 = LabelFrame(self, font=self.labelframefont, background=self.background, foreground=self.foreground,
                        text="AddFeedBacks")
        self.add_feedback_section = ScrolledText(L2, background=self.entrybackground, foreground=self.entryforeground,
                                                font=self.normalfont2)
        self.add_feedback_section.pack(fill=BOTH, expand=True)
        L2.grid(row=0, column=1, sticky=NSEW, columnspan=4, padx=4, pady=4)
        self.addfeedbackbutton = Button(self, text="AddFeedBack", background=self.buttonbackground,
                                        foreground=self.buttonforeground, font=self.normalfont2)
        self.addfeedbackbutton.grid(row=1, column=3, sticky=NSEW, padx=2, pady=2)
        self.backbutton = Button(self, text="Back", background=self.buttonbackground, foreground=self.buttonforeground,
                                 font=self.normalfont2)
        self.backbutton.grid(row=1, column=4, sticky="news", padx=2, pady=2)

        Label(self, text="Given By : ", foreground=self.foreground, background=self.background,
              font=self.normalfont2).grid(row=1, column=1, sticky="news")
        self.givenbyentry = Entry(self, foreground=self.entryforeground, background=self.entrybackground,
                                  font=self.normalfont2)
        self.givenbyentry.grid(row=1, column=2, sticky="news")

        self.rowconfigure(0, weight=3)
        self.columnconfigure(0, weight=1)

    def display_feedbacks(self, feedbacks):
        """
        displays the feedbacks
        :param feedbacks: list
        """
        self.old_feedbacks["state"] = NORMAL
        for feedback in feedbacks:
            self.old_feedbacks.insert(END, "Given By : " + feedback["name"] + "\n")
            self.old_feedbacks.insert(END, feedback["feedbacktext"] + "\n")
        self.old_feedbacks["state"] = DISABLED

    def set_commandforaddfeedbackbuttons(self, command):
        """
            :param command: function
        """
        self.addfeedbackbutton["command"] = lambda: command(
            {"name": self.givenbyentry.get(), "feedbacktext": self.add_feedback_section.get(0.0, END)})

    def set_commandforbackbutton(self, command):
        """
            :param command: function
        """
        self.backbutton["command"] = command
class EmployeeManager(LabelFrame, Base):
    def __init__(self, master):
        """
        Class to view Employees and add or remove employees
        """
        super().__init__(master=master, background=self.background, foreground=self.foreground, font=self.labelframefont, text="Employees : ")
        self.create_widgets()

    def create_widgets(self):
        self.viewemployees = ScrolledText(self, background=self.entrybackground, foreground=self.entryforeground, font=self.normalfont2)
        self.viewemployees.grid(row=0, column=0, columnspan=3, sticky="news")
        self.viewemployees["state"] = DISABLED
        self.backbutton = Button(self, text="Back", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont2)
        self.backbutton.grid(row=1, column=2, sticky="news", padx=2, pady=2)

        self.addempolyeebutton = Button(self, text="AddEmployee", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont2)
        self.addempolyeebutton.grid(row=1, column=0, sticky="news", padx=2, pady=2)

        self.removeempolyeebutton = Button(self, text="RemoveEmployee", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont2)
        self.removeempolyeebutton.grid(row=1, column=1, sticky="news", padx=2, pady=2)

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1)

    def display_employees(self, employees):
        """
        displays the feedbacks
        :param rooms: list
        """
        self.viewemployees["state"] = NORMAL
        for employee in employees:
            for key, value in employee.items():
                try:
                    self.viewemployees.insert(END, key + " : " + value + "\n")
                except:
                    pass
            self.viewemployees.insert(END, "\n")
        self.viewemployees["state"] = DISABLED

    def set_commandforbackbutton(self, command):
        """
            :param command: function
        """
        self.backbutton["command"] = command

    def set_commandforaddemployees(self, command):
        self.addempolyeebutton["command"] = command

    def set_commandforremoveemployees(self, command):
        self.removeempolyeebutton["command"] = command
class AddEmployeeToplevel(Toplevel, Base):
    def __init__(self):
        """
        Top Level To add employees
        """
        super().__init__(background=self.background)
        self.required_values = ["Name", "Email Address", "Phone Number", "Post", "Qualification"]
        self.create_widgets()

    def create_widgets(self):
        entrys = []
        for i in range(len(self.required_values)):
            Label(self, text=self.required_values[i] + " : ", foreground=self.foreground, background=self.background, font=self.normalfont2).grid(row=i, column=0, sticky="news")
            e = Entry(self, foreground=self.entryforeground, background=self.entrybackground, font=self.normalfont)
            e.grid(row=i, column=1, sticky="news")
            entrys.append(e)
        self.entrys = entrys
        self.addemployeebutton = Button(self, text="Add", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont)
        self.addemployeebutton.grid(row=len(self.required_values) + 1, column=0, columnspan=2, sticky=NSEW)

    def set_addemployeebuttoncommand(self, command):
        employee_dict = {}
        for i in range(len(self.required_values)):
            employee_dict[self.required_values[i]] = self.entrys[i]
        self.addemployeebutton["command"] = lambda: command(employee_dict)
class RemoveEmployeeToplevel(Toplevel, Base):
    def __init__(self):
        """
        Top Level To remove employees
        """
        super().__init__(background=self.background)
        self.required_values = ["Name", ]
        self.create_widgets()

    def create_widgets(self):
        entrys = []
        for i in range(len(self.required_values)):
            Label(self, text=self.required_values[i] + " : ", foreground=self.foreground, background=self.background, font=self.normalfont2).grid(row=i, column=0, sticky="news")
            e = Entry(self, foreground=self.entryforeground, background=self.entrybackground, font=self.normalfont)
            e.grid(row=i, column=1, sticky="news")
            entrys.append(e)
        self.entrys = entrys
        self.removeemployeebutton = Button(self, text="Remove", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont)
        self.removeemployeebutton.grid(row=len(self.required_values) + 1, column=0, columnspan=2, sticky=NSEW)

    def set_removeemployeebuttoncommand(self, command):
        employee_dict = {}
        print("hell")
        for i in range(len(self.required_values)):
            employee_dict[self.required_values[i]] = self.entrys[i]
        self.removeemployeebutton["command"] = lambda: command(employee_dict[self.required_values[0]])
class RoomManager(LabelFrame, Base):
    def __init__(self, master):
        """
        Class to view rooms, add, remove, or book rooms
        """
        super().__init__(master=master, background=self.background, foreground=self.foreground, font=self.labelframefont, text="Rooms : ")
        self.create_widgets()

    def create_widgets(self):
        self.viewrooms = ScrolledText(self, background=self.entrybackground, foreground=self.entryforeground, font=self.normalfont2)
        self.viewrooms.grid(row=0, column=0, columnspan=4, sticky="news")
        self.viewrooms["state"] = DISABLED
        self.backbutton = Button(self, text="Back", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont2)
        self.backbutton.grid(row=1, column=3, sticky="news", padx=2, pady=2)

        self.addroombutton = Button(self, text="AddRoom", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont2)
        self.addroombutton.grid(row=1, column=0, sticky="news", padx=2, pady=2)

        self.removeroombutton = Button(self, text="RemoveRoom", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont2)
        self.removeroombutton.grid(row=1, column=1, sticky="news", padx=2, pady=2)

        self.bookroombutton = Button(self, text="BookRoom", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont2)
        self.bookroombutton.grid(row=1, column=2, sticky="news", padx=2, pady=2)

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1)

    def display_rooms(self, rooms):
        """
        Displays the feedbacks
        :param rooms: list
        """
        self.viewrooms["state"] = NORMAL
        for room in rooms:
            for key, value in room.items():
                try:
                    if key != "_id":
                        self.viewrooms.insert(END, key + " : " + str(value) + "\n")
                except Exception as e:
                    print(e)
            self.viewrooms.insert(END, "\n")
        self.viewrooms["state"] = DISABLED

    def set_commandforbackbutton(self, command):
        """
        :param command: function
        """
        self.backbutton["command"] = command

    def set_commandforaddroombutton(self, command):
        """
        :param command: function
        """
        self.addroombutton["command"] = command

    def set_commandforremoveroombutton(self, command):
        """
        :param command: function
        """
        self.removeroombutton["command"] = command

    def set_commandforbookroombutton(self, command):
        """
        :param command: function
        """
        self.bookroombutton["command"] = command
class addroomtoplevel(Toplevel, Base):
    def __init__(self):
        """
        Top Level To add employees
        """
        super().__init__(background=self.background)
        self.required_values = ["Room Id", "Room Description"]
        self.create_widgets()

    def create_widgets(self):
        entrys = []
        for i in range(len(self.required_values)):
            Label(self, text=self.required_values[i] + " : ", foreground=self.foreground, background=self.background, font=self.normalfont2).grid(row=i, column=0, sticky="news")
            e = Entry(self, foreground=self.entryforeground, background=self.entrybackground, font=self.normalfont)
            e.grid(row=i, column=1, sticky="news")
            entrys.append(e)
        self.entrys = entrys
        self.addroombutton = Button(self, text="Add", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont)
        self.addroombutton.grid(row=len(self.required_values) + 1, column=0, columnspan=2, sticky=NSEW)

    def set_addroombuttoncommand(self, command):
        dict = {}
        for i in range(len(self.required_values)):
            dict[self.required_values[i]] = self.entrys[i]
        self.addroombutton["command"] = lambda: command(dict)
class removeroomtoplevel(Toplevel, Base):
    def __init__(self):
        """
        Top Level To add employees
        """
        super().__init__(background=self.background)
        self.required_values = ["Room Id"]
        self.create_widgets()

    def create_widgets(self):
        entrys = []
        for i in range(len(self.required_values)):
            Label(self, text=self.required_values[i] + " : ", foreground=self.foreground, background=self.background, font=self.normalfont2).grid(row=i, column=0, sticky="news")
            e = Entry(self, foreground=self.entryforeground, background=self.entrybackground, font=self.normalfont)
            e.grid(row=i, column=1, sticky="news")
            entrys.append(e)
        self.entrys = entrys
        self.removeroombutton = Button(self, text="Remove", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont)
        self.removeroombutton.grid(row=len(self.required_values) + 1, column=0, columnspan=2, sticky=NSEW)

    def set_removeroombuttoncommand(self, command):
        self.removeroombutton["command"] = lambda: command(self.entrys[0])
class bookroomtoplevel(Toplevel, Base):
    def __init__(self):
        """
        Top Level To Book Room
        """
        super().__init__(background=self.background)
        self.required_values = ["Room Id", "Name", "Email Address", "Phone Number", "Student Id", "Booked For"]
        self.create_widgets()

    def create_widgets(self):
        entrys = []

        for i in range(len(self.required_values)):
            Label(self, text=self.required_values[i] + " : ", foreground=self.foreground, background=self.background, font=self.normalfont2).grid(row=i, column=0, sticky="news", padx=5, pady=5)
            e = Entry(self, foreground=self.entryforeground, background=self.entrybackground, font=self.normalfont)
            e.grid(row=i, column=1, sticky="news", padx=5, pady=5)
            entrys.append(e)
        self.entrys = entrys
        self.bookroombutton = Button(self, text="Book Room", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont)
        self.bookroombutton.grid(row=len(self.required_values), column=0, columnspan=2, sticky=NSEW)

    def set_bookroombuttoncommand(self, command):
        dict = {}
        for i in range(len(self.required_values)):
            dict[self.required_values[i]] = self.entrys[i]
        self.bookroombutton["command"] = lambda: command(dict)
class ViewStudentsFrame(LabelFrame, Base):
    def __init__(self, master):
        """
        Class to view Students
        """
        super().__init__(master=master, background=self.background, foreground=self.foreground, font=self.labelframefont, text="Students : ")
        self.create_widgets()

    def create_widgets(self):
        self.viewstudents = ScrolledText(self, background=self.entrybackground, foreground=self.entryforeground, font=self.normalfont2)
        self.viewstudents.grid(row=0, column=0, columnspan=3, sticky="news")
        self.viewstudents["state"] = DISABLED
        self.backbutton = Button(self, text="Back", background=self.buttonbackground, foreground=self.buttonforeground, font=self.normalfont2)
        self.backbutton.grid(row=1, column=2, sticky="news", padx=2, pady=2)

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1)

    def display_students(self, students):
        """
        displays the feedbacks
        :param rooms: list
        """
        self.viewstudents["state"] = NORMAL
        for employee in students:
            for key, value in employee.items():
                try:
                    self.viewstudents.insert(END, key + " : " + value + "\n")
                except:
                    pass
            self.viewstudents.insert(END, "\n")
        self.viewstudents["state"] = DISABLED

    def set_commandforbackbutton(self, command):
        """
        :param command: function
        """
        self.backbutton["command"] = command
class App(Tk, Base):
    def __init__(self):
        """
        Main class of gui which handles all UI activities
        """
        super().__init__()
        self.title("Hostel Management System")
        self.geometry("1350x700")

        self.config(background=self.background)
        self.mainframe = MainFrame(self)
        self.loginframe = LoginFrame(self)
        self.feedbackmanager = FeedbackManager()
        self.employeemanager = EmployeeManager(self)
        self.roommanager = RoomManager(self)
        self.viewstudentsframe = ViewStudentsFrame(self)
        self.create_loginframe()

    def create_mainframe(self):
        self.mainframe.pack1()

    def create_loginframe(self):
        self.loginframe.pack(expand=True, fill=X, padx=300, ipadx=20, ipady=20)

    def create_feedbackmanager(self):
        self.feedbackmanager.pack(fill=BOTH, expand=True)

    def clear_window(self):
        """
        clears all the widgets from the window
        """
        for widget in self.pack_slaves():
            widget.pack_forget()

    def create_changeusernamepassword(self):
        self.changeusernamepasswordtoplevel = ChangeUsernamePassword()

    def create_addemployeestoplevel(self):
        self.addemployeestoplevel = addemployeetoplevel()

    def create_removeemployeestoplevel(self):
        self.removeemployeestoplevel = removeempolyeetoplevel()

    def create_employeemanager(self):
        self.clear_window()
        self.employeemanager.pack(fill=BOTH, expand=True)

    def create_roommanager(self):
        self.clear_window()
        self.roommanager.pack(fill=BOTH, expand=True)

    def create_viewstudents(self):
        self.clear_window()
        self.viewstudentsframe.pack(fill=BOTH, expand=True)

    def create_addroomtoplevel(self):
        self.addroomtoplevel = addroomtoplevel()

    def create_removeroomtoplevel(self):
        self.removeroomtoplevel = removeroomtoplevel()

    def create_bookroomtoplevel(self):
        self.bookroomroplevel = bookroomtoplevel()

    def log_out(self):
        self.clear_window()
        self.loginframe.rebuild()
        self.create_loginframe()

    def log_in(self):
        self.clear_window()
        self.create_mainframe()

    def start_feedbackmanager(self):
        self.clear_window()
        self.create_feedbackmanager()

    def backtomainframe(self):
        self.clear_window()
        self.create_mainframe()

