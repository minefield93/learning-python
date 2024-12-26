print()
dc_name = input("Enter the data center location: ")

print()
print(f"Upper case:\n{dc_name.upper()}")

print()
print("Strip off whitespace:")
print(f"Before: {repr(dc_name)}")
print(f"After: '{dc_name.strip()}'")

print()
new_dc_name = dc_name.strip().upper()
print("Method chaining:")
print(repr(new_dc_name))



