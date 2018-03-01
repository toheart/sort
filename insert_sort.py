
def insert_sort(alist):
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

if __name__ == "__main__":
    alist = [23,24,25,12,32,15,17,14,73]
    insert_sort(alist)
    print(alist)

