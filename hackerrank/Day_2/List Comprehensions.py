# List Comprehensions

x = int(input("Enter a Number for x: "))
y = int(input("Enter a Number for y: "))
z = int(input("Enter a Number for z: "))
n = int(input("Enter a Number for n: "))

result=[]
for i in range(x+1):   # The expression (x+1) is used to include all the value from 0 to x in range.
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                result.append([i,j,k])
print(result)

# List Comprehension method
result=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(result)
