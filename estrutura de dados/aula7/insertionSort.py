def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        marcado = array[i]
        j = i - 1
        while j >= 0 and marcado < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = marcado
    return array

array_insertion = [1, 7, 2, 5]
resultado_insertion = insertion_sort(array_insertion.copy())
print(f'Insertion Sort: {resultado_insertion}')