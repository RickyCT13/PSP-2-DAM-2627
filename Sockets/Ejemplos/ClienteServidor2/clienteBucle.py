import socket

with socket.socket() as cliente:
    cliente.connect(("127.0.0.1", 5555))
    
    while True:
        texto = input(f"Escribe un número: ")
        cliente.sendall(texto.encode())

        if (int(texto) < 0):
            break

        estado = cliente.recv(1024).decode()
        if estado == "ok":
            print("Operación completada con éxito")
        else:
            print("Ha ocurrido un error")