list01 = [3, 7, 5.2, 12.99, 12, 13, 43, 8]
print(len(list01))
mid = len(list01) // 2
listleft = (list01[:mid])
listright = (list01[mid:])
answer = max(listleft) + max(listright)
print(answer)
