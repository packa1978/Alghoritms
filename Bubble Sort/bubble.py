tab = [4,5,7,2,3,1,8]
i = 0
changed = True
while i < len(tab) -1:
    j = 0
    changed = False
    while j < len(tab)-1 -i:
        if tab[j] > tab[j+1]:
            tab[j], tab[j+1] = tab[j+1], tab[j]
            changed = True
        j+=1
    i+=1
    print(tab)