# Imports
import socket

# Creación de socket
servidor = socket.socket()

# Liberar puerto para que se pueda reutilizar
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind

# Tupla (protocolo), ip, puerto
servidor.bind(("0.0.0.0", 5555)) # 0.0.0.0 = Todas las direcciones de red
# También:
# ipServidor = "0.0.0.0"
# puertoServidor = 5555
# tupla = (ipServidor, puertoServidor)
# servidor.bind(tupla)

# Listen
# servidor.listen(10) # Tamaño de la cola / nºclientes que pueden esperar hasta ser atendidos
servidor.listen() # backlog = 4096

# Accept
(cliente, ipPuertoCliente) = servidor.accept()

# Almacenar ip y puerto cliente
(ipCliente, puertoCliente) = ipPuertoCliente
# Imprimir (opcional)
print("IP: ", ipCliente, ", Puerto: ", puertoCliente)

# Recibir mensaje (paquete)
mensaje = cliente.recv(1024) # Buffer de recepción (bytes)

# Decodificar mensaje de bytes a texto
texto = mensaje.decode()

print("Texto recibido: ", texto)


# Mandar mensaje de vuelta
texto = "Recibido."

mensaje = texto.encode()

cliente.sendall(mensaje)


# Cerrar cliente y servidor
cliente.close()
servidor.close()
