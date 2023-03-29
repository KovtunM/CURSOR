from helpers import *

while True:
    print('Enter "0" to exit.')
    print("1.Add new Employee\n"
          "2.Get all Employees\n"
          "3.Get employee by email\n"
          "4.Get employee by phone number\n"
          "5.Update by last name")
    flag = input("Choose menu item: ")
    if flag == "0":
        break
    if flag == "1":
        email = input("Employee email: ")
        first_name = input("Employee first name: ")
        last_name = input("Employee last name: ")
        phone = input("Employee phone number: ")
        save(email, first_name, last_name, phone)
    elif flag == "2":
        get_all_employers()
    elif flag == "3":
        email_to_find = input("Type email of employee which you want to find: ")
        get_employee_by_email(email_to_find)
    elif flag == "4":
        phone_to_find = input("Type phone of employee which you want to find: ")
        get_employee_by_phone_number(phone_to_find)
    elif flag == "5":
        last_name = input("Type last name of employee which you want to update: ")
        update_by_last_name(last_name)
