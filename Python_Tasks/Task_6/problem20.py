# Problem 20: Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

for _ in range(int(input())):
    number = input().strip()
    if re.fullmatch(r'[789]\d{9}', number):
        print('YES')
    else:
        print('NO')
