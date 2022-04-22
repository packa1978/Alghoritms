tabs = [8,2,1,9,5]
print(tabs)

def mergeSort(tab):
    if len(tab) > 1 :# divide the problem if 2 or more elements
        middle = len(tab)// 2
        left = tab[:middle]
        right = tab[middle:]
        print(f'"left:"{left} "right :" {right}')
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):# may have different lengths
            if left[i] < right[j]:
                tab[k] = left[i]
                i += 1
            else:
                tab[k] = right[j]
                j += 1
            k += 1
        while i < len(left):# check if any of the lists still have elements
            tab[k]= left[i]
            i += 1
            k += 1

        while j < len(right):
            tab[k] = right[j]
            j +=1
            k +=1
        print("after", tab)

mergeSort(tabs)
print(tabs)