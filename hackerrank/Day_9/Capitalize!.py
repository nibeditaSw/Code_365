# Capitalize!

s = input("Enter a string: ")
s_ar = s.split(" ")
final_ar = []
space = " "
for p in s_ar:
    final_ar.append(p.capitalize())
print(space.join(final_ar))