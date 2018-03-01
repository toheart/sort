
def selection_sort(alist):
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]

if __name__ == "__main__":
    alist = [9,6,3,2,1,4,2,21,12,32,13]
    selection_sort(alist)
    print(alist)
