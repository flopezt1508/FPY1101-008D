def raiz(num):
    raiz=num**0.5
    return raiz

while True:
    try:
        numero=float(input("Ingrese un nùmero a calcular la raiz : "))
        break
    except ValueError:
        print("Error, debe ingresar solamente nùmeros!!")
print (f"La raiz cuadrada de {numero} es : {raiz(numero)}")