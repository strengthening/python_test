
def selection_sort(slist):
    for i in xrange(0 , len(slist)):

        min = i
        for j in xrange(i+1, len(slist)):
            if slist[j] < slist[min]:
                min = j

        if min != i :
            slist[i],slist[min] = slist[min],slist[i]

    print slist

if __name__ == '__main__':

    slist = [3,2,1,5,23,6,9,10]
    selection_sort(slist)