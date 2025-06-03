from urllib.parse import urlparse
import re

def analyze_url(url):
    """
    Возвращает (оценку, список_причин).
    """
    score = 0
    reasons = []

    parsed = urlparse(url)

    if not parsed.scheme or not parsed.netloc:
        score += 0.5
        reasons.append("Отсутствует схема или домен")

    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    if re.match(ip_pattern, parsed.netloc):
        score += 0.4
        reasons.append("Домен — IP-адрес")

    if len(url) > 75:
        score += 0.2
        reasons.append("Длинный URL")

    suspicious_chars = ['@', '-', '_', '%', '$', '!', '*', ' ']
    for ch in suspicious_chars:
        if ch in url:
            score += 0.05
            reasons.append(f"Подозрительный символ: '{ch}'")

    score = min(score, 1.0)
    return score, reasons
