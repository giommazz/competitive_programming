"""
base case
"""

# modifying `array`
def mergesort_1(array):
    if len(array) > 1:
        half_length = round(len(array) / 2)
        array_left = array[:half_length]
        array_right = array[half_length:]
        mergesort_1(array_left)
        mergesort_1(array_right)
        # Merge the sorted halves back into the original array
        merged = merge(array_left, array_right)
        for i in range(len(merged)):
            array[i] = merged[i]
    return array


# without modifying `array`
def mergesort_2(array):
    if len(array) <= 1:
        return array 
    
    # Split the array into two halves
    half_length = round(len(array) / 2)
    left = mergesort_2(array[:half_length])
    right = mergesort_2(array[half_length:])
    
    # Merge the sorted halves and return the result
    return merge(left, right)

# takes two sorted sequences and merges them, returning one sorted sequence
def merge(left, right):
    if not left and not right:
        return
    if not left:
        return right
    if not right:
        return left
    else:
        if left[0] <= right[0]:
            return [left[0]] + merge(left[1:], right)
        else:
            return [right[0]] + merge(left, right[1:])
        
test_array = [5, 2, 9, 1, 5, 6]
a = [9, 5, 7]

print()
# print(merge(b, c))
# input()
print(mergesort_1(test_array))
print(mergesort_2(test_array))
