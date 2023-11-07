def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

array_bubble = ['B', 'D', 'A', 'E']
resultado_bubble = bubble_sort(array_bubble.copy())
print(f'Bubble Sort: {resultado_bubble}')
