# Problem: Set .intersection() Operation
# Link: https://www.hackerrank.com/challenges/py-set-intersection/problem

n = int(input())
set_a = set(map(int, input().split()))
b = int(input())
set_b = set(map(int, input().split()))

print(len(set_a.intersection(set_b)))
