import os
import subprocess

def envia_pings(host):
    """
    Envia um ping para o host

    -n: Indica a quantidade de pacotes a serem enviados.
    -w: Indica o tempo de espera para resposta em milisegundos.
    nt: Indica que o sistema operacional é o Windows.
    
    """
    sistema_operacional = os.name

    if sistema_operacional == "nt":
        comando_ping = f"ping -n 1 -w 2 {host}"
    else:
        comando_ping = f"ping -c 1 {host}"
    
    #resposta = os.system(comando_ping)

    # Limpa a saída padão do comando Ping, para não exibir na tela.
    resposta_do_host = subprocess.run(comando_ping, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    

    if resposta_do_host.returncode == 0:
        print(f"{host} está ativo.")
    else:
        print(f"{host} não respondeu.")
    


if __name__ == "__main__":
    # Base IP, exemplo.
    base_ip = "192.168.100."
    
    # Varre os IPs de 1 a 10.
    for i in range(1, 10):
        ip = base_ip + str(i)
        envia_pings(ip)
