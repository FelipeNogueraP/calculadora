"""Programa principal de la Cacluladora."""
import menu as m

if __name__ == "__main__":
    while True:
        mi_calculadora = m.llamar_menu()
        verificar = m.validador_seleccion(mi_calculadora)
        if verificar == "Q":
            break

