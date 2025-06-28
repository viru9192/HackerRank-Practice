eng = int(input())
n_eng = set(map(int, input().split()))
french = int(input())
n_french = set(map(int, input().split()))

both_paper = n_eng.intersection(n_french)
print(len(both_paper))