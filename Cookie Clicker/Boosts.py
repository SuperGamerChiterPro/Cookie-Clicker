from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import*
from main import*
import database
from save import read_from_file, write_in_file

def boosts():
    window = QDialog()
    window.resize(500, 500)


    boost_btn = QPushButton("Boost")
    boost_logo = QLabel("Cookie")
    boost_img = QPixmap("boost.png")
    cookiepnglvl2 = boost_img.scaledToWidth(200)
    boost_logo.setPixmap(boost_img)
    boost_lbl = QLabel("+1000 Energy⚡🔋")

    main_line = QVBoxLayout()
    main_line.addWidget(boost_btn)
    main_line.addWidget(boost_lbl)
    main_line.addWidget(boost_logo)

    def boost():
        info = read_from_file()
        if time.time() - info["Rewards"] > 10:
            database.energy += 1000
            boost_btn.setDisabled(True)
            info["Rewards"] = time.time()
            write_in_file(info)




    boost_btn.clicked.connect(boost)
    window.setLayout(main_line)
    window.exec()
