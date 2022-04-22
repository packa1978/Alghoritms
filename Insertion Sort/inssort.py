tab = [8,2,1,9,5]
print(tab)

i=1 # assumption that index 0 is already sorted
while i < len(tab):# we are finishing on last element o of the tab
    key = tab[i] # used for comparison if the value of the key is higher or lower
    j = i-1 #as we are comparing with left side of the tab
    while j >= 0 and key < tab[j]:
        tab[j+ 1] = tab[j]
        j-= 1
    tab[j+ 1] = key
    i +=1
    print(tab)