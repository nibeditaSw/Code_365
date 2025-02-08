# What's Your Name?


def print_full_name(first, last):
    print("Hello "+first+" "+last+"!"+" You just delved into python.")
    

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print_full_name(first_name, last_name)


# string format method

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Hello {} {}! You just delved into python.".format(first_name, last_name))