def solution(N, stages):
    stages = sorted(stages)
    
    ans = []

    for i in range(1,N+1):
        if i in stages:
            a = stages.count(i)
            ans.append([i,a/len(stages)])
            stages = stages[a:]
        elif i not in stages:
            ans.append([i,0])

    ans.sort(key=lambda x:x[1],reverse=True)

    new = []
    for val in ans:
        new.append(val[0])
        
    return new