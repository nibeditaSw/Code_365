# Nested Lists

n = int(input("Enter the number of students: "))
result = []
grade = []
for i in range(n):
    name = input("Enter your name: ")
    score = float(input("Enter your score: "))
    result.append([name, score])
    grade.append(score)
print(result)
print(grade)

grade = sorted(set(grade))  # sorted unique
print(grade)
m = grade[1]  # 2nd lowest score
print(m)
name = []
for value in result:
    if m == value[1]:
        name.append(value[0])
print(name)  # unsorted
name.sort()
print(name)  # sorted
for nm in name:
    print(nm)
