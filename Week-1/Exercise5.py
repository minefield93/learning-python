
# Assigning variables
ip_addr = "10.12.17.1"
mac_addr = "0024.c3e8.13ac"

# Printing using string concatenation
new_string = ip_addr + " --> " + mac_addr
print()
print("String concatenation:")
print(new_string)

# Printing using f-strings
print()
print(f"f-strings:\n{ip_addr} --> {mac_addr}")
print()

# Printing using .format() method
print("format() method:\n{} {} {}".format(ip_addr, "-->", mac_addr))
print()

