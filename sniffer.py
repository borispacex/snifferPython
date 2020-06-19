
import socket

# Creamos la maquina socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

# Iniciamos el olfateador en nuestra maquina
s.bind(("127.0.0.1", 0))
print("La maquina esta lista para olfatear ....")

while True:
     # leer en un paquete
    tcpData = s.recvfrom(65535)
    # imprime el paquete
    print(tcpData)
    print('')

# Para verificar enviamos un paquete a cualquier servidor TCP de nuestra maquina: netcat -u 127.0.0.1 8889