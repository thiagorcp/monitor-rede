import subprocess
import ips

ips = ips.host_rede()
link = "https://www.youtube.com/watch?v=R26iojTwUv8"
def envia_pings():
    host_test = "10.0.162.253"


    while True:
        for chave, valor in ips.items():
            comando_ping = "ping -n 1 -w 3 " + valor
            resposta_do_host = subprocess.run(comando_ping, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if not resposta_do_host.returncode:
                print(chave, ": ", valor, " tá vivo!")
            else:
                print(chave, ": ", valor, " tá morto!")
        break

    return None

envia_pings()