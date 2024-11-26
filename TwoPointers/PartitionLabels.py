def PartitionLabels(s):

    last_letters  = {}
    partitions = [0]
    for i, element in enumerate(s):
        last_letters[element] = i

    j = last_letters[s[0]]
    for i, element in enumerate(s):
        if (i == j):
            partitions.append(j+1)
        elif (i < j and last_letters[element] <=j):
            continue

        elif(last_letters[element] >= j):
            j = last_letters[element]
            if (j == i):
                partitions.append(j+1)
    lenghts = [partitions[i+1]-partitions[i] for i in range(len(partitions)-1)]
    return lenghts

s = "eaaaabaaec" 
print(PartitionLabels(s))

