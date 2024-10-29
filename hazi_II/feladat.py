# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147

def nyertes_korok(list1, list2):
    if len(list1) == 0 or len(list2) == 0 or len(list1) != len(list2):
        return -1
    count = 0
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            count += 1
    return count


list1 = [30, 50, 10, 80, 100, 40]
list2 = [60, 20, 10, 20, 30, 20]
print(nyertes_korok(list1, list2))
