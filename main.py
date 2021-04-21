#!/usr/bin/python3
import socket
import os
import threading
from ports import *
from grabbanner import *
from services import *
from vulnscanning import scanVuln

openPorts = []
banners = []

def main():
    threads = list()
    host = "127.0.0.1"
    print("[*] Escaneando portas abertas em {}".format(host))
    openPorts = scan_port("127.0.0.1")
    for port in openPorts:
        print(str(port) +" "+str(get_service_port(port)))
    getBanners("127.0.0.1", openPorts)

    vulnerabilidades = scanVuln("YahooPOPs! Simple Mail Transfer Service Ready")
    if len(vulnerabilidades) > 0:
        print("[!] Bug's encontrados - [{}]".format(len(vulnerabilidades)))
        for bug in vulnerabilidades:
            print("[+] Vulnerável - {}".format(bug))
    else:
        print("[+] Nenhum bug encontrado")


if __name__ == "__main__":
    main()