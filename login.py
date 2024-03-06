import dbhandler as h

###############################################################################
###############################################################################
#Check if the info is in the database and create a session by storing the user id 
###############################################################################
###############################################################################

u_id = None




def user_login():
    global u_id 

    print('\n##### welcome to Log in ############')
    email = input('Please enter your Email: ')
    passw = input('Please enter your Password: ')
    all = h.get_all_users()

    if all == []:#if DB is empty
        print('Register First please')
    else:
        for i in all:
            if i["email"] == email and i["password"] == passw:
                    u_id = i["user_id"]
                    print("#### Welcome Again ###")
                    break
    if not u_id :
        print('Wrong Email or Password or Both')

######

def is_session_opned():
    global u_id
    return u_id


def logout():
     global u_id
     u_id = None
