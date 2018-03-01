
def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    num = len(alist)/2
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])

    return merge(left, right)

def merge(left, right):
    l, r = 0, 0 
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]
    return result

if __name__ == "__main__":
    alist = [43, 23, 1,52, 63, 42, 25, 3, 53]
    sorted_alist = merge_sort(alist)
    print(sorted_alist)
