# Find the Runner-Up Score!

n = int(input("Enter your scores: "))
arr = list(map(int, input().split()))
arr.sort()
print(arr[(arr.index(max(arr)))-1])


#####

n = float(input("Enter your scores: "))
arr = list(map(float, input().split()))
b = sorted(set(arr))
c = b[-2]
print(c)