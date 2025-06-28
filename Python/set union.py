english = int(input())
n_en = set(map(int, input().split()))
french = int(input())
n_fr = set(map(int, input().split()))

unique_students = n_en.union(n_fr)
print(len(unique_students))