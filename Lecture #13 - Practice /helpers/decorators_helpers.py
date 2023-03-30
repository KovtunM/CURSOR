def is_email_valid(func):
    def wrapper(email, y, a, z, c, b):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(email, y, a, z, c, b)
            else:
                print("\n***!!!!!!!!!!!!!***")
                print("Email invalid without dot!!!!")
                print("***^^^^^^^^^^^^^^^***\n")
        else:
            print("\n***!!!!!!!!!!!!!***")
            print("Email invalid without @ !!!!")
            print("***^^^^^^^^^^^^^^^***\n")
    return wrapper


def is_phone_valid(func):
    def wrapper(y, a, z, phone, c, b):
        if len(phone) == 13 and phone[0] == '+':
            func(y, a, z, phone, c, b)
        elif len(phone) == 10:
            func(y, a, z, phone, c, b)
        else:
            print("\n***!!!!!!!!!!!!!***")
            print('Phone number is wrong!!!\n'
                  'The phone number must be in the format (+380*********) or (0*********)!!!')
            print("***^^^^^^^^^^^^^^^***\n")
    return wrapper
