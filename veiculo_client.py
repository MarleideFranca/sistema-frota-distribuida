import grpc
import frota_pb2
import frota_pb2_grpc
import time
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

def gerar_localizacoes(veiculo_id):
    velocidades = [60, 85, 110, 90, 70]  # Simulação de velocidades
    for i, vel in enumerate(velocidades):
        yield frota_pb2.Localizacao(
            veiculo_id=veiculo_id,
            latitude=-23.55 + i*0.001,
            longitude=-46.63 + i*0.001,
            timestamp=str(time.time()),
            velocidade=vel
        )
        time.sleep(1)

def exibir_comando(comando):
    if comando.prioridade >= 5:
        cor = Fore.RED
    elif comando.prioridade >= 3:
        cor = Fore.YELLOW
    else:
        cor = Fore.GREEN

    print(
        f"{cor}[{comando.tipo}] (Prioridade {comando.prioridade}) "
        f"{comando.mensagem}{Style.RESET_ALL}"
    )

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = frota_pb2_grpc.FrotaServiceStub(channel)

    print(f"{Fore.CYAN}Enviando localizações do veículo em tempo real...{Style.RESET_ALL}")
    respostas = stub.Comunicar(gerar_localizacoes("VEICULO123"))

    for resposta in respostas:
        exibir_comando(resposta)

if __name__ == "__main__":
    run()
