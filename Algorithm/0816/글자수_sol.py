import sys
sys.stdin = open("input.txt","r")

T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()

    cnts = [0] * 128 # ASCII 문자의 개수
    for char in str2:
        cnts[ord(char)] += 1

    maxV = 0 #최댓값 찾기

    for char in str1:
        if maxV < cnts[ord(char)]:
            maxV = cnts[ord(char)]

    print(f'#{t} {maxV}')

