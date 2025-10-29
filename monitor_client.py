import grpc
import frota_pb2
import frota_pb2_grpc
from colorama import Fore, Style, init
import time

# Inicializa o colorama para colorir o terminal
init(autoreset=True)

def consultar_veiculo(stub, veiculo_id):
    print(f"{Fore.CYAN}Consultando localização do {veiculo_id}...{Style.RESET_ALL}")
    resposta = stub.ConsultarVeiculo(frota_pb2.VeiculoRequest(veiculo_id=veiculo_id))
    print(
        f"{Fore.GREEN}Veículo {resposta.veiculo_id}:\n"
        f"  Latitude: {resposta.latitude}\n"
        f"  Longitude: {resposta.longitude}\n"
        f"  Velocidade: {resposta.velocidade} km/h\n"
        f"  Timestamp: {resposta.timestamp}{Style.RESET_ALL}"
    )

def estimar_entrega(stub, veiculo_id):
    print(f"{Fore.CYAN}Solicitando estimativa de entrega do {veiculo_id}...{Style.RESET_ALL}")
    resposta = stub.EstimarEntrega(frota_pb2.EntregaRequest(veiculo_id=veiculo_id))
    print(
        f"{Fore.YELLOW}Estimativa de entrega:\n"
        f"  Tempo: {resposta.tempo_estimado}\n"
        f"  Condições: {resposta.condicoes}\n"
        f"  Status: {resposta.status}{Style.RESET_ALL}"
    )

def menu():
    print(f"\n{Fore.MAGENTA}=== MONITOR DE FROTA ==={Style.RESET_ALL}")
    print("1 - Consultar veículo")
    print("2 - Estimar entrega")
    print("0 - Sair")

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = frota_pb2_grpc.FrotaServiceStub(channel)

    while True:
        menu()
        opcao = input(f"{Fore.CYAN}Escolha uma opção: {Style.RESET_ALL}")

        if opcao == "1":
            veiculo_id = input("Informe o ID do veículo: ").strip()
            consultar_veiculo(stub, veiculo_id)
        elif opcao == "2":
            veiculo_id = input("Informe o ID do veículo: ").strip()
            estimar_entrega(stub, veiculo_id)
        elif opcao == "0":
            print(f"{Fore.YELLOW}Encerrando monitor...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")

        time.sleep(1)

if __name__ == "__main__":
    main()
