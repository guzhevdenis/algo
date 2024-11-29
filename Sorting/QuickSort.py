

def partition (test_massive):
    #Выбираем случайный остов
    index = 1
    pivot = test_massive[index]
    j = 0
    for i in range(len(test_massive)):
        if test_massive[i] < pivot:
            test_massive[i], test_massive[j] = test_massive[j], test_massive[i]
            j += 1
    return 
        



    
    








test_massive =  [-2, -7, 0, 10, 3, -5, 12, 6, 9]
partition(test_massive)
print(test_massive)