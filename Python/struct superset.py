A = set(map(int, input().split()))
n = int(input())

superset = 'True'

for i in range(n):
    
    N = set(map(int, input().split()))
    if not (N.issuperset(A) and N != A):
        superset = 'False'
        break
        
print(superset)