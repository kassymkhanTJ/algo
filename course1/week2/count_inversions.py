def merge_count(A, B):
    i = j = 0
    res = []
    inv = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            inv += (len(A) - i)
            j += 1
    return res + A[i:] + B[j:], inv


def sort(A):
    if len(A) < 2:
        return A, 0
    m = len(A) // 2
    left, l_inv = sort(A[:m])
    right, r_inv = sort(A[m:])
    A, inv = merge_count(left, right)
    return A, l_inv + r_inv + inv


print(sort([8, 7, 6, 5, 4, 3, 2, 1]))
