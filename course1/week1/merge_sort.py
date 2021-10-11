def merge(A, B):
    i = j = 0
    res = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    return res + A[i:] + B[j:]


def sort(A):
    if len(A) < 2:
        return A
    m = len(A) // 2
    return merge(sort(A[:m]), sort(A[m:]))


print(sort([3, 4, 6, 8, 9, 3, 2, 4, 6, 7]))

a = []
a.sort()

def merge(arr1, arr2):
    i = j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if abs(arr1[i]) > abs(arr2[j]):
            res.append(arr2[j])
            j += 1
        elif abs(arr1[i]) < abs(arr2[j]):
            res.append(arr1[i])
            i += 1
        else:
            if arr1[i] > arr2[j]:
                res.append(arr2[j])
                j += 1
            else:
                res.append(arr1[i])
                i += 1
    return res + arr1[i:] + arr2[j:]


def absSort(arr):
    """
    @param arr: int[]
    @return: int[]
    """

    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(absSort(arr[:mid]), absSort(arr[mid:]))
