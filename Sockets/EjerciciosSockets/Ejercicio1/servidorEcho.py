import socket

# Servidor
with socket.socket() as server:
    # Liberar puerto para que se pueda reutilizar
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind: ligar a tupla (dirección ip, puerto)
    server.bind(("0.0.0.0", 5555))
    # Escuchar en servidor
    server.listen()

    # 
    while True:
        # Mensaje para indicar que está disponible la conexión
        print("Esperando conexión...")
        (connection, addrPort) = server.accept()
        with connection:
            print(f"Nueva conexión: {addrPort}")
            endCon = False
            while (not endCon):
                text = connection.recv(1024).decode()
                if (len(text) == 0):
                    endCon = True
                    print(f"Cadena vacía recibida, terminando conexión con {addrPort}")
                else:
                    echo = text.upper()
                    connection.sendall(echo.encode())
                    print("Respuesta enviada")
            print("Terminando conexión con este cliente...")
            