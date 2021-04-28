import socket
import hostinfo
import threading
from queue import Queue


class Portscanner():

    openPorts = []
    target = ''
    queue = Queue()
    begin_port = 1
    end_port = 65535
    important_ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]

    def __init__(self, target, begin = begin_port, end = end_port):
        self.target      = socket.gethostbyname(target)
        self.begin_port  = begin
        self.end_port    = end
        print(self.target)
        
    def setPorts(self, mode = 2, ports = ''):
        if mode == 1:
            for port in range(1,1025):
                self.queue.put(port)
        elif mode == 2:
            for port in range(self.begin_port, self.end_port):
                self.queue.put(port)
        elif mode == 3:
            ports = self.important_ports
            for port in ports:
                self.queue.put(port)
        elif mode == 4:
            ports = ports.split()
            ports = list(map(int, ports))
            for port in ports:
                self.queue.put(port)

    def getPorts(self):
        return self.queue
    
    def scan(self, port):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(2)
            client.connect((self.target, port))
            return True
        except:
            return False
    
    def worker(self):
        while not self.getPorts().empty():
            port = self.getPorts().get()
            if self.scan(port):
                print("==> open {} ".format(port))
                self.openPorts.append(port)

    def start(self, threads):
        thread_list = []
        for t in range(threads):
            thread = threading.Thread(target=self.worker)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()

        print("Open ports are:", self.openPorts)