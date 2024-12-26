# Assigning variables
sf_gw1 = "172.31.255.1/24"
sf_gw2 = input("Please input 'sf_gw2' IP address: ")

# Creating new variables to use for creating columns
header1 = "sf_gw1"
header2 = "sf_gw2"
header_line = "-" * 20

# Printing using f-string centering method
print()
print(f"{header1:^20} {header2:^20}")
print(f"{header_line:^20} {header_line:^20}")
print(f"{sf_gw1:^20} {sf_gw2:^20}")
print()
