import grpc
from concurrent import futures
import time
from colorama import Fore, Style, init
import frota_pb2
import frota_pb2_grpc

# Inicializa o colorama para colorir o terminal
init(autoreset=True)

class FrotaServiceServicer(frota_pb2_grpc.FrotaServiceServicer):

    def Comunicar(self, request_iterator, context):
        for localizacao in request_iterator:
            print(
                f"{Fore.CYAN}Veículo {localizacao.veiculo_id}: "
                f"({localizacao.latitude:.5f}, {localizacao.longitude:.5f}) | "
                f"Velocidade: {localizacao.velocidade} km/h{Style.RESET_ALL}"
            )

            # Lógica de exemplo de resposta conforme a velocidade
            if localizacao.velocidade > 100:
                yield frota_pb2.Comando(
                    veiculo_id=localizacao.veiculo_id,
                    tipo="ALERTA",
                    mensagem="Velocidade excessiva! Reduza imediatamente.",
                    prioridade=5
                )
            elif localizacao.velocidade > 80:
                yield frota_pb2.Comando(
                    veiculo_id=localizacao.veiculo_id,
                    tipo="AVISO",
                    mensagem="Mantenha a velocidade segura.",
                    prioridade=3
                )
            else:
                yield frota_pb2.Comando(
                    veiculo_id=localizacao.veiculo_id,
                    tipo="OK",
                    mensagem="Velocidade dentro do limite.",
                    prioridade=1
                )

    def EstimarEntrega(self, request, context):
        tempo = "15 minutos"
        condicoes = "Trânsito leve"
        status = "Em rota"
        return frota_pb2.EntregaResponse(
            tempo_estimado=tempo,
            condicoes=condicoes,
            status=status
        )

    def ConsultarVeiculo(self, request, context):
        return frota_pb2.Localizacao(
            veiculo_id=request.veiculo_id,
            latitude=-23.55,
            longitude=-46.63,
            timestamp=str(time.time()),
            velocidade=60
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    frota_pb2_grpc.add_FrotaServiceServicer_to_server(FrotaServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print(f"{Fore.GREEN}Servidor gRPC rodando na porta 50051...{Style.RESET_ALL}")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print(f"{Fore.YELLOW}\nServidor encerrado.{Style.RESET_ALL}")
        server.stop(0)

if __name__ == '__main__':
    serve()
