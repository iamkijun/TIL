box = [1,5,7,6]

def solution(box):
    #박스의 길이 선언
    n = len(box)

    while True:
        #박스에 든 빵의 최대값, 해당 값의 인덱스 찾아서 변수로 선언
        max_val = max(box)
        max_idx = box.index(max_val)
        
        #최적의 값 찾기 (가장 많은 상자에 든 최소한의 빵 개수 만드는 수)
        ideal_val = sum(box[:max_idx+1])//(max_idx+1)

        #박스에 든 빵의 최소값, 해당 값의 인덱스 찾아서 변수로 선언
        min_val = min(box[:max_idx+1])
        min_idx = box.index(min_val)

        #예외처리 (더이상 반복할 필요가 없으면 종료)
        if min_idx >= max_idx:
            break 
        
        #최대값에서 빼면 좋을 최적의 값 빼서 변수로 선언
        temp = (max_val - ideal_val)

        #왼쪽에 있는 박스에다가 옮겨주기
        box[max_idx] -= temp
        box[max_idx-1] += temp
    
    return max(box)
    

print(solution(box))