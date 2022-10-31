
a = input()
b = input()

h1 = int(a[:2])
m1 = int(a[3:5])
d1 = int(a[6:])

h2 = int(b[:2])
m2 = int(b[3:5])
d2 = int(b[6:])
if h1 == h2 and m1 == m2 and d1 == d2:
    print('24:00:00')
else:
    h = h2 - h1
    m = m2 - m1
    d = d2 - d1

    if d < 0:
        d = d + 60
        m = m - 1
    if m < 0:
        m = m + 60
        h = h - 1
    if h < 0:
        h = h + 24

    if d < 10:
        d = '0' +str(d)
    if m < 10:
        m = '0' +str(m)
    if h < 10:
        h = '0' +str(h)

    print(f'{h}:{m}:{d}')
