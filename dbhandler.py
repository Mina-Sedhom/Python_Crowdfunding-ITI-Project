import  json
import login as lo
import addproject as ap
##############################
            # user
#############################


def get_all_users():
    try:
        filobject = open("userdb.json", "r")
    except Exception as e:
        print(e)
    else:
        data = filobject.read() # string
        filobject.close()
        data= data.strip('\n')
        
        if data:
            # get valid python data from string
            file_data = json.loads(data)#return python list IF data exist
            return  file_data
        return []

def save_new_user(userdata: dict):
    old_data = get_all_users()  # list
    old_data.append(userdata)
    # convert old_data in list to valid json string
    valid_data = json.dumps(old_data, indent=2)##as json needs " str
    try:
        fileobj = open("userdb.json", "w")
    except Exception as e:
        return  False
    else:
        # saving the data in the file
        fileobj.write(valid_data)
        fileobj.close()
        return  True


##############################
            # project
#############################

def get_all_projects():
    try:
        filobject = open("projectdb.json", "r")
    except Exception as e:
        print(e)
    else:
        data = filobject.read() # string
        filobject.close()
        data= data.strip('\n')
        
        if data:
            # get valid python data from string
            file_data = json.loads(data)#return python list IF data exist
            return  file_data
        return []

def save_new_project(projectdata: dict):
    old_data = get_all_projects()  # list
    old_data.append(projectdata)
    # convert old_data in list to valid json string
    valid_data = json.dumps(old_data, indent=2)
    try:
        fileobj = open("projectdb.json", "w")
    except Exception as e:
        return  False
    else:
        # saving the data in the file
        fileobj.write(valid_data)
        fileobj.close()
        return  True




##############################
            # view all projects
#############################
def veiw_all_projects():
    pl = get_all_projects()  #project list
    for i in pl:
        for x, y in i.items():
            if x != "project_id" and x != "user_id":
                print(f"The project's {x} is: {y}   ",end=' ')
        print('')
    




##############################
            # Edit project
#############################
def edit_project():
    find = False
    if not lo.is_session_opned():## There is must be a user logged in
        return
    p_title = input('Enter the project title you want to edit: ')

    pl = get_all_projects()  #project list
    ind = 0         #index to iterate in list as x is Dict
    for i in pl:
        if p_title == i["title"]:
            find = True
            if lo.is_session_opned() != i["user_id"]:
                print("NOT allowed")
                return  ## so only each user can edit his own projects
            for x, y in i.items():
                
                if x != "project_id" and x != "user_id":#user can't change this
                    print("!!! Enter '1' to change, '0' to leave as it !!!" )
                    c = input(f"The project's {x} is {y} , Do you want to change it ? ")
                    if c == '1':
                        if x == "sdate" or x == "edate":
                            kk = input(f'Enter the new {x} : ')
                            pl[ind][x] = ap.convert_valid_date(kk)
                        elif x == "target":
                            kk = input(f'Enter the new {x} : ')
                            pl[ind][x] = ap.convert_valid_target(kk)
                        else:
                            pl[ind][x] = input(f'Enter the new {x} : ')
        ind +=1
    # convert Edited_data in list to valid json string
    if find == False:
        print("No such prject")
    valid_data = json.dumps(pl, indent=2)
    try:
        fileobj = open("projectdb.json", "w")
    except Exception as e:
        return  False
    else:
        # saving the data in the file
        fileobj.write(valid_data)
        fileobj.close()
        return  True




##############################
            # delete
#############################
def delete_project():
    deleted = False
    if not lo.is_session_opned():## There is must be a user logged in
        return
    p_title = input('Enter the project title you want to delete: ')

    pl = get_all_projects()  #project list
    ind = 0         #index to iterate in list ,as x is Dict
    for i in pl:
        if p_title == i["title"]:
            if lo.is_session_opned() != i["user_id"]:
                print("NOT allowed")
                return  ## so only each user can edit his own projects
            pl.pop(ind)
            deleted = True
        ind +=1

    # convert Edited_data in list to valid json string
    if deleted == False:
        print('There is no such project for you')####################################
    valid_data = json.dumps(pl, indent=2)
    try:
        fileobj = open("projectdb.json", "w")
    except Exception as e:
        return  False
    else:
        # saving the data in the file
        fileobj.write(valid_data)
        fileobj.close()
        return  True







##############################
            # search
#############################
def search_project():
    
    pl = get_all_projects()#project list

    sdate = input('Enter project Start date (m/d/y) to search: ')
    sdate = ap.convert_valid_date(sdate)
    while sdate == False:
        sdate = input('enter valid project Start date (m/d/y) to search: ')
        sdate = ap.convert_valid_date(sdate)

    ind = 0         #index to iterate in list ,as x is Dict
    for i in pl:
        if sdate == i["sdate"]:
            for x, y in i.items():
                if x != "project_id" and x != "user_id":
                    print(f"The project's {x} is: {y}   ",end=' ')
        ind +=1
