import socket

# Cliente
with socket.socket() as client:
    # Mensaje de bienvenida
    print("ClienteEcho v1.0\n" \
    "Introduzca un mensaje, que será devuelto en mayúsculas.\n" \
    "Para salir, simplemente introduzca una cadena vacía.")
    client.connect(("127.0.0.1", 5555))
    # Contar intentos 
    attempts = 0
    # Exit (para indicar cuando salir del bucle)
    exit = False
    while (not exit):
        # Cada vez que se repita el bucle equivale a un nuevo intento.
        attempts += 1
        # Recoger entrada del usuario y mandarla al servidor
        number = int(input("Número: "))
        client.sendall(str(number).encode())
        # Recibir respuesta
        response = int(client.recv(1024).decode())
        # print(f"Respuesta: {response}")
        match (response):
            # 1 - Intento > Secreto
            case 1:
                print(f"El número introducido ({number}) es MAYOR que el número secreto.")
            # -1 - Intento < Secreto
            case -1:
                print(f"El número introducido ({number}) es MENOR que el número secreto.")
            # 0 - Intento = Secreto
            case 0:
                # Mostrar número de intentos y salir
                print(f"El número introducido ({number}) ES el número secreto.")
                print(f"Número de intentos: {attempts}" 
                      + "\n¡Felicidades!"
                      + "\nSaliendo del programa...")
                exit = True