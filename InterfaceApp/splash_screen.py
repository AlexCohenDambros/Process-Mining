from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet("QFrame{\n"
"    border-radius: 135px;\n"
"    background-color: rgb(44, 49, 60);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.container.setObjectName("container")
        self.layoutWidget = QWidget(self.container)
        self.layoutWidget.setGeometry(QRect(-20, 10, 308, 227))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelPercentage = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(68)
        self.labelPercentage.setFont(font)
        self.labelPercentage.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(Qt.AlignCenter)
        self.labelPercentage.setObjectName("labelPercentage")
        self.gridLayout.addWidget(self.labelPercentage, 7, 0, 1, 1)
        self.labelTitle = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("background-color: none;\n"
"color: #FFFFFF")
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)
        self.labelCredits = QLabel(self.layoutWidget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet("background-color: none;\n"
"color: rgb(155, 155, 255);")
        self.labelCredits.setText("")
        self.labelCredits.setAlignment(Qt.AlignCenter)
        self.labelCredits.setObjectName("labelCredits")
        self.gridLayout.addWidget(self.labelCredits, 10, 0, 1, 1)
        self.labelLoadingInfo = QLabel(self.layoutWidget)
        self.labelLoadingInfo.setMinimumSize(QSize(0, 20))
        self.labelLoadingInfo.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelLoadingInfo.setFont(font)
        self.labelLoadingInfo.setStyleSheet("QLabel{\n"
"    border-radius: 10px;    \n"
"    background-color: rgb(93, 93, 154);\n"
"    color: #FFFFFF;\n"
"    margin-left: 40px;\n"
"    margin-right: 40px;\n"
"}")
        self.labelLoadingInfo.setFrameShape(QFrame.NoFrame)
        self.labelLoadingInfo.setAlignment(Qt.AlignCenter)
        self.labelLoadingInfo.setObjectName("labelLoadingInfo")
        self.gridLayout.addWidget(self.labelLoadingInfo, 8, 0, 1, 1)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.labelPercentage.setText(_translate("SplashScreen", "<p><span style=\" font-size:68pt;\">0</span><span style=\" font-size:58pt; vertical-align:super;\">%</span></p>"))
        self.labelTitle.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-weight:600; color:#9b9bff;\">Process</span> Mining</p></body></html>"))
        self.labelLoadingInfo.setText(_translate("SplashScreen", "loading..."))
