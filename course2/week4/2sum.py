from bisect import bisect_left, bisect_right

l = []

for i in open('input.txt', 'r'):
    i = int(i.strip())
    l.append(i)

# l = [1, 4, 45, 6, 10, 10, 8]
l.sort()
c = 0
s = set()
for i in set(l):
    left = bisect_left(l, -10000 - i)
    right = bisect_right(l, 10000 - i)
    for j in l[left:right]:
        if i != j:
            s.add(i + j)

print(len(s))
