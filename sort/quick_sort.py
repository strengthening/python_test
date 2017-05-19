
def quick_sort(slist):
    qsort(slist, 0 , len(slist)-1)

def qsort(slist , low , high):

    if low < high:
        piovet = partitional(slist , low ,high)
        qsort(slist,low,piovet-1)
        qsort(slist,piovet + 1 , high)


def partitional(slist, low , high):
    piovetkey = slist[low]
    while low < high:
        while low < high and slist[high] > piovetkey:
            high -= 1
        slist[low], slist[high] = slist[high], slist[low]

        while low < high and slist[low] < piovetkey :
            low += 1
        slist[low], slist[high] = slist[high], slist[low]        

    return low

if __name__ == '__main__':
    slist = [3,2,1,5,23,6,9,10]
    quick_sort(slist)

    print slist