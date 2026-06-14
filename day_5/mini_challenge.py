# Create a function that receives a dictionary and print the info 

def get_employee_info(employee):
    return f"{employee['name']} works as {employee['position']} and earns {employee['salary']}."

employee = {
    "name": "John",
    "position": "Data Engineer",
    "salary": 50000,
}

print(get_employee_info(employee))