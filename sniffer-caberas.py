
import socket
import struct

# Creamos la maquina socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

# Iniciamos el olfateador en nuestra maquina
s.bind(("127.0.0.1", 0))
print("La maquina esta lista para olfatear ....")

while True:
     # leer en un paquete
    tcpData = s.recvfrom(65535)
    # print(tcpData)
    # estructuramos mejor el dato recibido
    unpackedData = struct.unpack('!BBHHHBBH4s4s', tcpData[0][:20])
    print ("Datos interpretados:", unpackedData)
    version_IHL = unpackedData[0]
    version = version_IHL >> 4
    IHL = version_IHL & 0xF
    print("Version IP:", version)
    print ("IHL(Internet Header Length):", IHL)
    print('')

# Para verificar enviamos un paquete a cualquier servidor TCP de nuestra maquina: netcat -u 127.0.0.1 8889