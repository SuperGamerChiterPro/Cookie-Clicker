from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer
import time
from save import read_from_file, write_in_file

def shop():
    window = QDialog()
    window.resize(500, 500)
    info = read_from_file()
    upgrade_cookie_btn = QPushButton("Upgrade Cookie")
    social_credit = QLabel("Cookie")
    cookiepng_lvl2 = QPixmap(info["Social Credit"])
    cookiepng_lvl2 = cookiepng_lvl2.scaledToWidth(300)
    social_credit.setPixmap(cookiepng_lvl2)
    text_lbl = QLabel("Your next cookie(+2 cookie coins every click) 1000 CookieCoins Requied:")
    buy_btn = QPushButton("Buy")

    main_line = QVBoxLayout()
    main_line.addWidget(upgrade_cookie_btn)
    main_line.addWidget(text_lbl)
    main_line.addWidget(social_credit)
    window.setLayout(main_line)

    def upgrade():
        info = read_from_file()
        if info["CookieCoins"] >= 1000:
            info["cookie.png"] = "level 2.png"
            info["tap_power"] = 2
            info["level 1"] = 2
            write_in_file(info)

        if info["CookieCoins"] >= 2000 and info["level 1"] == 2:
            info["cookie.png"] = "level 3.png"
            info["tap_power"] = 3
            info["level 1"] = 3
            info["Social Credit"] = "level 2 social credit.png"
            write_in_file(info)

        if info["level 1"] == 3:
            info["Social Credit"] = "level 3 social credit.png"
            write_in_file(info)





    upgrade_cookie_btn.clicked.connect(upgrade)

    window.exec()
