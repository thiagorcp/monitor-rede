import json
import platform
import subprocess

def json_for_dict():
    with open('ips_test.json', 'r') as json_file:
        ips_test = json.load(json_file)
    return ips_test

def envia_ping():
    ips_test = json_for_dict()

    if platform.system().lower() == 'windows':
        cmd = "ping " + "-n" + " 1 "
        for host, ip in ips_test.items():
            output_subprocess = subprocess.run(args=(cmd + ip), capture_output=True, text=True, timeout=2)

        return output_subprocess.returncode









#def retorna_status_ping():
#    hosts = hosts_rede()
#    lists_status_hosts = dict()

    #for name_host, value_ip in hosts.items():
    #    cmd = ["ping", "-n", "1", value_ip]
    #    try:
    #        resp_status_ping = subprocess.run(cmd, capture_output=True, text=True, timeout=2)
    #        if resp_status_ping.returncode == 0:
    #            lists_status_hosts[name_host] = True
    #    except subprocess.TimeoutExpired:
    #        lists_status_hosts[name_host] = False
    #        pass

    #return lists_status_hosts

envia_ping()