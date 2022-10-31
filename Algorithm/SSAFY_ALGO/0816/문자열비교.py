import sys
sys.stdin = open("input.txt","r")

T = int(input())
for t in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    count = 0

    for i in range(len(str2)-len(str1)+1):
        if str1 == str2[i:i+len(str1)]:
            count += 1

    if count > 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')


