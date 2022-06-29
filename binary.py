# Binary search recursive method
def binary_search(input_array, value):
    if len(input_array) == 1:
        if input_array[0] != value:
            return -1
        else:
            return value
       
    med = len(input_array)//2
    if input_array[med] == value:
        return value
    if input_array[med] < value:
        return binary_search(input_array[med+1: len(input_array)], value)
    if input_array[med] > value:
        return binary_search(input_array[0: med-1], value)

'''
Binary search 

def binary_search(input_array, value):
    minimum= 0
    maximum= len(input_array)
    

    while minimum < maximum:
        middle= (minimum + maximum)//2
        if input_array[middle] < value:
            minimum = middle+1
           
        elif input_array[middle] > value:
            maximum = middle 
        else:
            return middle
    
    return -1
'''


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))