a, b = input().split()

len1 = len(str1)
len2 = len(str2)
iif len1 > len2:
	print(str1, len1)
elif len1 < len2:
	print(str2, len2)
else:
	print("same")