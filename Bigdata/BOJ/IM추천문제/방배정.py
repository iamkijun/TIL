import sys
sys.stdin = open('input.txt','r')

N, K = map(int, input().split())

female_grade = []   #남학생들 학년 저장하는 리스트
male_grade = []     #여학생들 학년 저장하는 리스트

for n in range(N):
    S, Y = map(int,input().split())

    if S == 0:          #여학생일 경우
        female_grade.append(Y)
    elif S == 1:        #남학생일 경우
        male_grade.append(Y)

#학년별 인원 수 1~6
female_count = [0] * 6
male_count = [0] * 6 

for val in female_grade:
    female_count[val-1] += 1

for val in male_grade:
    male_count[val-1] += 1

#필요한 방의 개수
count = 0
for i in range(6):
    if female_count[i] > 0:
        count += (female_count[i]+(K-1)) // K
    
    if male_count[i] > 0:
        count += (male_count[i]+(K-1)) // K

print(count)
