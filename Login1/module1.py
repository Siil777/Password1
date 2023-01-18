with open('file.txt') as base:
    data=base.readlines()


users={}
for user in data:
    name=user.split()[0]
    password=user.split()[1]
    user[name]=password


logins=users.keys()

def get_data() -> tuple:
    global users
    logins=users.keys()
    while True:
        login=input('login:')
        passw=input('pass:')
        if login not in logins:
            print('Success')
            users[login]=passw
            break
        else:
            print('There is a user with this username')


    return (login,passw)

def add_user():
    data: tuple= get_data()
    with open('file.txt','r+') as base:
        base.write(data[0]+ "" +data[1]+'\n')

def main():
    while True:
        print('Write 1 for reg 0 for exit')
        cmd=input()
        if cmd=='1':
            add_user()
        elif cmd=='0': break 
        else:
            print('incorrect command')
if name ==" main ":
    main()
