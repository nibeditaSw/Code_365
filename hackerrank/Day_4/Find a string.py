# Find a string

def count_substring(string, sub_string):
    c = 0
    l = len(sub_string)
    for i in range(len(string)):
        s = string[i:i+l]
        if s == sub_string:
            c+=1
    return c


string = input("Enter a string: ").strip()
sub_string = input("Enter a substring: ").strip()

count = count_substring(string, sub_string)
print(count)


# By using find method
# find() returns the index of the first occurrence of the substring, or -1 if it is not found.

