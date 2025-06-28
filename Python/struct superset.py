A = set(map(int, input().split()))
n = int(input())

superset = 'True'

for i in range(n):
    
    N = set(map(int, input().split()))
    if not (A.issuperset(N) and A != N):
        superset = 'False'
        break
        
print(superset)