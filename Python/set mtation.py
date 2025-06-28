A = int(input())
A_lst = set(map(int, input().split()))
N = int(input())

for i in range(N):
    cmd = input().split()
    values = set(map(int, input().split()))
    
    if cmd[0] == 'intersection_update':
        A_lst.intersection_update(values)
    elif cmd[0] == 'update':
        A_lst.update(values)
    elif cmd[0] == 'symmetric_difference_update':
        A_lst.symmetric_difference_update(values)
    elif cmd[0] == 'difference_update':
        A_lst.difference_update(values)

print(sum(A_lst))