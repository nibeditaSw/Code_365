# Input()

x, k = map(int, input().strip().split())
equation = input().strip()
print(eval(equation) == k)