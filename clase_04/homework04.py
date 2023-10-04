
def convert_to_list(list_str_numbers):
    list_numbers = []

    for str_num in list_str_numbers:
        list_numbers.append(int(str_num.strip()))
    return list_numbers

#Exercise 1: Crea una list con 5 numeros enteros, agrega un numero al final, 
#elimina el numero en la posicion 2y modifica el ultimo numero por 100
def exercise1():
    list_numbers = convert_to_list(input("Enter a list of 5 integers separated by a comma (Ex: 2,1.2,3): ").split(","))

    add_number = int(input("Enter another number: "))
    list_numbers.append(add_number)
    print(f"{add_number} was added to the list: {list_numbers}")
    eliminated_number = list_numbers.pop(1)
    print(f"{eliminated_number} was removed from the list: {list_numbers}")
    list_numbers[-1] = 100
    print(f"Last item of the list was modified: {list_numbers}")

#exercise1()

#Exercise 2: Crea una tupla con los dias de la semana y verifica si "Domingo" esta en la tupla
def exercise2():
    week_days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    word_to_check = input("Type a word in English to check if it's a weekday: ").lower()

    if week_days.count(word_to_check) > 0:
        print(f"{word_to_check.capitalize()} is a weekday!")
    else:
        print(f"{word_to_check.capitalize()} is not a weekday. Try again")

#exercise2()

#·xercise 3: Crea un diccionario con 3 pares clave-valor representando un libro (titulo, año, autor)
#Añade el numero de paginas, moficiando el diccionario
def exercise3(): 
    book_dict = {
        "title": "Fixing your Scrum",
        "author": "Ryan Ripley, Todd Miller",
        "published_year": "2020"
    }

    number_pages = int(input(f'Type the number of pages of book \"{book_dict["title"]}\": '))
    book_dict["pages"] = number_pages
    print("Information of the book:")
    print(f'Title: {book_dict["title"]}')
    print(f'Author(s): {book_dict["author"]}')
    print(f'Published year: {book_dict["published_year"]}')
    print(f'Number of pages: {book_dict["pages"]}')

#exercise3()

#Exercise 4: Crea dos sets, uno con los numeros del 1 al 5, y otro con los numeros del 3 al 7.
#Encuentra la interseccion y la diferencia entre ambos
def exercise4():
    set1 = set(convert_to_list(input("Enter a list of integers separated by a comma (Ex: 2,1.2,3): ").split(",")))
    set2 = set(convert_to_list(input("Enter a list of integers separated by a comma (Ex: 2,1.2,3): ").split(",")))

    intersection_set = set1.intersection(set2)
    difference_set = set1.difference(set2)

    print(f"Intersection set is: {intersection_set}")
    print(f"Difference set is: {difference_set}")

#exercise4()   

#Exercise 5: Utiliza un bucle while para imprimir los numeros del 1 al 5
def exercise5():
    limit = int(input("Print numbers up to (Type a number): "))
    index = 1

    while index <= limit:
        print(index)
        index += 1

#exercise5()    

#Exercise 6: Utiliza un bucle for y la funcion range() para imprimir los numeros del 1 al 5
def exercise6():
    limit = int(input("Print numbers up to (Type a number): "))
  
    for index in range(1, limit + 1):
        print(index)

#exercise6()

#Exercise 7: Crea una funcion que calcula el area de un rectangulo
def calculate_rectangle_area(rect_width, ret_height):
    return rect_width * ret_height

def exercise7():
    width = float(input("Type the width of the rectangle: "))
    height = float(input("Type the height of the rectangle: "))
    area = calculate_rectangle_area(width, height)

    print(f"The area of the rectangle is {area}.")

#exercise7()

#Exercise 8: Define una funcion es_par que tome un numero como argumento 
# y retorne True si el numero es par, y False si es impar
def es_par(number):
    return number % 2 == 0

def exercise8():
    number = int(input("Enter a number: "))

    if es_par(number):
        print(f"Number {number} is even")
    else:
         print(f"Number {number} is odd")

exercise8()
