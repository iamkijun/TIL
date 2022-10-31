N = 1
stages = [4, 4, 4, 4]

def solution(N, stages):
    answer = []

    stages.sort()

    for i in range(1,N+1):
        idx = 0
        for j in range(len(stages)):

            if stages[j] >= i:
                idx = j
                break
        print(i,j)
        try:
            ans = stages.count(i)/(len(stages[j:]))
        except:
            ans =0
        answer.append([ans,i])
                
    answer.sort(key = lambda x:-x[0])
    
    ans = []

    for val in answer:
        ans.append(val[1])

    return ans

print(solution(N,stages))