"""Menu principal del programa."""

import funciones as f


def menu():
    print("""
    ***************************************
    *        Menú Calculadora             *
    *                                     *
    *      1. Sumar                       *
    *      2. Restar                      *
    *      3. Multiplicar                 *
    *      4. Dividir                     *
    *      5. Raiz                        *
    *      6. Exponente                   *
    *      7. Seno                        *
    *      8. Coseno                      *
    ***************************************
    """)


def llamar_menu():
    menu()
    print("Si desea detener el programa presione la tecla 'q'.")
    seleccion = f.r_input("¿Que operación aritmetica desea realizar?: ")
    return seleccion


def validador_seleccion(seleccion):
    if seleccion == "1":
        num1 = float(f.r_input("Para Sumar, ingrese un primer número: "))
        num2 = float(f.r_input("Ingrese el número a sumar: "))
        resultado = f.sumar(num1, num2)
        print(f"El resultado de la Suma es: {resultado}")

    elif seleccion == "2":
        num1 = float(f.r_input("Para Restar, ingrese un primer número: "))
        num2 = float(f.r_input("Ingrese el número a restar: "))
        resultado = f.restar(num1, num2)
        print(f"El resultado de la Resta es: {resultado}")

    elif seleccion == "3":
        num1 = float(f.r_input("Para Multiplicar, ingrese un primer número: "))
        num2 = float(f.r_input("Ingrese el número a multiplicar: "))
        resultado = f.multiplicar(num1, num2)
        print(f"El resultado de la Multiplicación es: {resultado}")

    elif seleccion == "4":
        num1 = float(f.r_input("Para Dividir, ingrese un primer número: "))
        num2 = float(f.r_input("Ingrese el número en el cual se divide: "))
        resultado = f.dividir(num1, num2)
        print(f"El resultado de la División es: {resultado}")

    elif seleccion == "5":
        num1 = float(f.r_input("Para calcular la Raiz, ingrese un número: "))
        resultado = f.raiz(num1)
        print(f"La Raiz de {num1} es : {resultado}")

    elif seleccion == "6":
        num1 = float(f.r_input("Para calcular la Potencia(Exponente), ingrese un primer número: "))
        num2 = float(f.r_input("Ingrese un numero al cual se elevará: "))
        resultado = f.exponente(num1, num2)
        print(f"El resultado del Exponente es: {resultado}")

    elif seleccion == "7":
        num1 = float(f.r_input("Para calcular el Seno, ingrese un número: "))
        resultado = f.seno(num1)
        print(f"El Seno de {num1} es : {resultado}")

    elif seleccion == "8":
        num1 = float(f.r_input("Para calcular el Coseno, ingrese un número: "))
        resultado = f.coseno(num1)
        print(f"El Coseno de {num1} es : {resultado}")

    elif seleccion == "Q" or seleccion == "q":
        resultado = "Q"
        print("Adios.")

    else:
        print("El valor ingresado no es valido, intente de nuevo.")

    return resultado
