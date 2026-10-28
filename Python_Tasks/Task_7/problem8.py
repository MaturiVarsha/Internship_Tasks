# Problem 8: Gemstones
# https://www.hackerrank.com/challenges/gem-stones/problem

n=int(input())
common=set(input().strip())
for _ in range(n-1):
    common.intersection_update(input().strip())
print(len(common))
