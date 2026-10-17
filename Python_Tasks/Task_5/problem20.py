# Problem 20: Piling Up!
# HackerRank: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        blocks = deque(map(int, input().split()))
        largest = float('inf')
        possible = True
        while blocks:
            if blocks[0] >= blocks[-1]:
                current = blocks.popleft()
            else:
                current = blocks.pop()
            if current > largest:
                possible = False
                break
            largest = current
        print("Yes" if possible else "No")
