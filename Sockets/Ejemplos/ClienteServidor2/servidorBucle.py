import socket

with socket.socket() as servidor:
    # Liberar puerto para que se pueda reutilizar
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(("0.0.0.0", 5555))
    servidor.listen()
    

    while True:
        (conexion, dirPuerto) = servidor.accept()
        with conexion:
            print(f"Conexión recibida: {dirPuerto}")
            suma = 0
            salir = False
            while (not salir):
                valor = int(conexion.recv(1024).decode())
                print(f"Recibido valor: {valor}")
                if (valor < 0):
                    salir = True
                    break
                suma += valor
                conexion.sendall("ok".encode())
            print(f"Suma: {suma}")
    

    