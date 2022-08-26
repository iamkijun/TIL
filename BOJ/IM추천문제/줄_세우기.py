import sys
sys.stdin = open('input.txt','r')

N = int(input())

li = list(map(int, input().split()))

order_list = [0] * N       #순서를 담을 리스트

for i in range(1,N+1):
    if order_list[li[i-1]] == 0:        #대기자가 없는 경우
        order_list[li[i-1]] = i         #그냥 거기 서기
    else:
        for j in range(N-2,li[i-1]-1,-1):       #대기자가 있는 경우
            order_list[j+1] = order_list[j]     #전부 뒤로 미뤄버리기
        order_list[li[i-1]] = i                 #그자리 비집고 들어가기

print(*order_list[::-1]) #맨 뒷사람부터 출력
