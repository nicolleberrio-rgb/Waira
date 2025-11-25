import os
import csv

def leer_alistamiento():
    datos = {}
    with open("alistamiento.txt", "r", encoding="utf-8") as f:
        for linea in f:
            k, v = linea.strip().split("=")
            try:
                if "." in v:
                    v = float(v)
                else:
                    v = int(v)
            except:
                pass
            datos[k] = v
    return datos


def guardar_alistamiento(datos):
    with open("alistamiento.txt", "w", encoding="utf-8") as f:
        for k, v in datos.items():
            f.write(f"{k}={v}\n")


def validar_nombre(n):
    return n.isalpha() and len(n) >= 3

def validar_doc(d):
    return d.isdigit() and 3 <= len(d) <= 15

continuar = True

while continuar:

    print("""
===================================================
          WAIRA RESORT NATURAL SYSTEM
====================================================
1. Planeación de la demanda
2. Registro de clientes
3. Registro de clientes registrados
4. Control de mascotas registradas
5. Cálculo automático de costos, ventas y ganancias
6. Exportar administración (Requiere validación)
7. Salir
""")

    opcion = input("Seleccione una opción: ")
    ##opcion 1 
if opcion == "1":
        datos = leer_alistamiento()
        print("\n--- ALISTAMIENTO ACTUAL ---")
        for k, v in datos.items():
            print(k, "=", v)

        print("\nModifique valores (enter para mantener):")
        for k in datos:
            nuevo = input(f"{k} [{datos[k]}]: ")
            if nuevo.strip() != "":
                try:
                    if "." in nuevo:
                        datos[k] = float(nuevo)
                    else:
                        datos[k] = int(nuevo)
                except:
                    datos[k] = nuevo

        guardar_alistamiento(datos)
        print("\n[OK] Planeación actualizada.\n")
