import socket
import random

# Servidor
with socket.socket() as server:
    # Liberar puerto para que se pueda reutilizar
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind: ligar a tupla (dirección ip, puerto)
    server.bind(("0.0.0.0", 5555))
    # Escuchar en servidor
    server.listen()

    # Bucle para que esté constantemente esperando una conexión
    while True:
        secretNo = 0
        (connection, addrPort) = server.accept()
        with connection:
            print(f"Nueva conexión: {addrPort}")
            secretNo = random.randint(1, 100)
            endCon = False
            while (not endCon):
                attempt = int(connection.recv(1024).decode())
                # Intento > Secreto
                if (attempt > secretNo):
                    code = 1
                # Intento < Secreto
                elif (attempt < secretNo):
                    code = -1
                # Intento = Secreto
                else:
                    code = 0
                    endCon = True
                # Tras la comparación, mandar código al cliente 
                # (y terminar conexión en caso de que se haya adivinado)
                connection.sendall(str(code).encode())
                print("Respuesta enviada")
            print("Terminando conexión con este cliente...")