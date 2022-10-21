import sys
sys.stdin = open('Sort/input.txt','r')
import copy

N = int(input())

num_list= list(map(int, input().split()))

new = copy.deepcopy(num_list)
new.sort()

ans =[]

for i in range(N):

    if new.index(num_list[i]) in ans:
        k = 1
        while True:
            if new.index(num_list[i])+k in ans:
                k += 1
            else:
                ans.append(new.index(num_list[i])+k)
                break
    else:
        ans.append(new.index(num_list[i]))

print(*ans)