# Algorithm

---

## Day17, 8월 8일 월요일

---

## 2차원 배열

- 1차원 list를 묶어노은 list
- 2차원 이상의 다차원 list는 차원에 따라 index를 선언

````python
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
```
3
1 2 3
4 5 6
7 8 9
```

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
```
3
123
456
789
```
````

배열 순회

- n X m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법

- 델타를 이용한 2차 배열 탐색

  ```
  di[] <- [0,0,-1,1]
  dj[] <- [-1,1,0,0]
  for i : 1 -> N-1
  	for j ; 1 -> N-1 :
  		for k in range(4):
  			ni <- i +di[k]
  			nj <- j +dj[k]
  			if 0<=ni<N and 0<=nj<N
  				test(arr[ni][nj])
  ```

  

전치행렬

```python
for i in range(3):
	for j in range(3):
		if i <j:
			arr[i][j], arr[j][i] = arr[j][i], arr[i],[j]
```



선택정렬

```python
arr = [7,2,5,3,4,6]

N = len(arr)

for i in range(N-1):
    minIdx = i # 구간 맨 앞을 최소값으로 가정
    for j in range(i+1,N): # 실제 최소값 인덱스 찾기
        if arr[minIdx] > arr[j]:
            minIdx = j

    arr[minIdx], arr[i] = arr[i], arr[minIdx]

print(arr)


```

