# 🚗 Sistema de Gestão de Frota com gRPC

Este projeto implementa um sistema distribuído de gestão de frota utilizando o framework open source gRPC (Google Remote Procedure Call).  
O sistema simula a comunicação entre veículos, um servidor central e um módulo de monitoramento, permitindo o acompanhamento em tempo real de localização e velocidade.

---

## 📘 Relatório Técnico

O relatório técnico completo descrevendo a arquitetura, comunicação e justificativa da escolha do gRPC está disponível em:

📄 [Relatório Técnico - Sistema de Gestão de Frota com gRPC (PDF)](documentacao/Relatorio_Tecnico_gRPC.pdf)

---

## ⚙️ Estrutura do Sistema

- **central_server.py** → Servidor gRPC responsável por receber dados e enviar comandos.  
- **veiculo_client.py** → Cliente simulador de veículos, com comunicação bidirecional.  
- **monitor_client.py** → Cliente de monitoramento para consultas pontuais.  
- **frota.proto** → Definição da interface do serviço gRPC e das mensagens (Protocol Buffers).

---

⚙️ Como executar o projeto:

1️⃣ Gerar os arquivos Python a partir do .proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. frota.proto

2️⃣ Executar o servidor

python central_server.py

3️⃣ Em outro terminal, executar o cliente veículo

python veiculo_client.py

4️⃣ Em outro terminal, executar o cliente monitor

python monitor_client.py

---

💡 Lições Aprendidas

Durante o desenvolvimento deste projeto, foi possível compreender na prática:

- A importância de colaborar em equipe, compartilhando responsabilidades e resolvendo desafios técnicos de forma conjunta.

- O valor de trabalhar em um ambiente distribuído, tanto no aspecto humano (divisão de tarefas e integração de código) quanto técnico (comunicação entre múltiplos sistemas).

- Como o gRPC facilita a comunicação eficiente e escalável em sistemas distribuídos, refletindo os mesmos princípios de colaboração e integração presentes no trabalho em grupo.

Essas experiências reforçaram não apenas o aprendizado técnico, mas também o entendimento de como a comunicação — entre pessoas e entre sistemas — é fundamental para o sucesso de um projeto.


👩‍💻 **Discente:** *Marleide Alves de França*