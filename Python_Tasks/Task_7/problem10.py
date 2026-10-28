# Problem 10: CamelCase
# https://www.hackerrank.com/challenges/camelcase/problem

s=input().strip()
print(1+sum(ch.isupper() for ch in s) if s else 0)
