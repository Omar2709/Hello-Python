import time
start_time = time.time()

#outer loop
for i in range(100):
    #inner loop
    for j in range(10000):
        print(0, end = " ")
    print()  # Move to the next line after inner loop completes

print(round(time.time() - start_time, 2), "seconds")

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
for num in range(len(num_list)):
    print(num_list[num])
    if num_list[num] > 45:
        print("Mayor que 45:", num_list[num])
    else:
        print("Menor o igual a 45:", num_list[num])

for indice, num in enumerate(num_list):
    if num == 36:
        print("El número 36 se encuentra en el índice:", indice)
        break

count = 0
for indice, num in enumerate(num_list):
    count += 1
    if num == 36:
        print("El número 36 se encuentra en el índice:", indice)
        break
print(count)