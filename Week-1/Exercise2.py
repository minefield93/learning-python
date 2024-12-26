
# Asking for dc name
print()
dc_name = input("Enter the data center location: ")

# Printing in upper case using .upper() method
print()
print(f"Upper case:\n{dc_name.upper()}")

# Printing before and after stripping whitespace using repr(var) and .strip() methods
print()
print("Strip off whitespace:")
print(f"Before: {repr(dc_name)}")
print(f"After: '{dc_name.strip()}'")

# Assigning modified var value after method chaining and printing its absolute value using repr(var)
print()
new_dc_name = dc_name.strip().upper()
print("Method chaining:")
print(repr(new_dc_name))



