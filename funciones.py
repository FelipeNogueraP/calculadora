""" Funciones del programa, operaciones matematicas"""

from math import sin, cos
import numpy as np


def sumar(num1, num2):
    resultado = num1 + num2
    return resultado


def restar(num1, num2):
    resultado = num1 - num2
    return resultado


def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado


def dividir(num1, num2):
    resultado = num1 / num2
    return resultado


def raiz(num1):
    arr = [num1]
    arr_sqrt = np.sqrt(arr)
    return arr_sqrt


def exponente(num1, num2):
    resultado = num1 ** num2
    return resultado


def seno(num1):
    resultado = sin(num1)
    return resultado


def coseno(num1):
    resultado = cos(num1)
    return resultado


def r_input(mensaje):
    valor = input(mensaje)
    return valor


