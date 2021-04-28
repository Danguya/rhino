import socket


def get_hostname(ip):
    return socket.gethostbyname(ip)