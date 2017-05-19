

def bubble_sort(slist):
    for i in range(0,len(slist)):
        # print i
        for j in range(i + 1 , len(slist)):
            if slist[i] > slist[j]:
                slist[i] , slist[j] = slist[j] , slist[i]
    print slist



if __name__ == '__main__':
    print ('冒泡排序法=========')

    slist = [3,2,1,5,23,6,9,10]

    bubble_sort(slist)

