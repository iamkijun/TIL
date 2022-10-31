import sys
sys.stdin = open('Brute_Force/input.txt','r')

N = int(input())

student_list = []

for _ in range(N):
    W, H = map(int, input().split())
    student_list.append([W,H])

rank_list = []

for i in range(N):
    rank = 1
    
    for j in range(N):
        if student_list[i][0] <student_list[j][0] and student_list[i][1] <student_list[j][1]:
            rank += 1
        
    rank_list.append(rank)

print(*rank_list)