#!/usr/bin/python3
for n in range(0, 10):
    for j in range(0, 10):
        if n == 8 and j == 9:
            continue
        if n < j:
            print('{}{}'.format(n, j), end=", ")
print('{}{}'.format(n - 1, j))
