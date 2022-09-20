#코드업 기초 100제
---
## #21
``` python
s = input()
for i in range(len(s)):
    print(s[i])
```

## #22
``` python
s = input()
print(s[0:2])
```

## #23
``` python
s = input()
print(s[0:2],s[2:4],s[4:6])
```

## #24
``` python
w1, w2 = input().split()
s = w1 + w2
print(s)
```

## #25
``` python
a, b = input().split()
c = int(a) + int(b)
print(c)
```

## #26
``` python
a = float(input())
b = float(input())

print(a+b)
```

## #27
``` python
a = input()
n = int(a)
print(f'{n:0x}')
```

## #28 **이문제 좀 이상하다** !!! (제대로 출력이 안됨)
``` python
n = int(input())
print(f'{n:X}')
```

## #29
``` python
a = input()
n = int(a, 16)
print(f'{n:o}')
```

## #30
``` python
n = ord(input())
print(n)
```

## #31
``` python
c = int(input())
print(chr(c))
```

## #32
``` python
n = int(input())
print(-n) 
```

## #33
``` python
n = input()
print(chr(n+1))
```

## #34
``` python
a = int(input())
b = int(input())
c = a - b
print(c)
```

## #35
``` python
f1 = float(input())
f2 = float(input())
m = f1 * f2
print(m)
```

## #36
``` python
w, n = input().split()
print(w*int(n))
```

## #37
``` python
n = int(input())
s = input()
print(n*s)
```

## #38
``` python
a = int(input())
b = int(input())
c = a**b
print(c)
```

## #39
``` python
f1 = float(input())
f2 = float(input())
m = f1 ** f2
print(m)
```

## #40 ~7/19
``` python
a = int(input())
b = int(input())
print(a//b)
```