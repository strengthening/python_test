def merge_sort(seq):
    # msort(slist , copy.deepcopy(slist) , 0 , len(slist))
    if len(seq) <= 1:
        return seq

    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])

    return merge(left,right)

def merge(left,right):
    result = []
    i , j = 0 , 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]  
    result += right[j:] 

    return result

if __name__ == '__main__':
    # print 'hehe'
    slist = [3,2,1,5,23,6,9,10]
    print merge_sort(slist)