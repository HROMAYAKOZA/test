with open('text.txt', 'r') as f:
    print(f.read())

with open('secretcode.txt', 'r') as f:
    print("Your code is: %s" % f.read())