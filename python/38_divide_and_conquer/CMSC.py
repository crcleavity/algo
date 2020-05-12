inversion_num = 0

def merge_sort_counting(nums, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort_counting(nums, start, mid)
    merge_sort_counting(nums, mid+1, end)
    merge(nums, start, mid, end

def merge(nums, start , mid, end):
    global inversion_num
    i = start
    j = mid + 1
    tmp = []
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            inversion_num += j - mid - 1
            tmp.append(nums[i])
            i+=1
        else:
            tmp.append(nums[j])
            j += 1

        while i <= mid:
            inversion_num += end - mid
            tmp.append(nums[i])
            i += 1
        while j <= end:
            tmp.append(nums[j])
            j += 1
        nums[start:end+1] = tmp
    