# Problem 14: Anagram
# https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter
for _ in range(int(input())):
    s=input().strip()
    if len(s)%2:
        print(-1)
    else:
        h=len(s)//2
        print(sum((Counter(s[:h])-Counter(s[h:])).values()))
