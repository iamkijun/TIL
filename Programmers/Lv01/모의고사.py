def solution(answers):
    
    one = [1,2,3,4,5]*2000
    two = [2,1,2,3,2,4,2,5]*1250
    three = [3,3,1,1,2,2,4,4,5,5]*1000
    
    one_count = 0
    two_count = 0
    three_count = 0
    
    for i in range(len(answers)):
        if answers[i] == one[i]:
            one_count +=1
        if answers[i] == two[i]:
            two_count +=1
        if answers[i] == three[i]:
            three_count +=1
    
    cnts = [one_count,two_count,three_count]
    
    ans = []
    for i in range(3):
        if cnts[i] == max(cnts):
            ans.append(i+1)
            
    return ans