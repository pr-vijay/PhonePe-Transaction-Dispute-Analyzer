# Problem: Set Mutations
# Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

len_a = int(input())
a = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    operation, _ = input().split()
    other_set = set(map(int, input().split()))
    getattr(a, operation)(other_set)

print(sum(a))
