# Lists
# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

list = []

N = int(input("Enter the lines of commands: "))  #12

for i in range(N):
    cmd = input("Enter the operation: ").split() # 'insert 10 5'  ['insert','10','5']
    if cmd[0] == 'insert':
        list.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'print':  # 'print'
        print(list)
    elif  cmd[0] == 'remove':  #  'remove 6'  ['remove','6']
        list.remove(int(cmd[1]))
    elif cmd[0] == 'append':  # 'append 9' ['append','9']
        list.append(int(cmd[1]))
    elif cmd[0] == 'sort':  # 'sort'
        list.sort()
    elif cmd[0] == 'pop':  #'pop'
        list.pop()
    else:
        list.reverse()