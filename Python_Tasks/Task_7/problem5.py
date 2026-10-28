# Problem 5: Alternating Characters
# https://www.hackerrank.com/challenges/alternating-characters/problem

for _ in range(int(input())):
    s=input().strip()
    print(sum(s[i]==s[i-1] for i in range(1,len(s))))
