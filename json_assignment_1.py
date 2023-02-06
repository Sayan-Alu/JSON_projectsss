


import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def __repr__(self):
        return f"Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"

# Inputing a sample employee data in JSON format
employee_data = [
    {
        "Name": "sayan",
        "DOB": "01/01/1998",
        "Height": "5ft",
        "City": "arambagh",
        "State": "WB"
    },
    {
        "Name": "babli",
        "DOB": "04/01/1999",
        "Height": "4ft 7in",
        "City": "kolkata",
        "State": "WB"
    },
    {
        "Name": "kisu",
        "DOB": "05/15/1990",
        "Height": "6ft 2in",
        "City": "delhi",
        "State": "DELHI"
    },
    {
        "Name": "arka",
        "DOB": "01/12/2000",
        "Height": "6ft 5in",
        "City": "lucknow",
        "State": "UP"
    },
    {
        "Name": "Sumon",
        "DOB": "23/11/1996",
        "Height": "5ft 8in",
        "City": "mumbai",
        "State": "MAHARASTRA"
    }
]

# write employee data to employee.json file

with open("employee.json", "w") as f:            
    f.write(json.dumps(employee_data, indent=10))

# read employee data from employee.json file

with open("employee.json", "r") as f:
    employee_data = json.load(f)

# create a list of Employee objects
employee_objects = []
for emp in employee_data:
    emp_obj = Employee(emp["Name"], emp["DOB"], emp["Height"], emp["City"], emp["State"],)
    employee_objects.append(emp_obj)

# print the list of Employee objects
print(employee_objects)