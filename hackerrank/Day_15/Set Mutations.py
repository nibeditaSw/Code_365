# Set Mutations

number_of_elements = int(input())
initial_set = set(map(int, input().split()))
number_of_other_sets = int(input())
for _ in range(number_of_other_sets):
    cmd = input().split()
    opt = cmd[0]
    other_set = set(map(int, input().split()))
    if opt == "difference_update":
        initial_set.difference_update(other_set)
    elif opt == "intersection_update":
        initial_set.intersection_update(other_set)
    elif opt == "symmetric_difference_update":
        initial_set.symmetric_difference_update(other_set)
    elif opt == "update":
        initial_set.update(other_set)
print(sum(initial_set))