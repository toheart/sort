
def shell_sort(alist):
    n = len(alist)
    gap = n//2
    print(type(gap))
    while gap > 0:
        for i in range(gap,n):
            j = i 
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap

        gap = gap//2


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(alist)
    print(alist)

