# Problem 13: Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter
freq=Counter(Counter(input().strip()).values())
if len(freq)==1:
    print('YES')
elif len(freq)==2:
    (f1,c1),(f2,c2)=freq.items()
    ok=(f1==1 and c1==1) or (f2==1 and c2==1) or (abs(f1-f2)==1 and ((f1>f2 and c1==1) or (f2>f1 and c2==1)))
    print('YES' if ok else 'NO')
else:
    print('NO')
