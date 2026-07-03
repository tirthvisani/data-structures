ls1 = [1, 5, 8, 10]
ls2 = [2, 4, 7, 9]

i = 0
j = 0
merge = []

while i < len(ls1) and j < len(ls2):
    if ls1[i] < ls2[j]:
        merge.append(ls1[i])
        i += 1
    else:
        merge.append(ls2[j])
        j += 1

while i < len(ls1):
    merge.append(ls2[i])
    i += 1

while j < len(ls2):
    merged.append(ls2[j])
    j += 1

print("Merged List:", merge)
