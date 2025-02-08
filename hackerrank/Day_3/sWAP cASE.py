# sWAP cASE

s = input("Enter a string: ")

def swap_case(s):
    x = ""
    for c in s: # NehU
        if c.isupper():
            c = c.lower()
        else:
            c = c.upper()
        x+=c
    return x

result = swap_case(s)
print(result)

# By using sWAP cASE method

s = input("Enter a string: ")

def swap_case(s):
    return s.swapcase()

result = swap_case(s)
print(result)