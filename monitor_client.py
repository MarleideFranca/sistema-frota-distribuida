import grpc
import frota_pb2
import frota_pb2_grpc
from colorama import Fore, Style, init

# Inicializa colorama para colorir o terminal
init(autoreset=True)

def run():
    # Conexão com o servidor gRPC
    channel = grpc.insecure_channel('localhost:50051')
    stub = frota_pb2_grpc.FrotaServiceStub(channel)

    # Solicita a localização atual de um veículo específico
    veiculo_id = "VEICULO123"
    print(f"{Fore.CYAN}Consultando localização do veículo {veiculo_id}...{Style.RESET_ALL}")

    resposta = stub.ConsultarVeiculo(frota_pb2.VeiculoRequest(veiculo_id=veiculo_id))

    # Exibe a resposta formatada
    print(
        f"{Fore.GREEN}Localização atual de {resposta.veiculo_id}:{Style.RESET_ALL}\n"
        f"  Latitude: {resposta.latitude:.5f}\n"
        f"  Longitude: {resposta.longitude:.5f}\n"
        f"  Velocidade: {resposta.velocidade} km/h\n"
        f"  Timestamp: {resposta.timestamp}\n"
    )

if __name__ == '__main__':
    run()
