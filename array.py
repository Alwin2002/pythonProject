
import numpy as n
arr = []
a = int(input("Enter size of array : "))
for i in range(a):
    arr.append(int(input()))
ab = n.array(arr)
print(ab)
print(len(ab))
b = int(input("Enter element to be inserted : "))
c = int(input("Position : "))
ab = n.insert(ab, c, b)
print(ab)
b = int(input("Enter index of element to be deleted : "))
ab = n.delete(ab, b)
print(ab)
b = int(input("Enter element to be searched : "))
r = n.where(ab==b)
print("Element",b,"is found at indices",r[0])
b = int(input("Enter index of element to be updated : "))
c = int(input("Enter value of new element: "))
ab.flat[b]=c
print(ab)
new_array = []
a = int(input("Enter length of new array to be concatenated : "))
for i in range(a):
    new_array.append(int(input()))
new = n.array(new_array)
new = n.concatenate((ab,new))
print(new)
