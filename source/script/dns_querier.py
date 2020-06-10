
import dns.resolver
import sys

class MainClass:

    def __init__(self, target):
        self.target = target
        self.name = "dns_queries"
        self.out = []
        self.warnings = []
        self.error = []
        self.status = -1
        self.accept = ["dn"]
        self.types = ["A", "AAAA", "CNAME", "MX", "NS", "TXT"]

    def main(self):
        for rtype in self.types:
            try:
                result = dns.resolver.query(self.target, rtype)
                for res in result:
                    s = " "*(10-len(rtype))
                    self.out.append(rtype + s + self.target + "\t\t" + str(res))
            except:
                error = sys.exc_info()[0]
                if error == dns.resolver.NoAnswer:
                    self.warnings.append('No Answer from ' + rtype)
                else:
                    self.error.append(error)
        if self.error:
            self.status = 1
        else:
            self.status = 0