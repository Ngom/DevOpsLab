from string import punctuation, digits, ascii_letters

# The simplest function to get the user email (copy to src/user_functions.py)
# def get_email_from_input():
#    """ Contains '@' and '.' """
#    return input("Tell me your email: ")

# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """

    email = str(input("Tell me your email: "))
    # double negation is always true !!!
    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

# Do the same for the following functions
# Functions in src/user_functions.py and tests in tests/test_user_functions.py
def get_user_name_from_input():
    """ Not empty string. No spaces. """

    uname = input("Create your user name: ")
    # double negation is always true !!!
    if (uname == "") or (" " in uname):
        print("User_name is not correct")
    else:
        return uname

def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """

    password = input("Create your password: ")
    # list of special in password should not be empty
    list_sp_char = [password.find(i) for i in list(punctuation) if password.find(i) != -1]
    # list of digits in password should not be empty
    list_digits = [password.find(i) for i in list(digits) if password.find(i) != -1]
    # list of letters in password not be empty
    list_abc = [password.find(a) for a in list(ascii_letters) if password.find(a) != -1]

    # double negation is always true !!!
    if len(password) < 8 or (len(list_sp_char) == 0) or (len(list_digits) == 0) or (len(list_abc) == 0):
        print('Password is not valid')
    else:
        return password
