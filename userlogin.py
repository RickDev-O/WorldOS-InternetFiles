import os
print("- Imported")
os.system("clear")
print("WorldOS Login")
data1 = open("name", "r")
data2 = open("code", "r")
usrdata = data1.read()
passdata = data2.read()
print("Username: "+passdata)
while ok==1:
  password = input("Password: ")
  if password==passdata:
    ok = 1
os.system("bash ./WORLDOS/os")
