# Finding the percentage

n = int(input("number of students' records: "))

student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input("name of a student to query: ")

marks = student_marks[query_name]
# format(value, '.nf')
print(format(sum(marks)/3, '.2f'))