from collections import defaultdict

n, m = map(int, input().split())
a = defaultdict(list)

for i in range(1, n + 1):
    a[input()].append(i)
s = ""
for i in range(1, m + 1):
    key = input()
    if len(a[key]) > 0:
        print (s.join(map(str, a[key])))
    else:
        print (-1)