n = int(input())
s = set(map(int, input().split()))
A = int(input())

for i in range(A):
    cmd = input().split()
    
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1]))

total = 0
for i in s:
    total += i
print(total)