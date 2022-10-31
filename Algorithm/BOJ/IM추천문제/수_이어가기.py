import sys
sys.stdin = open('input.txt','r')

N = int(input())

max_num_list =[]
max_num = 0

for n in range(N,0,-1):
    num_list = [N]
    num_list.append(n)
    while num_list[-2] - num_list[-1] >= 0:
        num_list.append(num_list[-2] - num_list[-1])

    if len(num_list) > max_num:
        max_num = len(num_list)
        max_num_list = num_list

print(max_num)
print(*max_num_list)