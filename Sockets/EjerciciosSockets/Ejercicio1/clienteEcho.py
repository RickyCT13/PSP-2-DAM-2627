import socket

# Cliente
with socket.socket() as client:
    # Mensaje de bienvenida
    print("ClienteEcho v1.0\n" \
    "Introduzca un mensaje, que será devuelto en mayúsculas.\n" \
    "Para salir, simplemente introduzca una cadena vacía.")
    client.connect(("127.0.0.1", 5555))
    exit = False
    while (not exit):
        # Recoger entrada del usuario y 
        # mandarla al servidor
        text = input("Mensaje: ")
        client.sendall(text.encode())
        # Si la cadena está vacía, salir del programa
        if (len(text) == 0):
            print(f"Saliendo del programa...")
            exit = True
        # Si no, recibir e imprimir respuesta
        # (De no restringir la espera de la respuesta a un else, el programa no podría terminar)
        else:
            response = client.recv(1024).decode()
            print(f"Respuesta del servidor: {response}")