import array 

# Creat an array of integers with initial values
a = array.array('i', [10, 20, 30, 40, 50])

# Remove and return the last element of the array
last = a.pop()
print(last)
print(a)

# Remove and return the element at index 2
middle =a.pop(2)
print(middle)
print(a)