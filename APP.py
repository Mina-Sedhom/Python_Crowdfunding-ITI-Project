###### must be Login
import regist as reg
import login as lo
import dbhandler as h
import addproject as p



if __name__ == '__main__':
    choice = input("""\n please enter:
                                    0 to exit the app
                                    1 to Register
                                    2 to login
                                    3 to add new project
                                    4 to view all projects
                                    5 to edit any of your projects
                                    6 to delete of your projects
                                    7 search for a project using date 
                                    8 log out  \n""") 

    while True:
        if choice == '0':
            break

        elif choice == '1':#Register
            if lo.is_session_opned():
                print("Hi!!!! you are already loged in")
            else:
                reg.get_user_info()
                print("Great you can Login Now")

        elif choice == '2':#login
            if lo.is_session_opned():
                print("Hi!!!! you are already loged in")
            else:
                lo.user_login()#ok


        elif choice == '3':#add new project
            if lo.is_session_opned():
                p.get_project_info()
            else:
                print("Login first please to add new project")
                
        elif choice == '4':#view all projects
            h.veiw_all_projects()

        elif choice == '5':#edit
            if lo.is_session_opned():
                h.edit_project()
            else:
                print("Login first please to edit your projects")

        elif choice == '6':#delete
            if lo.is_session_opned():
                h.delete_project()
            else:
                print("Login first please delete your projects")

        elif choice == '7':#search
            h.search_project()
        elif choice == '8':#log out
            if lo.is_session_opned():
                lo.logout()
            else:
                print("Hi!!!! you are already not Logged in")
        else:
            print("Enter a Valid choice please")
        choice = input("""\n please enter:
                                        0 to exit the app
                                        1 to Register
                                        2 to login
                                        3 to add new project
                                        4 to view all projects
                                        5 to edit any of your projects
                                        6 to delete of your projects
                                        7 search for a project using date
                                        8 log out  \n""")
