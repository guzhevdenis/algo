def Merge(List_1,List_2):
    SortedList = []
    i = j = 0
    while  i < len(List_1) and j < len(List_2):
        if List_1[i] < List_2[j]:
            SortedList.append(List_1[i])
            i += 1
        else:
            SortedList.append(List_2[j])
            j += 1
       
    while (i < len(List_1) ):
        SortedList.append(List_1[i])
        i += 1

    while (j < len(List_2)):
        SortedList.append(List_2[j])
        j += 1
    return SortedList

def MergeSort(list):
     if len(list) == 1:
        return list
     FirstHalf = list[0:len(list)//2]
     SecondHalf = list[len(list)//2:]
     SortedFirstHalf = MergeSort(FirstHalf)
     SortedSecondHalf = MergeSort(SecondHalf)
     SortedList = Merge(SortedFirstHalf,SortedSecondHalf)
     return SortedList


list = [2, 1, 7, 4, 5, 0]

sorts = MergeSort(list)
print(sorts)