

✅ Etapa 7: Testar o sistema

Gere os arquivos Python do .proto:

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. frota.proto


Execute o servidor:
python central_server.py

Em outro terminal, execute o cliente veículo:
python veiculo_client.py

Depois, execute o cliente monitor:
python monitor_client.py


