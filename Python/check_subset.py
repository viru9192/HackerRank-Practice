T = int(input())

for i in range(T):
    A = int(input())
    A_set = set(map(int, input().split()))
    B = int(input())
    B_set = set(map(int, input().split()))
    
    if A_set.issubset(B_set):
        print('True')
    else:
        print('False')