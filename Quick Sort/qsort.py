tabs = [8,2,1,9,5]

arr=[1,2,3,4,5,6,7,8]
print(tabs)

def divide(tab, start, end):
    pivot = tab[end]
    low_element = start
    high_element = end-1
    while True :
        while low_element <= high_element and tab[low_element] <= pivot :
            low_element += 1
        while low_element <= high_element and tab[high_element]>= pivot:
            high_element -= 1

        if low_element <= high_element:
            tab[low_element], tab[high_element] = tab[high_element], tab[low_element]
        else:
            break

    tab[end],tab[low_element] = tab[low_element], tab[end]
    return low_element

def quickSort(tab, start, end):
    if start < end:
        pivot = divide(tab,start,end)
        quickSort(tab,start,pivot - 1)
        quickSort(tab, pivot + 1, end)
    print(tab)

quickSort(tabs, 0, len(tabs)-1)
print(tabs)

quickSort(arr,0, len(tabs))
print(arr)
