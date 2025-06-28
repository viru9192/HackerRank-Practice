K = int(input())
K_lst = list(map(int, input().split()))
K_uni = set(K_lst)

s1 = sum(K_uni)
s2 =sum(K_lst)

captain = (K * s1 - s2) // (K - 1)
print(captain)