from .system_helpers import *
from .decorators_helpers import *


@is_phone_valid
@is_email_valid
def save(email, first_name, last_name, phone):
    new_employee = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
    }
    save_to_file(new_employee)


def get_all_employers():
    employees = get_file_data()
    for employee in employees:
        print(employee["email"])
        print(employee["first_name"])
        print(employee["last_name"])
        print(employee["phone"])


def get_employee_by_email(email):
    employees = get_file_data()
    for employee in employees:
        if employee["email"] == email:
            print(employee["email"])
            print(employee["first_name"])
            print(employee["last_name"])
            print(employee["phone"])


def get_employee_by_phone_number(phone):
    employees = get_file_data()
    for employee in employees:
        if employee["phone"] == phone:
            print(employee["email"])
            print(employee["first_name"])
            print(employee["last_name"])
            print(employee["phone"])
        else:
            print("The employee cannot be found at this number.\n"
                  "Try entering the phone number in the format "
                  "(+380*********) or (0*********) or add a new employee.")


def update_by_last_name(last_name):
    employers = get_file_data()
    for employee in employers:
        if employee["last_name"] == last_name:
            employee["email"] = input("Email: ")
            employee["first_name"] = input("First name: ")
            employee["last_name"] = input("Last Name: ")
            employee["phone"] = input("Phone: ")

    file = open("database/employees.json", "w")
    data_in_json = json.dumps(employers)
    file.write(data_in_json)
    file.close()
