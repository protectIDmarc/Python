name = "\tLuis \nMarques"
print("_______UnFormatted________")
print(name)

print("_______Left Stripped________")
print(name.lstrip())

print("_______Right Stripped________")
print(name.rstrip())

print("_______Both Stripped________")
name = name.strip("\t")
print(name)

print("_______Strip New-Line________")
name = name.replace("\n", "")
print(name)
