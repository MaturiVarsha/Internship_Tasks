# Problem 3: Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem

s=input().strip()
expected='SOS'*(len(s)//3)
print(sum(x != y for x,y in zip(s,expected)))
