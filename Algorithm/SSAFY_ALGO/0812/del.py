i = 123
st = ''
while i>0:
    st = chr(i%10 + ord('0')) +st
    i//=10
print(st)