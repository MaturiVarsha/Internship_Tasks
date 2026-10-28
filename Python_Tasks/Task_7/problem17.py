# Problem 17: Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separate(s):
    for length in range(1,len(s)//2+1):
        first=int(s[:length]); cur=first; built=''
        while len(built)<len(s):
            built+=str(cur); cur+=1
        if built==s: return f'YES {first}'
    return 'NO'
for _ in range(int(input())):
    print(separate(input().strip()))
