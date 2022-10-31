import secrets
import sys
sys.stdin = open('String/input.txt','r')

normal = input()
secret = input()

for i in range(len(normal)):
    if normal[i].isalpha() and secret[i%len(secret)].isalpha():
        print(chr((ord(normal[i])-ord(secret[i%len(secret)])+25)%26+97), end="")
    else:
        print(' ',end="")
        
print()