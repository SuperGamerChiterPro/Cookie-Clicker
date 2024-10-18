from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer
import time

import Boosts
import Rewards
import Upgrades
import database
from save import read_from_file, write_in_file


def start_game():
    global CookieCoins
    CookieCoins = 0

    window = QDialog()
    window.resize(200, 200)
    window.setWindowTitle("Cookie Clicker")
    info = read_from_file()


    upgrades_btn = QPushButton("Shop")
    rewards_btn = QPushButton("Rewards")
    boost_btn = QPushButton("Boosts")
    cookie_png_lbl = QPushButton()
    cookiepng = QIcon(QPixmap(info["cookie.png"]))
    cookie_png_lbl.setIcon(cookiepng)
    cookie_png_lbl.setIconSize(QSize(500,500))
    cookie_coins = QLabel("CookieCoins🪙 = " + str(info["CookieCoins"]))

    def addEnergy():
        database.energy += 1
        energy_lbl.setText(("Energy⚡️ = " + str(database.energy)))
        print(database.energy)

    energy_lbl = QLabel("Energy⚡️ = " + str(database.energy))

    main_game = QVBoxLayout()

    up = QHBoxLayout()
    up.addWidget(rewards_btn)
    up.addWidget(upgrades_btn)
    up.addWidget(boost_btn)

    main_game.addLayout(up)
    main_game.addWidget(cookie_png_lbl)
    main_game.addWidget(cookie_coins)
    main_game.addWidget(energy_lbl)


    timer = QTimer()
    timer.setInterval(1000)  # Інтервал в мілісекундах (1000 мс = 1 секунда)
    timer.timeout.connect(addEnergy)  # Підключаємо сигнал до функції

    timer.start()

    def addCoins():
        database.energy -= 1
        info = read_from_file()

        if database.energy > 0:
            info['CookieCoins'] += info["tap_power"]
        write_in_file(info)
        cookie_coins.setText("CookieCoins = " + str(info["CookieCoins"]))

    def shop():
        Upgrades.shop()

    def boosts():
        Boosts.boosts()

    def rewards():
        Rewards.rewards()
        




    cookie_png_lbl.clicked.connect(addCoins)
    upgrades_btn.clicked.connect(shop)
    boost_btn.clicked.connect(boosts)
    rewards_btn.clicked.connect(rewards)


    window.setLayout(main_game)
    window.exec()
