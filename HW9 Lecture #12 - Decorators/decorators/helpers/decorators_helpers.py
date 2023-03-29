def is_email_valid(func):
    def wrapper(email, y, a, z):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(email, y, a, z)
            else:
                print("Email invalid without dot!!!!")
        else:
            print("Email invalid without @ !!!!")
    return wrapper


def is_phone_valid(func):
    def wrapper(y, a, z, phone):
        if len(phone) == 13 and phone[0] == '+':
            func(y, a, z, phone)
        elif len(phone) == 10:
            func(y, a, z, phone)
        else:
            print('Phone number is wrong.'
                  'The phone number must be in the format (+380*********) or (0*********)!!!')
    return wrapper