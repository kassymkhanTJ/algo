while True:
    start, first, second, third = list(map(int, input().split(" ")))
    if sum([start, first, second, third]) == 0:
        break
    total = 120
    total += start - first
    if start < first:
        total += 40
    total += second - first
    if second < first:
        total += 40
    total += second - third
    if second < third:
        total += 40
    print(total * 9)
