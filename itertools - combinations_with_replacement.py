from itertools import combinations_with_replacement
s,n = input().split()
n = int(n)
s = sorted(s)
for i in combinations_with_replacement(s,n):
    print(''.join(i))