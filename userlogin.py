import os
print("- Imported")
os.system("clear")
print("WorldOS Login")
data1 = open("name", "r")
data2 = open("code", "r")
usrdata = data1.read()
passdata = data2.read()
print("Username: "+passdata)
ok = 0
while True:
  password = input("Password: ")
  if password==passdata:
    os.system("bash ./WORLDOS/os")

