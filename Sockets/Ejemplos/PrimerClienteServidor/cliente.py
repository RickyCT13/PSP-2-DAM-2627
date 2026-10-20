# Imports
import socket

# Creación socket cliente
cliente = socket.socket()

# Conexión cliente a localhost:5555
cliente.connect(("127.0.0.1", 5555))

texto = "Hola mundo"

# Codificar texto a bytes
mensaje = texto.encode()

# Mandar paquete mensaje
cliente.sendall(mensaje)

# Recibir mensaje
mensaje = cliente.recv(1024)
texto = mensaje.decode()

print("Respuesta del servidor: ", texto)

# Cerrar cliente (No es necesario si se usa "with")
cliente.close()
