a, b, c = map(int, input().split())
max = 0
min = 0
T = a + b + c
if a > b:
    if a > c:
        max = a
if b > a:
    if b > c:
        max = b
if c > a:
    if c > b:
        max = c
if a < b:
    if a < c:
        min = a
if b < a:
    if b < c:
        min = b
if c < a:
    if c < b:
        min = c
print(T - max - min)                    