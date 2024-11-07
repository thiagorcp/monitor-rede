import ips
import subprocess
import platform
from fastapi import FastAPI

api_test = FastAPI()
hosts = ips.hosts_rede()

def envia_pings(host):
    status_host = False
    for name_host, value_ip in hosts.items():
        send_ping = ["ping", "-c", "1", value_ip] if platform.system() == "Windows" else ["ping", "-n", "1", value_ip]

        resp_status_ping = subprocess.run(send_ping, capture_output=True, text=True, timeout=2)
        if resp_status_ping.returncode:
            status_host = True
            print(f"{name_host}: {status_host}")
        else:
            #print(f"{name_host}: {status_host}")
            print(f"{name_host} não respondeu: (Tempo limite excedido!).")

    return None



@api_test.get("/status-host")
def get_status_hosts():
    status_ping = envia_pings()
    return status_ping


if __name__ == "__main__":

    print(envia_pings(hosts))