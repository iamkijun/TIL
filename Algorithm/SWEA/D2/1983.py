T = int(input())

for i in range(1,T+1):

    N, K = map(int, input().split())

    grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    new_grade = []
    value_list = []

    for k in range(10):
        for n in range(N//10):
            new_grade.append(grade[k])
    
    for j in range(N):
        a,b,c = map(int, input().split())
        sum = a * 0.35 + b * 0.45 + c * 0.2
        value_list.append(sum)

    remember = value_list[K-1]

    value_list.sort(reverse = True)

    idx = value_list.index(remember)
 
    my_grade = new_grade[idx]
    
    print(f'#{i} {my_grade}')