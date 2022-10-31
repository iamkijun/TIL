import sys
sys.stdin = open('input.txt','r')

P = int(input())
for _ in range(P):

    students = list(map(int, input().split()))

    tc = students.pop(0)

    count = 0           #학생들이 뒤로 물러난 횟수

    for i in range(19,0,-1):
        for j in range(i):
            if students[j] > students[j+1]:
                students[j], students[j+1] = students[j+1] , students[j]
                count+=1

    print(f'{tc} {count}')