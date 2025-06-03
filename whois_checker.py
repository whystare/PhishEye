import subprocess

def check_whois(url):
    try:
        domain = url.split("//")[-1].split("/")[0]
        result = subprocess.run(["whois", domain], capture_output=True, text=True, timeout=10)
        output = result.stdout.lower()
        if "no match" in output or "not found" in output:
            return False, "Домен не зарегистрирован"
        return True, "Домен зарегистрирован"
    except Exception as e:
        return False, f"Ошибка проверки WHOIS: {e}"
