from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt6.QtGui import QFont, QColor, QPalette

class PhishEyeGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PhishEye - Проверка фишинга")
        self.setFixedSize(600, 500)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Введите URL сайта для проверки:")
        self.label.setFont(QFont("Segoe UI", 14))
        self.layout.addWidget(self.label)

        self.url_input = QLineEdit()
        self.url_input.setFont(QFont("Segoe UI", 12))
        self.url_input.setPlaceholderText("https://example.com")
        self.layout.addWidget(self.url_input)

        self.check_btn = QPushButton("Проверить")
        self.check_btn.setFont(QFont("Segoe UI", 14))
        self.check_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)
        self.check_btn.clicked.connect(self.start_check)
        self.layout.addWidget(self.check_btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setFont(QFont("Consolas", 11))
        self.layout.addWidget(self.output)

        # Анимация кнопки (пример плавного изменения opacity)
        self.anim = QPropertyAnimation(self.check_btn, b"windowOpacity")
        self.anim.setDuration(300)
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.6)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.check_btn.pressed.connect(self.fade_out)
        self.check_btn.released.connect(self.fade_in)

    def fade_out(self):
        self.anim.setDirection(QPropertyAnimation.Direction.Forward)
        self.anim.start()

    def fade_in(self):
        self.anim.setDirection(QPropertyAnimation.Direction.Backward)
        self.anim.start()

    def start_check(self):
        url = self.url_input.text().strip()
        if not url:
            self.output.setPlainText("⚠️ Пожалуйста, введите URL для проверки.")
            return

        self.output.setPlainText("Проверка... Пожалуйста, подождите.\n")

        # Здесь вызываем основную функцию проверки, например main(url)
        # Для примера - имитация вывода:
        result = f"Проверяем URL: {url}\n\n"
        result += "[URL-анализ] Оценка подозрительности: 0.15\n"
        result += "✔️ URL выглядит нормально\n\n"
        result += "--- Проверка SSL ---\n"
        result += "Сертификат действителен до 2025-08-04\n\n"
        result += "--- WHOIS ---\n"
        result += "Домен зарегистрирован в 2010 году\n\n"
        result += "--- VirusTotal ---\n"
        result += "Репутация: 0\n\n"
        result += "✅ Сайт выглядит безопасным"
        
        self.output.setPlainText(result)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PhishEyeGUI()
    window.show()
    sys.exit(app.exec())
