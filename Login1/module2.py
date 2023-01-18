import sys

with open('file.txt', 'r') as base:
    data = base.readlines()
 
users = {}
for user in data:
    name = user.split()[0]
    password = user.split()[1]
    users[name] = password
 
 
logins = users.keys()
 
 
def get_data(passw) -> tuple:
    global users
    logins = users.keys()

    users[login] = passw
  
 
    return (login, passw)
 
 
def add_user(passw):
    data: tuple = get_data()
    with open('file.txt', 'r+') as base:
        base.write(data[0] + " " + data[1] + '\n')
    
 


