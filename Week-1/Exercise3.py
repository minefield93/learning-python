
# Assigning string to var line
line = "Processor board ID FAL127197A"

# Unpacking using .split() to assign divided string values to 4 different variables
var1, var2, var3, var4 = line.split()

print()
print(f"Serial number found in line:\n'{line}'")
print()
print(f"The serial number is: {var4}")
print()

# Assigning split values to a list
words = line.split()
print(f"The serial number using list assignment is: {words[3]}")
print() 
