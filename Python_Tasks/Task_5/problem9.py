# Problem 9: Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
words = {}
order = []
for i in range(n):
    word = input()
    if word not in words:
        words[word] = 1
        order.append(word)
    else:
        words[word] += 1
print(len(order))
for word in order:
    print(words[word], end=" ")
