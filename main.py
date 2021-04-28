#!/usr/bin/python3
import socket
import os
import threading
import time
from ports import Portscanner
import grabbanner as grabing
import services
import vulnscanning as vulnScanner
import hostinfo
import json


openPorts = []
banners = ['GAMSoft','A']
vulnServices = {}

def main():
    
    target = "127.0.0.1"
    print("Executando o Rh1no 1.0 em {}".format(time.asctime()))
    
    #Escaneando portas abertas
    print("\n========================= Escaneando portas =========================\n")
    portscan = Portscanner(target, 1, 65535)
    portscan.setPorts()
    portscan.start(40)
    print(portscan.openPorts)
    
    #openPorts = portScanner.scan_port(host)
    #if len(openPorts) > 0:
    #    for openPort in openPorts:
    #       print("== Porta Aberta [{}] => ".format(openPort)+"{}".format(services.get_service_name(openPort)))
    #     print("Terminando o escaneamento de portas em {}".format(time.asctime()))
    # 
    # print("========================= Escaneando serviços =========================")
    #Serviços Vulneraveis
    #if len(banners) > 0:
    #   for banner in banners:
    #        vulnServices = vulnScanner.scan(banner)
    #        print("[+] {}".format(banner))
    #        if len(vulnServices) > 0:
    #            print("==[Name]    {}".format(vulnServices['Name']))
    #           print("==[Author]  {}".format(vulnServices['Author']))
    #            print("==[CVE]     {}".format(vulnServices['CVE']))
    #            print("==[URL]     {}".format(vulnServices['URL']))



if __name__ == "__main__":
    main()
