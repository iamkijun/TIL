# Algorithm
---
## 0812
---
### 문자열(String)

정보의 교환을 위해서 미국에서 ASCII코드를 만들었다.

문자 뒤집기 ([::-1]안쓰고 for문으로)
``` python
st = 'hello'
ts = ''
for ch in st:
    ts = ch +ts
print(ts)
```

문자열 -> 정수로 변환 (ASCII)
```python
str1 = '1234'
sm = 0
for ch in str1:
  sm = sm* 10 + ord(ch)-ord('0')
print(sm)
```

정수 -> 문자열로 변환 (ASCII)
```python
i = 123
st = ''
while i>0:
    st = chr(i%10 + ord('0')) +st
    i//=10
print(st)
```