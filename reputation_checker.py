import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env

VT_API_KEY = os.getenv("VT_API_KEY")

def check_virustotal(url):
    try:
        domain = url.split("//")[-1].split("/")[0]
        headers = {"x-apikey": VT_API_KEY}
        response = requests.get(f"https://www.virustotal.com/api/v3/domains/{domain}", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            reputation = data.get("data", {}).get("attributes", {}).get("reputation", 0)
            return True, reputation, "OK"
        else:
            return False, 0, f"Ошибка API VirusTotal: {response.status_code}"
    except Exception as e:
        return False, 0, f"Ошибка запроса к VirusTotal: {e}"
с