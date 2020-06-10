import socket 

class MainClass:

    def __init__(self, target):
        self.target = target
        self.name = "dns_reverseloop"
        self.out = []
        self.error = None
        self.status = -1
        self.accept = ["i4"]

    def main(self):
        try: 
            names = socket.gethostbyaddr(self.target) 
            self.out = self.recurse(names)
            for name in self.out:
                print(self.target + "\t" + name)
            self.status = 0
        except: 
            self.error = "Unable to get Hostname and IP"
            self.status = 1 
        
    def recurse(self, names):
        out = []
        for name in names:
            if type(name) == str:
                out.append(name)
            else:
                for name2 in self.recurse(name):
                    out.append(name2)
        return out