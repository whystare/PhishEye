import ssl
import whois
import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

VT_API_KEY = os.getenv("VT_API_KEY")

def analyze_url(url: str) -> float:
    # Твоя функция оценки URL
    return 0.1  # заглушка

def check_ssl_certificate(url: str):
    try:
        # Проверяем SSL сертификат (пример для https)
        hostname = url.replace("https://", "").replace("http://", "").split("/")[0]
        context = ssl.create_default_context()
        with context.wrap_socket(
            socket.socket(), server_hostname=hostname,
        ) as s:
            s.settimeout(5.0)
            s.connect((hostname, 443))
            cert = s.getpeercert()
            expiry = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            return True, expiry
    except Exception as e:
        return False, str(e)

def check_whois(domain: str):
    try:
        w = whois.whois(domain)
        return True, w.creation_date
    except Exception as e:
        return False, str(e)

def check_virustotal(domain: str):
    try:
        url = f"https://www.virustotal.com/api/v3/domains/{domain}"
        headers = {"x-apikey": VT_API_KEY}
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            reputation = data.get("data", {}).get("attributes", {}).get("reputation", 0)
            return True, reputation
        return False, f"HTTP {r.status_code}"
    except Exception as e:
        return False, str(e)
