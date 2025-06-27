from collections import namedtuple

n = int(input())
header = input().split()
stud = namedtuple('stud', header)
total = 0
for i in range(n):
    data = input().split()
    s =stud(*data)
    total += int(s.MARKS)

average_marks = total/n
print(f"{average_marks: .2f}")