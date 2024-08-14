'''
Disclaimer: Este texto no contiene tildes
v2: Suponga que esta construyendo un sistema para una discoteca
y necesita revisar la entrada de N personas. Por cada persona necesita decidir
si es mayor de edad puede ingresar, si no lo es, no puede.
'''

n = int(input("Ingrese cuantas personas van a ingresar: "))
for contador in range(0, n):
    while True:
        edad = input(f"Ingrese la edad de la persona {contador + 1} : ")
        try:
            edad = float(edad)

            if edad >= 18:
                print("Bienvenido, puede ingresar")
            else:
                print("No puede ingresar a la fiesta")

            break
        except:
            print("error: la edad debe ser un valor numerico")