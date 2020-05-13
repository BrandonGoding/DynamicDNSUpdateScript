from requests import get


class DomainNameEntry:
    public_ip = None

    def set_public_address(self):
        ip = get('https://api.ipify.org')
        if ip.status_code != 200:
            return False
        self.public_ip = ip.text
        return True

    def update_dynamic_dns(self):
        return False


if __name__ == "__main__":
    dns = DomainNameEntry()
    if dns.set_public_address():
        print(dns.public_ip)
