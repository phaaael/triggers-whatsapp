# 📩 Automação de WhatsApp com API Brasil

Este projeto é um conjunto de **scripts em Python** para automatizar tarefas no WhatsApp utilizando a **[API Brasil](https://apibrasil.com.br/)**.  
Ele inclui ferramentas para **extrair contatos** e **enviar mensagens automáticas** com segurança e menor risco de bloqueio.

---

## 🚀 Scripts incluídos

### 1️⃣ send_message.py
Automatiza o envio de mensagens no WhatsApp a partir de uma lista de contatos.

#### Recursos
- 📑 **Lista de contatos** → leitura de `lista_de_contatos.txt`.  
- 🛑 **Blacklist automática** → erros comuns adicionam o contato em `blacklist.txt`.  
- 🔄 **Rotatividade de contatos** → após o envio, o número vai para o final da fila.  
- ⏳ **Intervalos randômicos** → entre 90 e 150 segundos por disparo.  
- 💤 **Pausas programadas** → a cada 10–15 envios, pausa de 15 a 20 minutos.  
- ✅ **Logs em tempo real** → feedback no terminal.  

---

### 2️⃣ get_contacts.py
Extrai todos os contatos cadastrados no aparelho conectado na API Brasil e salva em um arquivo local.

#### Como funciona
1. Faz uma requisição GET para `https://gateway.apibrasil.io/api/v2/whatsapp/getAllContacts`.  
2. Salva a resposta em formato JSON no arquivo **`contatos_extraidos.txt`**.  
3. Exibe no terminal o status da requisição.  

#### Saída esperada
- ✅ Arquivo `contatos_extraidos.txt` contendo os contatos extraídos.  
- ⚠️ Caso a API retorne erro, o status e a mensagem são exibidos no terminal.  

---

## 📂 Estrutura dos arquivos
- `send_message.py` → envio de mensagens automatizado.  
- `get_contacts.py` → extração de contatos via API.  
- `lista_de_contatos.txt` → contatos que receberão mensagens.  
- `blacklist.txt` → contatos bloqueados automaticamente após erros.  
- `contatos_extraidos.txt` → contatos exportados pela API.  

---

## 📋 Exemplo de `lista_de_contatos.txt`
```
5521999999999
5521988888888
5521977777777
```

---

## ⚠️ Aviso importante
Este projeto deve ser utilizado **apenas para fins legais** e respeitando:
- ✅ Políticas de uso do WhatsApp.  
- ✅ Leis de privacidade e proteção de dados.  

O desenvolvedor **não se responsabiliza** pelo uso inadequado dos scripts.

---

## 🛠️ Tecnologias utilizadas
- [Python 3](https://www.python.org/)  
- [Requests](https://pypi.org/project/requests/)  

---

## 📜 Licença
Este projeto está sob a licença **MIT** – sinta-se livre para usar, modificar e distribuir.

---
