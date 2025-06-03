# 🛡️ PhishEye

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Mac%2FLinux%20%7C%20Windows-lightgrey)
![License](https://img.shields.io/github/license/whystare/PhishEye)
![Maintained](https://img.shields.io/badge/Maintained-yes-brightgreen)
![Stars](https://img.shields.io/github/stars/whystare/PhishEye?style=social)

> Инструмент для анализа фишинговых сайтов с помощью URL-эвристик, SSL, WHOIS, VirusTotal и сравнения скриншотов.

---

## 🚀 Возможности

- 🔍 Анализирует URL на признаки фишинга
- 🔐 Проверяет SSL-сертификат сайта
- 🌍 Проверка WHOIS-домена
- 🧠 Использует API VirusTotal для репутации
- 🖼️ Делает скриншот сайта и сравнивает с эталоном
- 🎨 Цветной CLI-вывод для наглядности
---

## 🧩 Пример использования

```bash
$ python main.py
Введите URL для проверки: google.com

Проверяем URL: https://google.com
Оценка URL (0-1): 0.00
Причин для подозрений не найдено.
[SSL] Сертификат действителен до 2025-08-04 08:43:07
[WHOIS] Домен зарегистрирован
[VT] Репутация домена: 626
[+] Скриншот сохранён: suspicious/google.com.png
[ℹ️] Эталонный скриншот не найден.
[⚠️] Сайт вызывает подозрения!
```

  ##   📦 Установка
  ```bash
git clone https://github.com/<your-username>/PhishEye.git
cd PhishEye

# Создай и активируй виртуальное окружение
python3 -m venv venv
source venv/bin/activate  # для Linux/macOS
# или
venv\Scripts\activate     # для Windows

## Установи зависимости
pip install -r requirements.txt

Создай файл .env и добавь ключ API от VirusTotal:

VT_API_KEY=твой_ключ_от_virustotal
```
## 🗂 Структура проекта
```bash
PhishEye/
├── main.py                  # Главный исполняемый файл
├── url_analyzer.py          # Проверка структуры URL
├── ssl_checker.py           # Проверка SSL-сертификата
├── whois_checker.py         # Проверка WHOIS
├── reputation_checker.py    # Проверка через VirusTotal
├── screenshotter.py         # Захват скриншота
├── comparator.py            # Сравнение изображений
├── trusted_sites/           # Эталонные скриншоты
├── suspicious/              # Подозрительные скриншоты
├── .env                     # Файл переменных окружения
├── .gitignore
└── requirements.txt
```
## 📦 Зависимости

Установлены через requirements.txt, включая:
```bash
requests

python-whois

colorama

selenium

Pillow

opencv-python

python-dotenv
```
## 📸 Эталонные скриншоты
```bash
Для более точного определения фишинга можно поместить эталонные изображения в trusted_sites/, чтобы сравнивать сайты по визуальному сходству.
```
## 📝 Лицензия
```bash
Проект распространяется под лицензией MIT.
Свободен для использования и модификации с указанием авторства.
```
