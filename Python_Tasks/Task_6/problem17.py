# Problem 17: Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

a = set(map(int, input().split()))
result = True
for _ in range(int(input())):
    other = set(map(int, input().split()))
    if not (a > other):
        result = False
print(result)
