import sys
sys.stdin = open('Data_Structure/input.txt','r')

dic = {}
cnt = 0
ans = []

while True:
    species = sys.stdin.readline().rstrip()
    if not species:
        break

    cnt += 1

    if species in dic:
        dic[species] +=1
    else:
        dic[species] = 1
        ans.append(species)

ans.sort()

for i in range(len(ans)):
    percent = dic[ans[i]]
    print(f'{ans[i]} {percent/cnt*100:.4f}')