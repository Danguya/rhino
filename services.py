import socket


services = {
    "TOR":9050
}


def get_service_version(port):
    try:
        return socket.getservbyport(port)
    except OSError as osError:
        return "Serviço Desconhecido"

def get_service_name():
    return