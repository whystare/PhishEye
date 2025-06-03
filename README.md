# 🛡️ PhishEye — Антифишинговый сканер сайтов

PhishEye — это многоуровневый инструмент для проверки URL на фишинг.  
Он объединяет эвристический анализ, проверки безопасности и визуальное сравнение, чтобы определить, вызывает ли сайт подозрения.

---

## 🔍 Что умеет PhishEye

✅ Проверяет структуру URL  
✅ Валидирует SSL-сертификаты  
✅ Получает данные WHOIS  
✅ Запрашивает репутацию домена с VirusTotal  
✅ Делает скриншот сайта  
✅ Сравнивает его с эталонным изображением  
✅ Выводит итоговый вердикт: безопасно / подозрительно

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

📦 Установка
git clone https://github.com/<your-username>/PhishEye.git
cd PhishEye

# Создай и активируй виртуальное окружение
python3 -m venv venv
source venv/bin/activate  # для Linux/macOS
# или
venv\Scripts\activate     # для Windows

# Установи зависимости
pip install -r requirements.txt

Создай файл .env и добавь ключ API от VirusTotal:

VT_API_KEY=твой_ключ_от_virustotal

🗂 Структура проекта

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

📦 Зависимости
Установлены через requirements.txt, включая:

requests

python-whois

colorama

selenium

Pillow

opencv-python

python-dotenv

📸 Эталонные скриншоты
Для более точного определения фишинга можно поместить эталонные изображения в trusted_sites/, чтобы сравнивать сайты по визуальному сходству.

📝 Лицензия
Проект распространяется под лицензией MIT.
Свободен для использования и модификации с указанием авторства.

