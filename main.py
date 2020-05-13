from os import path
from requests import get, post
from requests.auth import HTTPBasicAuth
from decouple import config

FILENAME = "ip_address.txt"

class DomainNameEntry:
    public_ip = None

    def set_public_address(self):
        ip = get('https://api.ipify.org')
        if ip.status_code != 200:
            return False
        self.public_ip = ip.text
        return True

    def check_if_file_exists(self):
        if not path.exists(FILENAME):
            outF = open(FILENAME, "w")
            outF.write(self.public_ip)
            outF.close()
            return True
        with open(FILENAME, 'r') as file:
            data = file.read().replace('\n', '')
        if data != self.public_ip:
            return True
        return False

    def update_dynamic_dns(self):
        url = f"https://domains.google.com/nic/update?hostname=farm-server.brandongoding.com&myip={self.public_ip}"
        update = post(url, auth=HTTPBasicAuth(config('DNS_USERNAME'), config('DNS_PASSWORD')))
        print("UPDATING SHIT")
        print(update.status_code)
        print(update.text)


if __name__ == "__main__":
    dns = DomainNameEntry()
    if dns.set_public_address():
        if dns.check_if_file_exists():
            dns.update_dynamic_dns()