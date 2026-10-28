# Problem 15: Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter
s=input().strip()
print('YES' if sum(v%2 for v in Counter(s).values())<=1 else 'NO')
