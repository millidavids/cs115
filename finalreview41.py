

def prod(arr1, arr2):
    product = 1
    for index in range(len(arr1)):
        if arr1[index] < 0:
            product *= arr2[index]
    return product

list_1 = [-1, 4, 9, -2, 7]
list_2 = [9, 5, 4, 2, 1]
print(prod(list_1, list_2))