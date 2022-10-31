import sys
sys.stdin = open("input.txt","r")

T = int(input())

for t in range(1, T+1):
    counts = [0] * 26  #알파벳 자리별 갯수 세는 리스트

    str1 = list(input()) #리스트로 받음
    str2 = list(input())

    maxV = 0 #최댓값 찾기

    for i in range(len(str1)):
        if str2.count(str1[i]) > maxV:
            maxV = str2.count(str1[i])

    print(f'#{t} {maxV}')

