import array

a = array.array('i', [0, 0, 0, 0, 0])


# Accessing the element at index 2
print(a[2])

# Modifying the element at index 2
a[2] = 10
print(a[2])

# Appending a new element to the array
a.append(20)
print(a)

# Inserting an element at index 3
a.insert(3, 30)
print(a)