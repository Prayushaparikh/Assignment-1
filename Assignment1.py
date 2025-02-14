# 1. [Category: Coding] Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log(n)) run time complexity,
# implement your algorithm in your favorite language.


def searchRange(nums, target):
    # Helper function to find the first occurrence
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1  # Move left to find the first occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    # Helper function to find the last occurrence
    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1  # Move right to find the last occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    # Perform both searches
    first = findFirst(nums, target)
    if first == -1:
        return [-1, -1]  # Target not found
    last = findLast(nums, target)
    return [first, last]


# Test cases
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(searchRange(nums1, target1))  # Output: [3, 4]

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(searchRange(nums2, target2))  # Output: [-1, -1]
