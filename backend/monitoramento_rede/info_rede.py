import json
import platform
import subprocess


def json_for_dict():
    with open('ips_test.json', 'r') as file:
        ips_test = json.load(file)
    file.close()
    return ips_test

def retorna_dic_status_hosts():
    """
    A função recebe um dicionário contendo os nome dos hosts e seus IPs,
    lê o dicionário e envia um ping para cada IP.

    Coleta a resposta e retorna um novo dicionário contendo o nome do hosts e
    "True", caso responda o ping, caso contrário retorna "False".

    Ex:
    {
        "host": True
    }
    """
    output_subprocess = ""
    dict_hosts = json_for_dict()
    status_ip = dict()
    if platform.system().lower() == 'windows':
        # -n: quantidade de pings a serem enviados
        # -l: quantidade de bytes a serem enviados
        cmd = "ping " + "-n 1 "
        for host, ip in dict_hosts.items():
            try:
                # envia um ping para os hosts em 'dict_hosts'
                output_subprocess = subprocess.run(args=(cmd + ip), capture_output=True, shell= True, text=True, timeout=1)
                # cria um dicionário contendo 'nome' e um boleano 'True' ou 'False'
                status_ip[host] = output_subprocess.returncode
            except subprocess.TimeoutExpired:
                status_ip[host] = output_subprocess.returncode
        # retorna o nome do host e um booleano true para ativo ou false para inativo
        return status_ip


def get_status_hosts():
    hosts = retorna_dic_status_hosts()
    hosts_resp = dict()

    for k, v in hosts.items():
        if v == 0:
            hosts_resp[k] = True
        else:
            hosts_resp[k] = False

    return hosts_resp
