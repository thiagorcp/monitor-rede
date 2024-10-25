import subprocess

link = "https://www.youtube.com/watch?v=R26iojTwUv8"
def envia_pings():
    host_test = "10.0.162.253"

    hosts = {
        "Datacom-Nucleo-Parque": "10.0.162.253",
        "HPE 1920 - SETIC PZB": "10.0.162.252",
        "Huawei S5720 - Veterinaria": "10.0.154.253",
        "Huawei S5720 - SEOFI 1 ":"10.0.152.253",
        "Huawei S5720 - SEOFI 2":"10.0.152.252",
        "Huawei S5720 - SEEDU": "10.0.146.253",
        "HP 1910 - Contratos": "10.0.156.253",
        "HP 1910 - Contratos": "10.0.156.253",
        "Intelbras SG 5204 - Eduardo Galvao": "10.0.150.253",
        "HP 1910 - SEPZO": "10.0.160.253",
        "HPE 1920 - SECOS": "10.0.142.253",
        "PC DUDU": "10.0.40.169",

    }


    while True:
        for chave, valor in hosts.items():
            comando_ping = "ping -n 1 -w 3 " + valor
            resposta_do_host = subprocess.run(comando_ping, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if not resposta_do_host.returncode:
                print(chave, ": ", valor, " tá vivo!")
            else:
                print(chave, ": ", valor, " tá morto!")
        break

    return None

envia_pings()