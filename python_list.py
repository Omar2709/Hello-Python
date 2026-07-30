list1 = [1, 2, 3, 4, 5]

print (list1, sep = ", ")

list1.insert(len(list1), 6)

list1.append(7)

list1.extend([8, 9, 10])

list1.pop(9)

del list1[0]

for i in list1:
    print ("Value is: ", i)