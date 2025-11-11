a, b = input().split()
len1 = len(a)
len2 = len(b)

if len1 > len2:
    print(a, len1)
if len2 > len1:
    print(b, len2)
if len1 == len2:
    print('same')        
