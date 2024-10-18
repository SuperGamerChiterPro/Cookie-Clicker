import time

from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import*
from PyQt6.QtWidgets import*
from save import read_from_file, write_in_file
def rewards():
    window = QDialog()
    window.resize(500, 500)

    reward_info_lbl = QLabel("Reward 10k coins💰!")
    present_logo = QLabel("Cookie")
    present_img = QPixmap("present.png")
    present_img = present_img.scaledToWidth(200)
    present_logo.setPixmap(present_img)
    day_1_lbl = QLabel("Day 1")
    reward_btn = QPushButton("Reward!")

    def getReward():
        info = read_from_file()
        if time.time() - info["Rewards"] > 10:
            info['CookieCoins'] += 1000
            info["Rewards"] = time.time()
            write_in_file(info)
            reward_btn.setDisabled(True)


    main_line = QHBoxLayout()
    main_line.addWidget(day_1_lbl)
    main_line.addWidget(present_logo)

    main_line2 = QVBoxLayout()
    main_line.addWidget(reward_info_lbl)
    main_line2.addWidget(reward_btn)


    reward_btn.clicked.connect(getReward)
    main_line.addLayout(main_line2)
    main_line.addWidget(reward_info_lbl)
    window.setLayout(main_line)
    window.exec()