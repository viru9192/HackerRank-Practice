M = int(input())
M_list = list(map(int, input().split()))
N = int(input())
N_list = list(map(int, input().split()))
set_M = set(M_list)
set_N = set(N_list)
final_lst = sorted(set_M.symmetric_difference(set_N))
for i in final_lst:
    print(i)