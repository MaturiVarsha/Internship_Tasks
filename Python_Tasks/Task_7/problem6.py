# Problem 6: Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem

s=input().lower()
print('pangram' if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s)) else 'not pangram')
