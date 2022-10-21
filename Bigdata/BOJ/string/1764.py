N, M = map(int, input().split())

N_list = [' '] * N
M_list = [' '] * M

for n in range(N):
    N_name = input()
    N_list[n] = N_name

for m in range(M):
    M_name = input()
    M_list.append(M_name)


NM_list = set(N_list) & set(M_list)
NM_list = list(NM_list)
NM_list.sort()

print(len(NM_list))
for val in NM_list:
    print(val)