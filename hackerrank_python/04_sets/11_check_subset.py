# Problem: Check Subset
# Link: https://www.hackerrank.com/challenges/py-check-subset/problem

t = int(input())
for _ in range(t):
    _ = int(input())
    a = set(map(int, input().split()))
    _ = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))
