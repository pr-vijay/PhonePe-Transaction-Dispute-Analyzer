# Problem: Designer Door Mat
# Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = map(int, input().split())

# Top half
for i in range(1, n, 2):
    print(('.|.' * i).center(m, '-'))

# Center
print('WELCOME'.center(m, '-'))

# Bottom half
for i in range(n - 2, 0, -2):
    print(('.|.' * i).center(m, '-'))
