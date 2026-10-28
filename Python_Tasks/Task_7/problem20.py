# Problem 20: Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem

s=input().strip(); stack=[]
for ch in s:
    if stack and stack[-1]==ch: stack.pop()
    else: stack.append(ch)
print(''.join(stack) if stack else 'Empty String')
