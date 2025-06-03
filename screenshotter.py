# screenshotter.py

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import time

def get_screenshot(url, output_path="suspicious/screenshot.png"):
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)

    try:
        print(f"[+] Открываем URL: {url}")
        driver.set_window_size(1280, 1024)
        driver.get(url)
        time.sleep(3)  # ждем загрузки страницы

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        driver.save_screenshot(output_path)
        print(f"[+] Скриншот сохранён: {output_path}")
        return True
    except Exception as e:
        print(f"[!] Ошибка при создании скриншота: {e}")
        return False
    finally:
        driver.quit()
