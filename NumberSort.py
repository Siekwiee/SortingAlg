import random

def BubbleSortNumbers(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

data = random.sample(range(0, 100), 100) #No number will be generated twice
#Beginner method:
'''for i in range(0,100):
    n = random.randint(1,100)
    data.append(n)'''

print(f'Unsorted: {data}')
print('---------------------')
BubbleSortNumbers(data)
print(f'Sorted array: {data}')
