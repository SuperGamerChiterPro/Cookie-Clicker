from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import*
from main import*
app = QApplication([])
window = QWidget()
window.resize(500, 500)

CookieCoins = 0

window.setWindowTitle("Cookie Clicker")
start_game_btn = QPushButton("Start Game")
settings_game_btn = QPushButton("Settings")
exchange_btn = QPushButton("Exchange")
cookie_text = QLabel("Text")
CookieCoins_lbl = QLabel("CookieCoins")
cookie_text_png = QPixmap("Cookie_Clicker_Logo.png")
cookie_text_png = cookie_text_png.scaledToWidth(200)
cookie_text.setPixmap(cookie_text_png)
cookie_png_lbl = QLabel("Cookie")
cookiepng = QPixmap("cookie.png")
cookiepng = cookiepng.scaledToWidth(500)
cookie_png_lbl.setPixmap(cookiepng)

menu = QVBoxLayout()
menu.addWidget(cookie_text)
menu.addWidget(cookie_png_lbl)
menu.addWidget(start_game_btn)
menu.addWidget(settings_game_btn)
menu.addWidget(exchange_btn)

start_game_btn.clicked.connect(start_game)
window.setLayout(menu)

window.show()
app.exec()