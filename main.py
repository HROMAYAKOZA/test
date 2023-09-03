import json
f = open('text.txt', 'r')
print(*f)
f.close()

f = open('secretcode.txt', 'r')
s = f.read()
user = input("Your username: ")
with open('database.json', 'r') as file:
    data = json.load(file)
    password = data.get(user, None)
if password == s:
    print("Success")
else:
    print("You don't have access")
print("Your code is: %s" % password)
f.close