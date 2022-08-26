import sys
sys.stdin = open('input.txt','r')

#V: 열의 개수 , R: 행의 개수
C, R = map(int, input().split())

R_list = [0] #시작점을 포함한 가로로 자르는 위치리스트 생성
C_list=  [0] #시작점을 포함한 세로로 자르는 위치리스트 생성

N = int(input())

#자르는 위치 더해주기
for _ in range(N):
    d, num = map(int,input().split())
    if d == 0:
        R_list.append(num)

    elif d == 1:
        C_list.append(num)

#정렬한 뒤 끝점 더해주기
R_list.sort()
R_list += [R]

#자르고 자르고 남은 세로의 변의 길이 저장하는 리스트 생성
R_len = []
for i in range(len(R_list)-1):  #아까 마지막꺼 + R해줘서 -1해주는거임
    R_len.append(R_list[i+1]-R_list[i])

#정렬한 뒤 마지막 위치 더해주기
C_list.sort()
C_list += [C]

#자르고 자르고 남은 가로의 변의 길이 저장하는 리스트 생성
C_len = []
for i in range(len(C_list)-1): #아까 마지막꺼 + C해줘서 -1해주는거임
    C_len.append(C_list[i+1]-C_list[i])

#최대 넓이 구하기
max_area = 0
for i in range(len(R_len)):
    for j in range(len(C_len)):
        area = R_len[i] * C_len[j]
        if area> max_area:
            max_area = area

print(max_area)



