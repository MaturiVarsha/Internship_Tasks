# Problem 16: Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

n=int(input()); s=input().strip(); k=int(input())%26
out=[]
for ch in s:
    if 'a'<=ch<='z': out.append(chr((ord(ch)-97+k)%26+97))
    elif 'A'<=ch<='Z': out.append(chr((ord(ch)-65+k)%26+65))
    else: out.append(ch)
print(''.join(out))
