# String Split and Join

line = input("Enter a string: ")

def split_and_join(line):
    result = "-".join(line.split())
    return result


result = split_and_join(line)
print(result)