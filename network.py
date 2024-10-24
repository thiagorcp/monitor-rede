import subprocess

def envia_pings(host):
    """
    Envia um ping para o host

    -n: Indica a quantidade de pacotes a serem enviados.
    -w: Indica o tempo de espera para resposta em milisegundos.
    
    """

    comando_ping = "ping -n 1 -w 2 " + host

    resposta_do_host = subprocess.run(comando_ping, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    

    if resposta_do_host.returncode == 0:
        print(f"{host}: Está ativo!")
    else:
        print(f"{host}: Não respondeu!")
    


if __name__ == "__main__":
    # Base IP, exemplo.
    hosts = ("10.0.40.169", "127.0.0.1", "10.0.40.170")
    envia_pings(hosts[2])
