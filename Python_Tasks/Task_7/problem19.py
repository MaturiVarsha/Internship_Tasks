# Problem 19: Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s=input().strip(); weights=set(); prev=''; run=0
for ch in s:
    if ch==prev: run+=1
    else: prev=ch; run=1
    weights.add((ord(ch)-ord('a')+1)*run)
for _ in range(int(input())):
    print('Yes' if int(input()) in weights else 'No')
