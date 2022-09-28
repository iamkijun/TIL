import sys
sys.stdin = open('Binary_Search/input.txt','r')


N, M = map(int, input().split())


arr = []
for _ in range(N):
    li = list(map(int, input().split()))
    linked_lamp_number = li[0]
    linked_lamp_list = li[1:]
    arr.append(linked_lamp_list)


for i in range(N):
    new_arr = arr[:i] + arr[i+1:]
    
    lamp_list = []
    for val in new_arr:
        for i in val:
            if i not in lamp_list:
                lamp_list.append(i)
    lamp_list.sort()
    if lamp_list == [x for x in range(1,M+1)]:
        print(1)
        break
else:
    print(0)
