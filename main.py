# main.py

from urllib.parse import urlparse
from url_analyzer import analyze_url
from ssl_checker import check_ssl_certificate
from whois_checker import check_whois
from reputation_checker import check_virustotal
from screenshotter import get_screenshot
from comparator import compare_screenshots
import os
from colorama import init, Fore, Style

init(autoreset=True)

def normalize_url(url):
    if not url.startswith("http"):
        url = "https://" + url
    return url

def main():
    url_input = input("Введите URL для проверки: ").strip()
    url = normalize_url(url_input)
    print(f"Проверяем URL: {Fore.CYAN}{url}{Style.RESET_ALL}")

    # Анализ URL
    url_score, url_reasons = analyze_url(url)
    # Цвет оценки URL
    if url_score < 0.3:
        url_color = Fore.GREEN
    elif url_score < 0.7:
        url_color = Fore.YELLOW
    else:
        url_color = Fore.RED
    print(f"Оценка URL (0-1): {url_color}{url_score:.2f}{Style.RESET_ALL}")

    if url_reasons:
        print(f"{Fore.YELLOW}Причины подозрений:{Style.RESET_ALL}")
        for reason in url_reasons:
            print(f" - {Fore.YELLOW}{reason}{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}Причин для подозрений не найдено.{Style.RESET_ALL}")

    # Проверка SSL сертификата
    ssl_valid, ssl_info = check_ssl_certificate(url)
    if ssl_valid:
        print(f"[SSL] {Fore.GREEN}Сертификат действителен до {ssl_info}{Style.RESET_ALL}")
    else:
        print(f"[SSL] {Fore.RED}Ошибка проверки сертификата: {ssl_info}{Style.RESET_ALL}")

    # Проверка WHOIS
    whois_status, whois_info = check_whois(url)
    if whois_status:
        print(f"[WHOIS] {Fore.GREEN}Домен выглядит нормально.{Style.RESET_ALL}")
    else:
        print(f"[WHOIS] {Fore.RED}Подозрение: {whois_info}{Style.RESET_ALL}")

    # Проверка репутации через VirusTotal
    vt_status, vt_score, vt_info = check_virustotal(url)
    if vt_status:
        vt_color = Fore.GREEN if vt_score > 50 else Fore.YELLOW if vt_score > 10 else Fore.RED
        print(f"[VT] Репутация домена: {vt_color}{vt_score}{Style.RESET_ALL}")
    else:
        print(f"[VT] {Fore.RED}Ошибка проверки репутации: {vt_info}{Style.RESET_ALL}")

    # Скриншот подозрительного сайта
    suspicious_dir = "suspicious"
    os.makedirs(suspicious_dir, exist_ok=True)
    suspicious_path = os.path.join(suspicious_dir, urlparse(url).netloc + ".png")
    if get_screenshot(url, suspicious_path):
        print(f"[+] Скриншот сохранён: {Fore.CYAN}{suspicious_path}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[!] Ошибка при создании скриншота.{Style.RESET_ALL}")

    # Проверяем наличие эталонного скриншота
    trusted_dir = "trusted_sites"
    trusted_path = os.path.join(trusted_dir, urlparse(url).netloc + ".png")

    if os.path.exists(trusted_path):
        score = compare_screenshots(trusted_path, suspicious_path)
        print(f"[=] Оценка сходства скриншотов: {Fore.CYAN}{score:.2f}{Style.RESET_ALL}")
        if score > 0.9:
            print(f"{Fore.GREEN}Сайт похож на оригинал{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Сайт вызывает подозрения{Style.RESET_ALL}")
    else:
        print(f"{Fore.BLUE}[ℹ️] Эталонный скриншот не найден.{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[ℹ️] Для более точной проверки добавьте эталонный скриншот в trusted_sites/{Style.RESET_ALL}")

    # Итоговое заключение
    suspicious_flags = [
        url_score > 0.5,
        not ssl_valid,
        not whois_status,
        vt_score < 0 if vt_status else True,
        not os.path.exists(trusted_path) or (os.path.exists(trusted_path) and score <= 0.9)
    ]

    if any(suspicious_flags):
        print(f"{Fore.RED}[⚠️] Сайт вызывает подозрения!{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}[✔️] Сайт не вызывает подозрений.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
