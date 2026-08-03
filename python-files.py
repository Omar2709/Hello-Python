#Opcion 1: Crea el archivo y escribe en él, lo reemplaza si ya existe
with open('new_file.txt', 'w') as file:
    file.writelines(['This is a new file created using the with statement.\n', 'This is the second line.\n'])

#Opcion 2: Crea el archivo y escribe en él, agrega al final si ya existe
with open('new_file.txt', 'a') as file:
    file.writelines(['This line is appended to the file.\n', 'This is another appended line.\n'])

#Opcion 3: Usando Try y Except para manejar errores al abrir el archivo que no existe
try:
    with open('sample/new_file.txt', 'a') as file:
        file.writelines(['This line is appended to the file.\n', 'This is another appended line.\n'])
except FileNotFoundError as e:
    print("Error: File not found.", e)