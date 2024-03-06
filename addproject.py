'''
 The user can create a project fund raise campaign which contains:
• Title
• Details
• Total target (i.e 250000 EGP)
• Set start/end time for the campaign (validate the date formula)

'''
import re
import  time
import dbhandler as h
import login as lo
from datetime import datetime


def convert_valid_date(date: str):
    try:        
        date = datetime.strptime(date, '%m/%d/%Y').date()#The datetime.strptime() method returns a datetime object that matches the date_string parsed by the format
        date = str(date)
        return date
    except Exception as e:
        print('invalid date')
        return  False    

def convert_valid_target(target: str):
    try:
        target = float(target)
        return target
    except Exception as e:
        print('invalid target value')
        return  False

def generate_id():
    "generate random id "
    id= time.time()
    return round(id)



def get_project_info():
    if not lo.is_session_opned():
        return
    project_id = generate_id()
    user_id = lo.is_session_opned()
    title = input('enter project name: ')
    details = input('enter project Details: ')


    target = input('enter project Target: ')
    target = convert_valid_target(target)
    

    sdate = input('enter project Start date m/d/y: ')
    sdate = convert_valid_date(sdate)
    while sdate == False:
            sdate = input('enter valid project Start date m/d/y: ')
            sdate = convert_valid_date(sdate)

    
    edate = input('enter project End date m/d/y: ')
    edate = convert_valid_date(edate)
    while edate == False:
            edate = input('enter valid project Start date m/d/y: ')
            edate = convert_valid_date(edate)

    projectdata = {"user_id":user_id,
                    "project_id": project_id,
                "title": title,
                "details": details,
                "target": target, 
                "sdate": sdate,
                "edate":edate}

    
    h.save_new_project(projectdata)