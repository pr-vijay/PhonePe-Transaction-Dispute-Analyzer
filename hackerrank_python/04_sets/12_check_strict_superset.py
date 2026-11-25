# Problem: Check Strict Superset
# Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

a = set(map(int, input().split()))
n = int(input())
is_strict = True

for _ in range(n):
    other = set(map(int, input().split()))
    if not (a.issuperset(other) and len(a) > len(other)):
        is_strict = False
        break

print(is_strict)
