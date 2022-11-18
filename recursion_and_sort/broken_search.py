# 72091779
def binary_search(nums, target, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search(nums, target, left, mid)
    return binary_search(nums, target, mid + 1, right)


def binary_search_broken_index(nums, left, right):
    mid = (left + right) // 2
    if right - left == 1:
        return mid
    if nums[mid] < nums[left]:
        return binary_search_broken_index(nums, left, mid)
    return binary_search_broken_index(nums, mid, right)


def broken_search(nums, target) -> int:
    if not nums:
        return -1
    broken_index = binary_search_broken_index(nums, 0, len(nums))
    if nums[0] <= target <= nums[broken_index]:
        return binary_search(nums, target, 0, broken_index + 1)
    elif target <= nums[-1]:
        return binary_search(nums, target, broken_index + 1, len(nums))
    return -1
