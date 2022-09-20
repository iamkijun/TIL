import sys
sys.stdin = open("Greedy/input.txt","r")

A, B = map(int, input().split())

cnt = 1

num_li = [A]
while True:
    new_num_li = []
    for val in num_li:
        if val*2 <= B:
            new_num_li.append(val*2)
        if val*10+1:
            new_num_li.append(val*10+1)
    
    num_li = new_num_li
    cnt += 1

    if B in num_li:
        break
    elif min(num_li) > B:
        cnt = -1
        break

print(cnt)

