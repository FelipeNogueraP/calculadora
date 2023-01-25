import funciones as f
import menu as m


flag = True

while flag:
    m.menu()
    seleccion = f.r_input("¿Que operación aritmetica desea realizar?: ")
    if seleccion == "1":
        num1 = float(f.r_input("Para sumar, ingrese un primer numero: "))
        num2 = float(f.r_input("Ingrese un segundo numero: "))
        print(f"El resultado de la Suma es: {f.sumar(num1, num2)}")

    elif seleccion == "2":
        num1 = float(f.r_input("Para sumar, ingrese un primer numero: "))
        num2 = float(f.r_input("Ingrese un segundo numero: "))
        print(f"El resultado de la Suma es: {f.sumar(num1, num2)}")


