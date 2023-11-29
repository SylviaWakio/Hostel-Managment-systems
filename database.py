from pymongo import MongoClient
class DataBaseManager():
    def __init__(self):
        """
            Class to manage database
        """
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["Hostel_Management_System"]
        self.RoomsCollection = self.db["rooms"]
        self.AdminCollection = self.db["admins"]
        self.StudentCollection = self.db["students"]
        self.FeedBackCollection = self.db["feedBacks"]
        self.EmployeeCollection = self.db["employees"]
 
    def add_room(self,dict):
        dict["aviliability"] = "aviliable"
        dict["bookedfor"] = 0
        self.RoomsCollection.insert_one(dict)
 
    def book_room(self,dict):
        doc = self.RoomsCollection.find_one({"Room Id":dict["Room Id"]})
        doc["aviliability"] = "Occupied By " + dict["Name"]
        doc["bookedfor"] = dict["Booked For"]
        print(doc)
        self.RoomsCollection.find_one_and_replace({"Room Id":dict["Room Id"]},doc)
        self.StudentCollection.insert_one(dict)
 
 
    def check_authentication(self,username,password):
        dbusername = self.AdminCollection.find_one()["username"]
        dbpassword = self.AdminCollection.find_one()["password"]
        return username == dbusername and password == dbpassword
 
    def change_authentication_details(self,newusername,newpassword):
        doc = dict(self.AdminCollection.find_one())
        doc["username"] = newusername
        doc["password"] = newpassword
        self.AdminCollection.find_one_and_replace({},replacement=doc)
 
    def insert_feedback(self,dict1):
        self.FeedBackCollection.insert_one(dict1)
 
 
    def get_feedbacks(self):
        feedbacks = []
        for document in self.FeedBackCollection.find():
            feedbacks.append(document)
        return feedbacks
 
    def get_employees(self):
        employees = []
        for document in self.EmployeeCollection.find():
            employees.append(document)
        return employees
   
    def get_students(self):
        students = []
        for document in self.StudentCollection.find():
            students.append(document)
        return students
 
    def get_rooms(self):
        rooms = []
        for document in self.RoomsCollection.find():
            rooms.append(document)
        return rooms
 
    def add_employee(self,dict1):
        self.EmployeeCollection.insert_one(dict1)
