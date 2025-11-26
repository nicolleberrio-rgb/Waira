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
        print("\nPlaneación actualizada.\n")
elif opcion == "2":

        print("\n--- REGISTRO DE CLIENTES ---")
        print("1. Individual (1 persona)")
        print("2. Pareja (2 personas)")
        print("3. Familiar (4 personas)")

        tipo = input("Seleccione tipo: ")

        if tipo == "1":
            personas = 1; hab = "single"
        elif tipo == "2":
            personas = 2; hab = "double"
        elif tipo == "3":
            personas = 4; hab = "family"
        else:
            print("Tipo inválido.\n")
            continue

        # Nombres
        nombre = input("Nombre: ")
        while not validar_nombre(nombre):
            nombre = input("Nombre inválido. Intente de nuevo: ")

        apellido = input("Apellido: ")
        while not validar_nombre(apellido):
            apellido = input("Apellido inválido. Intente de nuevo: ")

        documento = input("Documento: ")
        while not validar_doc(documento):
            documento = input("Documento inválido. Intente de nuevo: ")

        noches = int(input("Noches: "))
        tours = int(input("Tours: "))

        mascota = input("¿Trae mascota? (s/n): ").lower()
        if mascota == "s":
            tipo_m = input("Tipo de mascota: ")
            nombre_m = input("Nombre de la mascota: ")
        else:
            tipo_m = ""
            nombre_m = ""

        # costos
        datos = leer_alistamiento()
        tarifa = datos[f"tarifa_{hab}"]
        total = tarifa*noches + personas*datos["precio_comida"]*noches + tours*datos["precio_tour"]

        # Guardar CSV
        with open("clientes.csv", "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([nombre,apellido,documento,tipo,personas,noches,hab,mascota,tipo_m,nombre_m,tours,total])

        print("\n[OK] Cliente registrado.")
        print("Total estimado:", total, "\n") 
    
# 3) LISTA DE CLIENTES
    elif opcion == "3":
        print("\n--- CLIENTES REGISTRADOS ---\n")
        with open("clientes.csv", "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            next(lector)
            for fila in lector:
                print(fila)
        print()

    ##opcion 4
  elif opcion == "4":
        print("\n--- MASCOTAS REGISTRADAS ---\n")
        with open("clientes.csv", "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            next(lector)
            for c in lector:
                if c[7] == "s":
                    print(f"{c[0]} {c[1]} trajo un@ {c[8]} llamad@ {c[9]}")
        print()
