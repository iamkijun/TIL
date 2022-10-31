import sys
sys.stdin = open('input.txt','r')



N = int(input()) #이닝

score = 0

def dfs():
    global current_score
    global n

    status = [0,0,0] # 1루, 2루, 3루
    outs = 0

    while outs<3:
        if li[n] == 0:
            outs += 1
        elif li[n] == 1:
            if status[2] == 1:
                current_score += 1
                status[2] = 0
            if status[1] == 1:
                status[2] = 1
                status[1] = 0
            if status[0] == 1:
                status[1] = 1
                status[0] = 0
            status[0] = 1

        elif li[n] == 2:
            if status[2] == 1:
                current_score +=1
                status[2] = 0
            if status[1] == 1:
                current_score +=1
                status[1] = 0
            if status[0] == 1:
                status[2] = 1
                status[0] = 0
            status[1] = 1
        elif li[n] == 3:
            current_score += sum(status)
            status = [0,0,1]
        elif li[n] == 4:
            current_score += sum(status) + 1
            status = [0,0,0]

        n += 1
        if n == 9:
            n = 0

    return

total_li =[]

for _ in range(N):
    li = list(map(int, input().split()))
    total_li.append(li)

max_score = 0
for i in range(9):

    current_score = 0
    n = i
    for li in total_li:

        dfs()

    # print(i, current_score)

    if current_score > max_score:
        max_score = current_score

print(max_score)

from itertools import permutations

for a in permutations(range(1,9),8):
    line_up = list(a[:3])+ [0] + list(a[3:])
    print(line_up)