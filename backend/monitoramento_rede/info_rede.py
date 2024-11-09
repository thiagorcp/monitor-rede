import subprocess
from ips import hosts_rede


def retorna_status_ping():
    hosts = hosts_rede()
    lists_status_hosts = dict()

    for name_host, value_ip in hosts.items():
        cmd = ["ping", "-n", "1", value_ip]
        try:
            resp_status_ping = subprocess.run(cmd, capture_output=True, text=True, timeout=2)
            if resp_status_ping.returncode == 0:
                lists_status_hosts[name_host] = True
        except subprocess.TimeoutExpired:
            lists_status_hosts[name_host] = False
            pass

    return lists_status_hosts