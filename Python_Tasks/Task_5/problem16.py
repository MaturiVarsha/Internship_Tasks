# Problem 16: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    x = int(input())
    shoe_counts = Counter(map(int, input().split()))
    customers = int(input())
    earnings = 0
    for _ in range(customers):
        size, price = map(int, input().split())
        if shoe_counts[size] > 0:
            earnings += price
            shoe_counts[size] -= 1
    print(earnings)
