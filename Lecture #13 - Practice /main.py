from helpers import save, get_employee_by_phone_number, get_all_employers, get_employee_by_email, \
    get_all_plants, get_plant_by_id, get_salon_by_id, update, save_plant, save_salon, save_sales_departament, \
    delete_employee


while True:
    try:
        print("1.Add new Employee\n2.Get all Employees\n3.Get employee by email\n4.Get employee by phone number\n"
              "5.Update Employee\n6.Add plant\n7.Get all plants\n8.Get plant by id\n9.Add salon\n"
              "10.Add sales departament\n11.Delete Employee")

        flag = int(input('Select a menu item or enter 0 to exit: '))

        if flag == 0:
            break

        if flag == 1:
            email = input("Employee email: ")
            first_name = input("Employee first name: ")
            last_name = input("Employee last name: ")
            phone_number = input("Employee phone number: ")
            work_id = int(input("Employee work id: "))
            type = input("Employee work type: ")
            save(email, first_name, last_name, phone_number, work_id, type)

        elif flag == 2:
            get_all_employers()

        elif flag == 3:
            email_to_find = input("Type email of employee which you want to find: ")
            employee = get_employee_by_email(email_to_find)

            print("1.Display info about place of work.\n0.Exit")
            flag_inner = int(input("Your choose: "))
            if flag_inner == 1:
                if employee["type"] == "plant":
                    get_plant_by_id(int(employee["work_id"]))
                elif employee["type"] == "salon":
                    get_salon_by_id(int(employee["work_id"]))
            else:
                continue

        elif flag == 4:
            phone_to_find = input("Type phone of employee which you want to find: ")
            get_employee_by_phone_number(phone_to_find)

        elif flag == 5:
            id = int(input("Type a id of user which you want to update: "))
            update(id)

        elif flag == 6:
            name = input("Type a name of Plant: ")
            address = input("Type an address of Plant: ")
            save_plant(name, address)

        elif flag == 7:
            get_all_plants()

        elif flag == 8:
            id = int(input("Id of plant: "))
            get_plant_by_id(id)

        elif flag == 9:
            name = input("Type a name of Salon: ")
            address = input("Type an address of Salon: ")
            save_salon(name, address)

        elif flag == 10:
            name = input("Type a name of sales departament: ")
            address = input("Type an address of sales departament: ")
            save_sales_departament(name, address)

        elif flag == 11:
            id = int(input("Id of element which you want to delete: "))
            delete_employee(id)

        else:
            print("\n***!!!!!!!!!!!!!***")
            print("Invalid input!!!\nPlease enter a number between 0 and 11.")
            print("***^^^^^^^^^^^^^^^***\n")

    except ValueError:
        print("\n***!!!!!!!!!!!!!***")
        print("Invalid input!!!\nPlease enter a number.")
        print("***^^^^^^^^^^^^^^^***\n")
        continue
    print("===============================================================================")
