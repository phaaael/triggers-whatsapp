import requests
import json
import re

url = "https://gateway.apibrasil.io/api/v2/whatsapp/getAllContacts"

headers = {
    "Content-Type": "application/json",
    "DeviceToken": "APIBBRASIL",
    "Authorization": "Bearer CODE_APIBRASIL"
}

try:
    response = requests.get(url, headers=headers)
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        with open("contatos_extraidos.txt", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("✅ Conteúdo salvo em contatos_extraidos.txt")
    else:
        print("⚠️ Erro na requisição ou status diferente de 200")

except Exception as e:
    print(f"❌ Erro ao fazer requisição: {e}")