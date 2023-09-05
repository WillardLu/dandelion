#!/usr/bin/env python
import sys
from pathlib import Path
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PIL import Image
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
try:
    from predict import *
except predict:
    raise


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("数字识别")

        self.setFixedSize(QSize(300, 300))

        self.layout = QVBoxLayout()

        self.select_pic = QPushButton("选择图像文件")
        self.select_pic.clicked.connect(self.get_filename)
        self.layout.addWidget(self.select_pic)

        self.pic1 = QLabel("图片")
        self.layout.addWidget(self.pic1)

        self.recognition_result = QLabel("识别结果：")
        self.layout.addWidget(self.recognition_result)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def get_filename(self):
        filename, _ = QFileDialog.getOpenFileName(self)
        if len(filename) == 0:
            return

        self.pic1.setPixmap(QPixmap(filename))

        img = Image.open(filename)
        img1 = img.convert("L")
        new_size = (28, 28)
        img1 = img1.resize(new_size)
        im = np.array(img1)
        im = im.reshape(28*28)
        dataset = im.astype(np.float32)
        dataset /= 255.0

        y = predict(network, dataset)
        print("Result: ", y)
        self.recognition_result.setText("识别结果：" + str(y))


network = init_network()  # 读入权重参数

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
