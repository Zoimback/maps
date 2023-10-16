import socket
import sys
sys.path.append("/home/alex/Scripts/py-maps")
import methods_motor


methods.start()
try:
    # Configura el servidor

    server_ip = "0.0.0.0"  # Escucha en todas las interfaces
    server_port = 12345

    # Crea un socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula el socket a la dirección y el puerto
    server_socket.bind((server_ip, server_port))

    # Escucha conexiones entrantes
    server_socket.listen(5)

    print(f"Servidor escuchando en {server_ip}:{server_port}")

    # Acepta conexiones entrantes
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")

    # Comunicación con el cliente
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Recibido: {data.decode()}")
        response = methods.right(0.2)


        client_socket.send(response.encode())
except Exception as e:

    print("Failed\n Salida: {}",str(e))

finally:
# Cierra el socket del cliente y el servidor
    client_socket.close()
    server_socket.close()



