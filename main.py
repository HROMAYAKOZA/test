f = open('text.txt', 'r')
print(*f)
f.close()

f = open('secretcode.txt', 'r')
print("Your code is: %s" % f.read())
f.close