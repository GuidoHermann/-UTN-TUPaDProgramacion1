# TP Secuenciales
# Guido Hermann Alzogaray

# Ejercicio 1 

print("Hello World")

# Ejercicio 2 

nombre = input("Por favor,Ingresa tu nombre: ")
print(f"Hola {nombre}")

# Ejercicio 3

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apiellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa donde vives")

print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

# Ejercicio 4 

pi = 3.14

radio = float(input("Ingresa el radio de tu circulo: "))
area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"El area de tu circulo es: {area}")
print(f"El perimetro de tu circulo es: {perimetro}")

# Ejercicio 5

segundos = int(input("Ingresa la cantidad de segundos: "))

horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas} horas")

# Ejercicio 6

numero = int(input("Ingrese un numero para ver su tabla de multiplicar :"))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i} ")

# Ejercicio 7 

num1 = int(input("ingresa un numero (distinto de 0): "))
num2 = int(input("Ingresa otro numnero(distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"La suma es {suma}")
print(f"La resta es {resta}")
print(f"La multiplicacion es {multiplicacion}")
print(f"La division es {division}")

# Ejercicio 8

peso = float(input("ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu indice de masa corporal (IMC) es: {imc}")

# Ejercicio 9

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = (9/5) * celsius + 32

print(f"{celsius} Grados celsius equivalen a {fahrenheit} grados fahrenheit")

# Ejercicio 10

num1 = float(input("Ingresa el primer numero "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

promedio = (num1 + num2 + num3 ) / 3

print(f"El promerio es: {promedio}")