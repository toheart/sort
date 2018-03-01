
def quick_sort(alist, start, end):
    if start >= end:
        return 

    mid = alist[start]
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
            
        alist[low] = alist[high]

        while low < high and alist[low] < mid:
            low += 1

        alist[high] = alist[low]

    alist[low] = mid
    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)

if __name__ == "__main__":
    alist = [1,3,5,8,2,1,12,31,24,52,17]
    quick_sort(alist,0,len(alist)-1)
    print(alist)

