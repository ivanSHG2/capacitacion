
# cine moro boleteria
#Variables

i = 1

entradas_nino = 0
entradas_joven = 0
entradas_adulto = 0
entradas_totales = 0
ganancia_total = 0

#Ciclo

while i == 1:
    try:
        print("Bienvenido a cine Moro")
        edad = int(input("Por favor ingrese la edad del cliente "))
        if edad >= 1 and edad <= 13:
            print("Su categoria es niño")
            print("El precio por entrada para su edad es 5500")
            num_entradas = int(input("¿Cuantas entradas desea? "))
            gasto_total = num_entradas * 5500
            print("Categoria = Niño")
            print("Cantidad de entradas = ",num_entradas)
            print("Total a pagar = $",gasto_total)
            print("Gracias por su compra, disfrute la funcion")
            entradas_totales = entradas_totales + num_entradas
            ganancia_total = ganancia_total + gasto_total
            entradas_nino = entradas_nino + num_entradas
        elif edad >= 14 and edad <= 21:
            print("Su categoria es joven")
            print("El precio por entrada para su edad es 7000")
            num_entradas = int(input("¿Cuantas entradas desea? "))
            gasto_total = num_entradas * 7000
            print("Categoria = Joven")
            print("Cantidad de entradas = ",num_entradas)
            print("Total a pagar = $",gasto_total)
            print("Gracias por su compra, disfrute la funcion")
            entradas_totales = entradas_totales + num_entradas
            ganancia_total = ganancia_total + gasto_total
            entradas_joven = entradas_joven + num_entradas
        elif edad >= 22:
            print("Su categoria es adulto")
            print("El precio por entrada para su edad es 9000")
            num_entradas = int(input("¿Cuantas entradas desea? "))
            gasto_total = num_entradas * 9000
            print("Categoria = Adulto")
            print("Cantidad de entradas = ",num_entradas)
            print("Total a pagar = $",gasto_total)
            print("Gracias por su compra, disfrute la funcion")
            entradas_totales = entradas_totales + num_entradas
            ganancia_total = ganancia_total + gasto_total
            entradas_adulto = entradas_adulto + num_entradas
        else:
            print("Valor fuera de rango")
        
        i = int(input("¿Desea continuar con la venta de entradas? 1 = si otro numero = no "))
    except:
        print("Caracter Erroneo")

#Calculo de porcentajes        
por_nino = (entradas_nino*100)/entradas_totales
por_joven = (entradas_joven*100)/entradas_totales
por_adulto = (entradas_adulto*100)/entradas_totales

#Muestra de resultados por pantalla
print("El total de entradas de niño fue ",entradas_nino,"correspondiente al ",por_nino,"% del total de entradas")
print("El total de entradas de joven fue ",entradas_joven,"correspondiente al ",por_joven,"% del total de entradas")
print("El total de entradas de adulto fue ",entradas_adulto,"correspondiente al ",por_adulto,"% del total de entradas")
print("El dinero recaudado por la venta de entradas es ", ganancia_total)