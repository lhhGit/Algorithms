# i indicate the i-th order that the method will return
def Rselect(list,length,i):
    #pivot = randElement(list,start,end)
    if length<=1:
        return list[0]
    idx = partition(list,0,length)
    if idx+1 == i:
        return list[idx]
    elif idx+1 < i:
        return Rselect(list[idx+1:length],length-idx-1,i-(idx+1))
    else:
        return Rselect(list[0:idx],idx,i)



# quickSort subroutine, this is a recursive method
def quickSort(list,start,end):
    #pivot = list[start]
    if start>=end-1:
        return list[start]
    idx = partition(list,start,end)
    quickSort(list,start,idx)
    quickSort(list,idx+1,end)
    

# partition subroutine, return the position of the pivot
# i points to the boundary between elements less than pivot
# and elements bigger than pivot(the first bigger-than-pivot element)
# j points to the boundary between elements sorted and unsorted
# elements(the first unsorted element)
def partition(list,start,end):
    i = start + 1
    pivot = list[start]
    for j in range(start+1,end):
        if list[j] >  pivot:
            continue
        else:
            swap(list,j,i)
            i+=1
    #first set the pivot at the appropriate position
    swap(list,start,i-1)
    #print list
    return i-1
    
def swap(list,i,j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


m = [2,5,7,4,3,1,8,6]
# quickSort(m,0,8)
print Rselect(m,8,5)
