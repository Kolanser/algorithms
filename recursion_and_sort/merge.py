def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]
    l, r, k = 0, 0, 0
    result = [None] * len(arr)
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1
    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1
    return result


def merge_sort(arr, lf, rg):
    def sort(arr, lf, rg):
        if rg - lf == 1:
            return arr[lf:rg]
        mid = (rg + lf) // 2
        left = sort(arr, lf, mid)
        right = sort(arr, mid, rg)
        return merge(
            left + right, 0, (len(left + right) // 2), len(left + right)
        )
    arr[:] = sort(arr, lf, rg)
