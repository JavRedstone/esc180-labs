msg = "Enter a name: "
name = input(msg)
names = ""
while name != "END":
    names += name + ', '
    name = input(msg)
print(names[:-2])