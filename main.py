lista=[]

while True:
    print("***** Menu De Notas *****")
    print("1. Agregar notas")
    print("2. Calcular Promedio")

    op=int(input("Ingresa un digito (1,2): "))

    if op == 1:
        nota=int(input("Ingresa la cantidad de notas: "))
        for x in range(nota):
            pp=int(input(f"Ingrese nota {x+1}: \n"))
            lista.append(pp)
            continue

        print(lista)
    
    if op == 2:
        print("Calcular Promedio")
        prom=sum(lista)/len(lista)

        print(f"El promedio de notas es {prom}")
        break
    



