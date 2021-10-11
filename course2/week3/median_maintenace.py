import heapq
heapq.heappush()

min_h = []
max_h = []
total_m = 0
sorted_total = 0
s = []

c = 0
for line in open('input.txt', 'r'):
    c  += 1
    x = int(line.strip())
    s.append(x)
    s.sort()
    if len(s) % 2 == 0:
        sorted_total += s[len(s) // 2-1]
    else:
        sorted_total += s[len(s) // 2]
    if len(min_h) == len(max_h):
        if max_h and x <= -max_h[0]:
            heapq.heappush(min_h, -heapq.heappop(max_h))
            heapq.heappush(max_h, -x)
            total_m += min_h[0]
        else:
            heapq.heappush(min_h, x)
            total_m += min_h[0]
        # print(max_h, min_h)
        continue
    elif len(max_h) > len(min_h):
        if x <= -max_h[0]:
            heapq.heappush(min_h, -heapq.heappop(max_h))
            heapq.heappush(max_h, -x)
        else:
            heapq.heappush(min_h, x)
    else:
        if min_h and x >= min_h[0]:
            heapq.heappush(max_h, -heapq.heappop(min_h))
            heapq.heappush(min_h, x)
        else:
            heapq.heappush(max_h, -x)
    total_m += -max_h[0]
    # print(max_h, min_h)
    if total_m != sorted_total:
        print('False')
        break

print(total_m, sorted_total, c)
print(total_m%10000)
