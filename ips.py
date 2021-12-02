import ipaddress


if __name__ == '__main__':
    ip = '192.168.0.10/24'
    rede = ipaddress.ip_network(ip, strict=False)
    for ip in rede:
        print(ip)
