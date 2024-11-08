import subprocess
from ips import hosts_rede

def retorna_status_ping():
    hosts = hosts_rede()
    status_host = False
    lists_status_hosts = dict()

    for name_host, value_ip in hosts.items():
        send_ping = ["ping", "-n", "1", value_ip]

        try:
            resp_status_ping = subprocess.run(send_ping, capture_output=True, text=True, timeout=3)
            if resp_status_ping.returncode == 0:
                status_host = True
                lists_status_hosts[name_host] = status_host
        except subprocess.TimeoutExpired:
            lists_status_hosts[name_host] = status_host

    return lists_status_hosts


if __name__ == "__main__":
    pass