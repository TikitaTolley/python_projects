# encrypting passwords

from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''

'''
this will open/create a file called key.key in wb mode - meaning write in bytes
then giving it name 'key_file'
then you will write in the key that was generated by Fernet

then call the function
then comment it out

key + password + text to encrypt = random text
random text + key + passweord = text to encrypt

if you type in the wrong master_pwd you will get a wrong decrypted text
'''



def load_key():     # function must be defined before I use it
    file = open("key.key", "rb") # reading bytes
    key = file.read() # reading the file
    file.close() # closing the file
    return key




key = load_key()      # bytes is a different way of storing information
fer = Fernet(key)



def view():     # a function is an executable, re-usable piece of code
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()    #strip off the carriage return from our line
            user, passw = data.split("|")   # it will split everything when '|' is found, and put into a list (with 2 elements)(so user is assigned to 1st element, etc)
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")


    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")      #encoding the password will convert it into bytes


'''
'with' automatically closes file
file name
a = mode to open file in

w mode = overwites file that already exists
r mode = can't write anything since it is in read mode
a mode = most flexible mode, add something (append) to the end of an existing file,
         and create a new file if that file doesn't exist

f = name of file
'''


while True:

    mode = input("Would you like to add a new password or view existing ones (view/add)? (press q to quit)").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue