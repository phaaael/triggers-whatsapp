import requests
import time
import random
import os

url = "https://gateway.apibrasil.io/api/v2/whatsapp/sendText"

headers = {
    "Content-Type": "application/json",
    "DeviceToken": "APIBBRASIL",
    "Authorization": "Bearer CODE_APIBRASIL"
}
    
mensagens = [ "DIGITE SUA MENSAGEM AQUI !" ]

blacklist = set()
if os.path.exists("blacklist.txt"):
    with open("blacklist.txt", "r", encoding="utf-8") as bl:
        blacklist = set(linha.strip() for linha in bl if linha.strip())

try:
    with open("lista_de_contatos.txt", "r", encoding="utf-8") as f:
        lista_original = [linha.strip() for linha in f if linha.strip()]
except FileNotFoundError:
    print("❌ Arquivo 'lista_de_contatos.txt' não encontrado.")
    exit()

numeros = [n for n in lista_original if n not in blacklist]

contador_envios = 0
proxima_pausa = random.randint(10, 15)

for numero in numeros:
    mensagem = random.choice(mensagens)
    payload = {
        "number": numero,
        "text": mensagem
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            print(f"✅ Mensagem enviada para {numero}")

            lista_original.remove(numero)
            lista_original.append(numero)

            with open("lista_de_contatos.txt", "w", encoding="utf-8") as f:
                for num in lista_original:
                    f.write(num + "\n")

        else:
            print(f"❌ Erro ao enviar para {numero}: {response.status_code}")
            print(response.text)
            if response.status_code in [400, 403, 429, 500]:
                print(f"⛔ {numero} adicionado à blacklist")
                with open("blacklist.txt", "a", encoding="utf-8") as bl:
                    bl.write(numero + "\n")
                continue

    except Exception as e:
        print(f"⚠️ Erro ao enviar para {numero}: {e}")
        continue

    contador_envios += 1

    if contador_envios == proxima_pausa:
        minutos = random.randint(15, 20)
        print(f"⏸️ Pausando {minutos} minutos após {contador_envios} envios.")
        time.sleep(minutos * 60)
        contador_envios = 0
        proxima_pausa = random.randint(10, 15)

    espera = random.randint(90, 150)
    print(f"⏳ Esperando {espera} segundos antes do próximo envio...")
    time.sleep(espera)

print("\n🏁 Finalizado.")