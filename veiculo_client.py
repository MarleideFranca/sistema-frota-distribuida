import grpc
import frota_pb2
import frota_pb2_grpc
import time
import threading
import random
from colorama import Fore, Style, init
from threading import Lock

# Inicializa o colorama
init(autoreset=True)

# Cria um lock para evitar que duas threads imprimam ao mesmo tempo
print_lock = Lock()

def gerar_localizacoes(veiculo_id):
    # Ponto inicial aleatório para cada veículo
    lat = -23.55 + random.uniform(-0.01, 0.01)
    lon = -46.63 + random.uniform(-0.01, 0.01)

    for _ in range(10):  # envia 10 localizações
        velocidade = random.randint(50, 120)
        lat += random.uniform(-0.001, 0.001)
        lon += random.uniform(-0.001, 0.001)

        yield frota_pb2.Localizacao(
            veiculo_id=veiculo_id,
            latitude=lat,
            longitude=lon,
            timestamp=str(time.time()),
            velocidade=velocidade
        )
        time.sleep(3)

def exibir_comando(comando):
    if comando.prioridade >= 5:
        cor = Fore.RED
    elif comando.prioridade >= 3:
        cor = Fore.YELLOW
    else:
        cor = Fore.GREEN

    # Usa o lock para imprimir de forma ordenada
    with print_lock:
        print(
            f"{cor}[{comando.veiculo_id}] [{comando.tipo}] "
            f"(Prioridade {comando.prioridade}) {comando.mensagem}{Style.RESET_ALL}\n"
        )
        time.sleep(0.05)  # pequeno delay visual

def simular_veiculo(veiculo_id):
    channel = grpc.insecure_channel('localhost:50051')
    stub = frota_pb2_grpc.FrotaServiceStub(channel)

    with print_lock:
        print(f"{Fore.CYAN}Iniciando simulação do {veiculo_id}...{Style.RESET_ALL}\n")

    respostas = stub.Comunicar(gerar_localizacoes(veiculo_id))

    for resposta in respostas:
        exibir_comando(resposta)

def main():
    threads = []
    for vid in ["VEICULO123", "VEICULO456"]:
        t = threading.Thread(target=simular_veiculo, args=(vid,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
