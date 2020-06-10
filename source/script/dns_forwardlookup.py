import socket 

class MainClass:

    def __init__(self, target):
        self.target = target
        self.name = "dns_forwardlookup"
        self.out = []
        self.error = []
        self.status = -1
        self.accept = ["dn"]
        self.warnings = []

    def main(self):
        try: 
            self.out.append(socket.gethostbyname(self.target) + "\t" + self.target)
            self.status = 0
        except: 
            self.error.append("Unable to get IP")
            self.status = 1