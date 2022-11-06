x = 4
y = 6
z = 2

def solution(x, y, z):
    
    # x: 시작 위치, y: 목표 위치, z: 최대 이동 수

    # 시작위치와 목적지의 거리
    distance = abs(y - x) 

    # Case 1: 불가능할 경우(두 위치의 거리가 최대 이동수보다 클 경우)
    if distance > z:
        return -1
    
    # Case 2: 두 위치의 거리가 최대 이동수와 같을 경우
    elif distance == z:
        return max(y,x)

    # Case 3: 두 위치의 거리가 최대 이동수보다 작을 경우 (목적지에 도착 후에/도착 전에 추가적으로 움직일 수 있을 경우)
    else:
        return max(x,y)+ (z-distance)//2


print(solution(x,y,z))