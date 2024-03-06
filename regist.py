import re
import  time
import dbhandler as h
'''
1 - Authentication System:
• Registration:
• First name
• Last name
• Email
• Password
• Confirm password
• Mobile phone [validated against Egyptian phone numbers] 
• Login
• The user should be able to login after activation using his email 
and password


'''


def generate_id():
    "generate random id "
    id= time.time()
    # print(round(id))
    return round(id)





def is_valid_email(email):
    while True:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):#will return a match object, which is truthy. In this case, the function will return True, else none.
            email = input('please enter valid Email: ')
        else:
            return email



def get_user_info():
    print('\n#####   welcome in Registration   ########')
    user_id = generate_id()
    f_name = input('Enter your first name: ')

    l_name = input('Enter your last name: ')

    email = input('Enter your email: ')###check if time
    email = is_valid_email(email)
    
    passw = input('Enter your  password: ')
    conf_pasw = input('confirm your  password: ')
    while conf_pasw != passw:
        print('not Matched password Renter Please ')
        passw = input('Enter your  password: ')
        conf_pasw = input('confirm your  password: ')

    phone = input('enter your phone number ')
    while True:
        if not re.match(r"[+20]+[0-9]", phone) or len(phone) != 13:#will return a match object, which is truthy. In this case, the function will return True, else none.
            print('not valid Egyptian phone numbers')
            phone = input('please enter valid Egyptian phone numbers: ')
        else:
            break

    userdata = {"user_id":user_id,
            "f_name": f_name,
            "l_name": l_name,
            "email": email, 
            "password": passw,
            "phone":phone}
    
    h.save_new_user(userdata)