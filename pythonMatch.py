http_status = int(input("Enter the HTTP status code: "))

if http_status == 200 or http_status == 201:
    print("Request was successful.")
elif http_status == 400:
    print("Bad request. Please check your input.")
elif http_status == 404:
    print("Resource not found. Please check the URL.")
elif http_status == 500 or http_status == 501:
    print("Server error. Please try again later.")  
else:
    print("Unexpected status code received:", http_status)


#AQUI PONDREMOS EN PRACTICA LO QUE HEMOS APRENDIDO EN EL CURSO DE PYTHON USANDO MATCH

match http_status:
    case 200 | 201:
        print("Request was successful.")
    case 400:
        print("Bad request. Please check your input.")
    case 404:
        print("Resource not found. Please check the URL.")
    case 500 | 501:
        print("Server error. Please try again later.")
    case _:
        print("Unexpected status code received:", http_status)