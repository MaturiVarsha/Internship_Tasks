# Problem 16: Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem

for _ in range(int(input())):
    a_count = int(input())
    a = set(map(int, input().split()))
    b_count = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))
