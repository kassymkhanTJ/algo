from statistics import median

c = 0


def partition(arr, l, r):
    p = l
    m = (r + l - 1) // 2
    med = median([arr[l], arr[m], arr[r - 1]])
    if med == arr[m]:
        o = m
    elif med == arr[r - 1]:
        o = r - 1
    else:
        o = l
    arr[p], arr[o] = arr[o], arr[p]
    i = l + 1
    for j in range(i, r):
        if arr[j] < arr[p]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    i -= 1
    arr[p], arr[i] = arr[i], arr[p]
    return i


def quick_sort(arr, l, r):
    global c
    if r - l < 2:
        return
    p = partition(arr, l, r)
    c += (r - l - 1)
    quick_sort(arr, l, p)
    quick_sort(arr, p + 1, r)


# arr = [5, 4, 6, 7, 8, 3, 2]
with open("input.txt", "r") as f:
    arr = list(map(lambda line: int(line.strip()), f.readlines()))
quick_sort(arr, 0, len(arr))
print(arr)
print(c)
