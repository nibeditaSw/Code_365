# Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
number_of_commands = int(input())

for _ in range(number_of_commands):
    cmd = list(input().split())
    if len(cmd) == 1:
        s.pop()
    else:
        value = int(cmd[1])
        operation = cmd[0]
        if operation == "discard":
            s.discard(value)
        else:
            s.remove(value)
print(sum(s))