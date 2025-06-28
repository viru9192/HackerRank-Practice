eng = int(input())
eng_roll = set(map(int, input().split()))
fren = int(input())
fren_roll = set(map(int, input().split()))

total_eng = eng_roll.difference(fren_roll)
print(len(total_eng))