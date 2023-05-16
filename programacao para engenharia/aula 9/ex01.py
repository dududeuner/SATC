arr = [0,0,0,0,0]


while arr[0] != -1:
    arr[0] = int(input('Digite um numero: '))
    if arr[0] > 0:
        arr[1] = arr[0] + arr[1]
    arr[2] = arr[2] + 1
    if arr[0] > arr[3]:
        arr[3] = arr[0]
    if arr[0] < arr[4] and arr[0] != -1:
        arr[4] = arr[0]
        
print('Soma de todos : ', arr[1])
print('media : ', arr[1] / arr[2])
print('Numero de numeros : ', arr[2])
print('Maior numero : ',arr[3])
print('Menor numero : ',arr[4])