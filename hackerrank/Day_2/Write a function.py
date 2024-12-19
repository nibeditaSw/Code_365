# leap_year


def is_leap(year):
    leap = False
    
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    
    return leap

year = int(input("Enter a year: "))
print(is_leap(year))


# using helper function

def is_divisible(num, divisor):
    return num % divisor == 0

def is_leap(year):
    return is_divisible(year, 4) and (not is_divisible(year, 100) or is_divisible(year, 400))

year = int(input("Enter a year: "))
print(is_leap(year))

