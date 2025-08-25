# 📩 WhatsApp Broadcaster com API Brasil

Este projeto é um **script em Python** que automatiza o envio de mensagens no WhatsApp utilizando a **[API Brasil](https://apibrasil.com.br/)**.  
Ele foi desenvolvido para facilitar disparos em massa de forma mais **segura** e com **redução do risco de bloqueio**, aplicando intervalos e pausas aleatórias entre os envios.

---

## 🚀 Como funciona
1. Gere seus tokens de acesso na API Brasil:
   - **DeviceToken**
   - **Authorization (Bearer Token)**
2. Configure a lista de mensagens dentro da variável `mensagens` no código.
3. Adicione os números de destino em **`lista_de_contatos.txt`** (um por linha).
4. Execute o script:

```bash
python send_message.py
```

---

## ⚙️ Recursos principais
- 📑 **Lista de contatos** → leitura automática do arquivo `lista_de_contatos.txt`.  
- 🛑 **Blacklist automática** → contatos que retornarem erro (400, 403, 429, 500) são registrados em `blacklist.txt` e ignorados nos próximos envios.  
- 🔄 **Rotatividade de contatos** → após o envio, o número é movido para o final da lista, evitando repetições desnecessárias.  
- ⏳ **Intervalos randômicos** → cada disparo aguarda entre **90 e 150 segundos** antes do próximo.  
- 💤 **Pausas programadas** → a cada 10–15 envios, o script pausa por **15 a 20 minutos**.  
- ✅ **Logs em tempo real** → feedback no terminal indicando status de cada envio.  

---

## 📂 Estrutura dos arquivos
- `send_message.py` → script principal.  
- `lista_de_contatos.txt` → contatos que receberão mensagens.  
- `blacklist.txt` → contatos bloqueados automaticamente após erros.  

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

O desenvolvedor **não se responsabiliza** pelo uso inadequado do script.

---

## 🛠️ Tecnologias utilizadas
- [Python 3](https://www.python.org/)  
- [Requests](https://pypi.org/project/requests/)  

---

## 📜 Licença
Este projeto está sob a licença **MIT** – sinta-se livre para usar, modificar e distribuir.

---
