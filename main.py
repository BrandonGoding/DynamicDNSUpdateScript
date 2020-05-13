from requests import get
from os import path

class DomainNameEntry:
    public_ip = None

    def set_public_address(self):
        ip = get('https://api.ipify.org')
        if ip.status_code != 200:
            return False
        self.public_ip = ip.text
        return True

    def check_if_file_exists(self):
        if not path.exists("ip_address.txt"):
            outF = open("ip_address.txt", "w")
            outF.write(self.public_ip)
            outF.close()
            return True
        with open('ip_address.txt', 'r') as file:
            data = file.read().replace('\n', '')
        if data != self.public_ip:
            return True
        return False

    def update_dynamic_dns(self):
        print("UPDATING SHIT")


if __name__ == "__main__":
    dns = DomainNameEntry()
    if dns.set_public_address():
        if dns.check_if_file_exists():
            dns.update_dynamic_dns()