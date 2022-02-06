import sys
import platform
import pandas as pd
from PyQt5.QtWidgets import (QMessageBox, QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel,
                             QVBoxLayout, QPlainTextEdit)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir
from datetime import datetime
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# Dicionarios
login = {}
dici = {}
listas = {}

pd.set_option('max_columns', None)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 720))
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
                                 "QToolTip {\n"
                                 "    color: #ffffff;\n"
                                 "    background-color: rgba(27, 29, 35, 160);\n"
                                 "    border: 1px solid rgb(100, 100, 100);\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: transparent;\n"
                                         "color: rgb(210, 210, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("")
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QtWidgets.QFrame(self.frame_main)
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_top.setStyleSheet("background-color: transparent;")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_toggle = QtWidgets.QFrame(self.frame_top)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_toggle.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_toggle_menu = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet("QPushButton {\n"
                                           "    \n"
                                           "    background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                           "    background-position: center;\n"
                                           "    background-repeat: no-reperat;\n"
                                           "    border: none;\n"
                                           "    background-color: rgb(27, 29, 35);\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(33, 37, 43);\n"
                                           "}\n"
                                           "QPushButton:pressed {    \n"
                                           "    background-color: rgb(85, 170, 255);\n"
                                           "}")
        self.btn_toggle_menu.setText("")
        self.btn_toggle_menu.setObjectName("btn_toggle_menu")
        self.verticalLayout_3.addWidget(self.btn_toggle_menu)
        self.horizontalLayout_3.addWidget(self.frame_toggle)
        self.frame_top_right = QtWidgets.QFrame(self.frame_top)
        self.frame_top_right.setStyleSheet("background: transparent;")
        self.frame_top_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_right.setObjectName("frame_top_right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top_btns = QtWidgets.QFrame(self.frame_top_right)
        self.frame_top_btns.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_top_btns.setStyleSheet("background-color: rgba(33, 37, 43, 150);")
        self.frame_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_btns.setObjectName("frame_top_btns")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setContentsMargins(8, 0, 10, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_icon_top_bar = QtWidgets.QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet("background: transparent;\n"
                                              "background-image: url(:/16x/icons/16x16/cil-terminal.png);\n"
                                              "background-position: center;\n"
                                              "background-repeat: no-repeat;")
        self.frame_icon_top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_icon_top_bar.setObjectName("frame_icon_top_bar")
        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)
        self.label_title_bar_top = QtWidgets.QLabel(self.frame_label_top_btns)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet("background: transparent;\n"
                                               "margin-left: 5px;")
        self.label_title_bar_top.setObjectName("label_title_bar_top")
        self.horizontalLayout_10.addWidget(self.label_title_bar_top)
        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QtWidgets.QFrame(self.frame_top_btns)
        self.frame_btns_right.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
                                        "    border: none;\n"
                                        "    background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(44, 49, 60)\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(85, 170, 255);\n"
                                        "}")
        self.btn_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-window-minimize.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_5.addWidget(self.btn_minimize)
        self.btn_maximize_restore = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy)
        self.btn_maximize_restore.setStyleSheet("QPushButton {    \n"
                                                "    border: none;\n"
                                                "    background-color: transparent;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: rgb(44, 49, 60)\n"
                                                "}\n"
                                                "QPushButton:pressed {    \n"
                                                "    background-color: rgb(85, 170, 255);\n"
                                                "}")
        self.btn_maximize_restore.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-window-maximize.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)
        self.btn_maximize_restore.setObjectName("btn_maximize_restore")
        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setStyleSheet("QPushButton {    \n"
                                     "    border: none;\n"
                                     "    background-color: transparent;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(44, 49, 60)\n"
                                     "}\n"
                                     "QPushButton:pressed {    \n"
                                     "    background-color: rgb(85, 170, 255);\n"
                                     "}")
        self.btn_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_5.addWidget(self.btn_close)
        self.horizontalLayout_4.addWidget(self.frame_btns_right)
        self.verticalLayout_2.addWidget(self.frame_top_btns)
        self.frame_top_info = QtWidgets.QFrame(self.frame_top_right)
        self.frame_top_info.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_top_info.setStyleSheet("background-color: rgb(27, 29, 35);t")
        self.frame_top_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_info.setObjectName("frame_top_info")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_OPEN = QtWidgets.QPushButton(self.frame_top_info)
        self.btn_OPEN.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_OPEN.setStyleSheet("QPushButton {    \n"
                                    "    background-image: url(:/16x16/icons/16x16/cil-file.png);\n"
                                    "    background-position: left center;\n"
                                    "    background-repeat: no-repeat;\n"
                                    "    border: none;\n"
                                    "    border-left: 28px solid rgb(27, 29, 35);\n"
                                    "    background-color: rgb(27, 29, 35);\n"
                                    "    text-align: left;\n"
                                    "    padding-left: 45px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(33, 37, 43);\n"
                                    "    border-left: 28px solid rgb(33, 37, 43);\n"
                                    "}\n"
                                    "QPushButton:pressed {    \n"
                                    "    background-color: rgb(85, 170, 255);\n"
                                    "    border-left: 28px solid rgb(85, 170, 255);\n"
                                    "}")
        self.btn_OPEN.setObjectName("btn_OPEN")
        self.horizontalLayout_8.addWidget(self.btn_OPEN)
        self.btn_OpenLo = QtWidgets.QPushButton(self.frame_top_info)
        self.btn_OpenLo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_OpenLo.setStyleSheet("QPushButton {    \n"
                                      "    background-image: url(:/16x16/icons/16x16/cil-find-in-page.png);\n"
                                      "    background-position: left center;\n"
                                      "    background-repeat: no-repeat;\n"
                                      "    border: none;\n"
                                      "    border-left: 28px solid rgb(27, 29, 35);\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    text-align: left;\n"
                                      "    padding-left: 45px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(33, 37, 43);\n"
                                      "    border-left: 28px solid rgb(33, 37, 43);\n"
                                      "}\n"
                                      "QPushButton:pressed {    \n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "    border-left: 28px solid rgb(85, 170, 255);\n"
                                      "}")
        self.btn_OpenLo.setObjectName("btn_OpenLo")
        self.horizontalLayout_8.addWidget(self.btn_OpenLo)
        self.btn_SAVE = QtWidgets.QPushButton(self.frame_top_info)
        self.btn_SAVE.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_SAVE.setStyleSheet("QPushButton {    \n"
                                    "    background-image: url(:/16x16/icons/16x16/cil-save.png);\n"
                                    "    background-position: left center;\n"
                                    "    background-repeat: no-repeat;\n"
                                    "    border: none;\n"
                                    "    border-left: 28px solid rgb(27, 29, 35);\n"
                                    "    background-color: rgb(27, 29, 35);\n"
                                    "    text-align: left;\n"
                                    "    padding-left: 45px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(33, 37, 43);\n"
                                    "    border-left: 28px solid rgb(33, 37, 43);\n"
                                    "}\n"
                                    "QPushButton:pressed {    \n"
                                    "    background-color: rgb(85, 170, 255);\n"
                                    "    border-left: 28px solid rgb(85, 170, 255);\n"
                                    "}")
        self.btn_SAVE.setObjectName("btn_SAVE")
        self.horizontalLayout_8.addWidget(self.btn_SAVE)
        self.btn_SAVEEXPORT = QtWidgets.QPushButton(self.frame_top_info)
        self.btn_SAVEEXPORT.setMaximumSize(QtCore.QSize(16777215, 40))
        self.btn_SAVEEXPORT.setStyleSheet("QPushButton {    \n"
                                          "    \n"
                                          "    background-image: url(:/16x16/icons/16x16/cil-external-link.png);\n"
                                          "    background-position: left center;\n"
                                          "    background-repeat: no-repeat;\n"
                                          "    border: none;\n"
                                          "    border-left: 28px solid rgb(27, 29, 35);\n"
                                          "    background-color: rgb(27, 29, 35);\n"
                                          "    text-align: left;\n"
                                          "    padding-left: 45px;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(33, 37, 43);\n"
                                          "    border-left: 28px solid rgb(33, 37, 43);\n"
                                          "}\n"
                                          "QPushButton:pressed {    \n"
                                          "    background-color: rgb(85, 170, 255);\n"
                                          "    border-left: 28px solid rgb(85, 170, 255);\n"
                                          "}")
        self.btn_SAVEEXPORT.setObjectName("btn_SAVEEXPORT")
        self.horizontalLayout_8.addWidget(self.btn_SAVEEXPORT)
        self.frame_top_info_1 = QtWidgets.QFrame(self.frame_top_info)
        self.frame_top_info_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_info_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_info_1.setObjectName("frame_top_info_1")
        self.horizontalLayout_8.addWidget(self.frame_top_info_1)
        self.label_top_info_2 = QtWidgets.QLabel(self.frame_top_info)
        self.label_top_info_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_top_info_2.setFont(font)
        self.label_top_info_2.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_top_info_2.setObjectName("label_top_info_2")
        self.horizontalLayout_8.addWidget(self.label_top_info_2)
        self.verticalLayout_2.addWidget(self.frame_top_info)
        self.horizontalLayout_3.addWidget(self.frame_top_right)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_center = QtWidgets.QFrame(self.frame_main)
        self.frame_center.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.frame_center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menus.setObjectName("frame_menus")
        self.layout_menus = QtWidgets.QVBoxLayout(self.frame_menus)
        self.layout_menus.setContentsMargins(0, 0, 0, 0)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName("layout_menus")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")

        self.verticalLayout_5.addWidget(self.frame_menus, 0, QtCore.Qt.AlignTop)
        self.frame_extra_menus = QtWidgets.QFrame(self.frame_left_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy)
        self.frame_extra_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_extra_menus.setObjectName("frame_extra_menus")
        self.layout_menu_bottom = QtWidgets.QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName("layout_menu_bottom")
        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_content_right = QtWidgets.QFrame(self.frame_center)
        self.frame_content_right.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_right.setObjectName("frame_content_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_content = QtWidgets.QFrame(self.frame_content_right)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_content)
        self.stackedWidget.setStyleSheet("background: transparent;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_home = QtWidgets.QLabel(self.page_home)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_home.setFont(font)
        self.label_home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home.setObjectName("label_home")
        self.verticalLayout_10.addWidget(self.label_home)
        self.label_home2 = QtWidgets.QLabel(self.page_home)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_home2.setFont(font)
        self.label_home2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home2.setObjectName("label_home2")
        self.verticalLayout_10.addWidget(self.label_home2)
        self.stackedWidget.addWidget(self.page_home)
        self.page_preve = QtWidgets.QWidget()
        self.page_preve.setObjectName("page_preve")
        self.horizontalLayout_11 = QtWidgets.QVBoxLayout(self.page_preve)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_preve = QtWidgets.QFrame(self.page_preve)
        self.frame_preve.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.frame_preve.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_preve.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_preve.setObjectName("frame_preve")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_preve)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_preve2 = QtWidgets.QFrame(self.frame_preve)
        self.frame_preve2.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_preve2.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.frame_preve2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_preve2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_preve2.setObjectName("frame_preve2")
        self.textBox = QtWidgets.QLineEdit(self.frame_preve2)
        self.textBox.setGeometry(QtCore.QRect(30, 220, 391, 51))
        self.textBox.setStyleSheet("QLineEdit {\n"
                                   "    border: 2px solid rgb(45, 45, 45);\n"
                                   "    border-radius: 5px;\n"
                                   "    padding: 15px;\n"
                                   "    background-color: rgb(30, 30, 30);    \n"
                                   "    color: rgb(100, 100, 100);\n"
                                   "}\n"
                                   "QLineEdit:hover {\n"
                                   "    border: 2px solid rgb(55, 55, 55);\n"
                                   "}\n"
                                   "QLineEdit:focus {\n"
                                   "    border: 2px solid rgb(255, 207, 0);    \n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "}")
        self.textBox.setClearButtonEnabled(False)
        self.textBox.setObjectName("textBox")
        self.textBox2 = QtWidgets.QLineEdit(self.frame_preve2)
        self.textBox2.setGeometry(QtCore.QRect(30, 330, 391, 51))
        self.textBox2.setStyleSheet("QLineEdit {\n"
                                    "    border: 2px solid rgb(45, 45, 45);\n"
                                    "    border-radius: 5px;\n"
                                    "    padding: 15px;\n"
                                    "    background-color: rgb(30, 30, 30);    \n"
                                    "    color: rgb(100, 100, 100);\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "    border: 2px solid rgb(55, 55, 55);\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "    border: 2px solid rgb(255, 207, 0);    \n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "}")
        self.textBox2.setObjectName("textBox2")
        self.label_insert2 = QtWidgets.QLabel(self.frame_preve2)
        self.label_insert2.setGeometry(QtCore.QRect(30, 280, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_insert2.setFont(font)
        self.label_insert2.setObjectName("label_insert2")
        self.label_Insert = QtWidgets.QLabel(self.frame_preve2)
        self.label_Insert.setGeometry(QtCore.QRect(30, 170, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Insert.setFont(font)
        self.label_Insert.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Insert.setObjectName("label_Insert")
        self.label_TituPrev = QtWidgets.QLabel(self.frame_preve2)
        self.label_TituPrev.setGeometry(QtCore.QRect(50, 10, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_TituPrev.setFont(font)
        self.label_TituPrev.setObjectName("label_TituPrev")
        self.btn_prediction = QtWidgets.QPushButton(self.frame_preve2)
        self.btn_prediction.setGeometry(QtCore.QRect(30, 450, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_prediction.setFont(font)
        self.btn_prediction.setStyleSheet("QPushButton {    \n"
                                          "    background-color: rgb(50, 50, 50);\n"
                                          "    border: 2px solid rgb(60, 60, 60);\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "QPushButton:hover {    \n"
                                          "    background-color: rgb(60, 60, 60);\n"
                                          "    border: 2px solid rgb(70, 70, 70);\n"
                                          "}\n"
                                          "QPushButton:pressed {    \n"
                                          "    background-color: rgb(250, 230, 0);\n"
                                          "    border: 2px solid rgb(255, 165, 24);    \n"
                                          "    color: rgb(35, 35, 35);\n"
                                          "}")
        self.btn_prediction.setObjectName("btn_prediction")
        self.horizontalLayout_12.addWidget(self.frame_preve2)
        self.horizontalLayout_11.addWidget(self.frame_preve)
        self.stackedWidget.addWidget(self.page_preve)
        self.page_calculate = QtWidgets.QWidget()
        self.page_calculate.setObjectName("page_calculate")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.page_calculate)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_calcu = QtWidgets.QFrame(self.page_calculate)
        self.frame_calcu.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_calcu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_calcu.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.frame_calcu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_calcu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_calcu.setObjectName("frame_calcu")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_calcu)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_calcu2left = QtWidgets.QFrame(self.frame_calcu)
        self.frame_calcu2left.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_calcu2left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_calcu2left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_calcu2left.setObjectName("frame_calcu2left")
        self.btn_calculate = QtWidgets.QPushButton(self.frame_calcu2left)
        self.btn_calculate.setGeometry(QtCore.QRect(20, 80, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_calculate.setFont(font)
        self.btn_calculate.setStyleSheet("QPushButton {    \n"
                                         "    background-color: rgb(50, 50, 50);\n"
                                         "    border: 2px solid rgb(60, 60, 60);\n"
                                         "    border-radius: 5px;\n"
                                         "}\n"
                                         "QPushButton:hover {    \n"
                                         "    background-color: rgb(60, 60, 60);\n"
                                         "    border: 2px solid rgb(70, 70, 70);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(250, 230, 0);\n"
                                         "    border: 2px solid rgb(255, 165, 24);    \n"
                                         "    color: rgb(35, 35, 35);\n"
                                         "}")
        self.btn_calculate.setObjectName("btn_calculate")
        self.label_calcu = QtWidgets.QLabel(self.frame_calcu2left)
        self.label_calcu.setGeometry(QtCore.QRect(-20, 10, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_calcu.setFont(font)
        self.label_calcu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_calcu.setObjectName("label_calcu")
        self.horizontalLayout_13.addWidget(self.frame_calcu2left)
        self.textEdit_calcu = QtWidgets.QTextEdit(self.frame_calcu)
        self.textEdit_calcu.setMinimumSize(QtCore.QSize(400, 0))
        self.textEdit_calcu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit_calcu.setFont(font)
        self.textEdit_calcu.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_calcu.setAutoFillBackground(False)
        self.textEdit_calcu.setStyleSheet("QTextEdit{\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "color: black;\n"
                                          "}\n"
                                          "QTextEdit:focus {\n"
                                          "    border: 2px solid rgb(255, 207, 0);\n"
                                          "\n"
                                          "    color: black;\n"
                                          "}\n"
                                          "QScrollBar:vertical {\n"
                                          "    border: none;\n"
                                          "    background: rgb(45, 45, 68);\n"
                                          "    width: 14px;\n"
                                          "    margin: 15px 0 15px 0;\n"
                                          "    border-radius: 0px;\n"
                                          " }\n"
                                          "\n"
                                          "/*  HANDLE BAR VERTICAL */\n"
                                          "QScrollBar::handle:vertical {    \n"
                                          "    background-color: rgb(80, 80, 122);\n"
                                          "    min-height: 30px;\n"
                                          "    border-radius: 7px;\n"
                                          "}\n"
                                          "QScrollBar::handle:vertical:hover{    \n"
                                          "    background-color:  rgb(255, 207, 0);\n"
                                          "}\n"
                                          "QScrollBar::handle:vertical:pressed {    \n"
                                          "    background-color:  rgb(255, 207, 0);\n"
                                          "}\n"
                                          "\n"
                                          "/* BTN TOP - SCROLLBAR */\n"
                                          "QScrollBar::sub-line:vertical {\n"
                                          "    border: none;\n"
                                          "    background-color: rgb(59, 59, 90);\n"
                                          "    height: 15px;\n"
                                          "    border-top-left-radius: 7px;\n"
                                          "    border-top-right-radius: 7px;\n"
                                          "    subcontrol-position: top;\n"
                                          "    subcontrol-origin: margin;\n"
                                          "}\n"
                                          "QScrollBar::sub-line:vertical:hover {    \n"
                                          "    background-color:  rgb(255, 207, 0);\n"
                                          "}\n"
                                          "QScrollBar::sub-line:vertical:pressed {    \n"
                                          "    background-color: rgb(185, 0, 92);\n"
                                          "}\n"
                                          "\n"
                                          "/* BTN BOTTOM - SCROLLBAR */\n"
                                          "QScrollBar::add-line:vertical {\n"
                                          "    border: none;\n"
                                          "    background-color: rgb(59, 59, 90);\n"
                                          "    height: 15px;\n"
                                          "    border-bottom-left-radius: 7px;\n"
                                          "    border-bottom-right-radius: 7px;\n"
                                          "    subcontrol-position: bottom;\n"
                                          "    subcontrol-origin: margin;\n"
                                          "}\n"
                                          "QScrollBar::add-line:vertical:hover {    \n"
                                          "    background-color:  rgb(255, 207, 0);\n"
                                          "}\n"
                                          "QScrollBar::add-line:vertical:pressed {    \n"
                                          "    background-color: rgb(185, 0, 92);\n"
                                          "}\n"
                                          "\n"
                                          "/* RESET ARROW */\n"
                                          "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                          "    background: none;\n"
                                          "}\n"
                                          "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                          "    background: none;\n"
                                          "}")
        self.textEdit_calcu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_calcu.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_calcu.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_calcu.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit_calcu.setObjectName("textEdit_calcu")
        self.horizontalLayout_13.addWidget(self.textEdit_calcu)
        self.horizontalLayout_9.addWidget(self.frame_calcu)
        self.stackedWidget.addWidget(self.page_calculate)
        self.page_showFile = QtWidgets.QWidget()
        self.page_showFile.setObjectName("page_showFile")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.page_showFile)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_showFile1 = QtWidgets.QFrame(self.page_showFile)
        self.frame_showFile1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_showFile1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_showFile1.setObjectName("frame_showFile1")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_showFile1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_showFile2 = QtWidgets.QFrame(self.frame_showFile1)
        self.frame_showFile2.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_showFile2.setStyleSheet("")
        self.frame_showFile2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_showFile2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_showFile2.setObjectName("frame_showFile2")
        self.label_file = QtWidgets.QLabel(self.frame_showFile2)
        self.label_file.setGeometry(QtCore.QRect(10, 10, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_file.setFont(font)
        self.label_file.setStyleSheet("QTextLabel{\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "}")
        self.label_file.setAlignment(QtCore.Qt.AlignCenter)
        self.label_file.setObjectName("label_file")
        self.btn_mostrarDados = QtWidgets.QPushButton(self.frame_showFile2)
        self.btn_mostrarDados.setGeometry(QtCore.QRect(20, 140, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_mostrarDados.setFont(font)
        self.btn_mostrarDados.setStyleSheet("QPushButton {    \n"
                                            "    background-color: rgb(50, 50, 50);\n"
                                            "    border: 2px solid rgb(60, 60, 60);\n"
                                            "    border-radius: 5px;\n"
                                            "}\n"
                                            "QPushButton:hover {    \n"
                                            "    background-color: rgb(60, 60, 60);\n"
                                            "    border: 2px solid rgb(70, 70, 70);\n"
                                            "}\n"
                                            "QPushButton:pressed {    \n"
                                            "    background-color: rgb(250, 230, 0);\n"
                                            "    border: 2px solid rgb(255, 165, 24);    \n"
                                            "    color: rgb(35, 35, 35);\n"
                                            "}")
        self.btn_mostrarDados.setObjectName("btn_mostrarDados")
        self.horizontalLayout_15.addWidget(self.frame_showFile2)
        self.textEditFile = QtWidgets.QTextEdit(self.frame_showFile1)
        self.textEditFile.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEditFile.setFont(font)
        self.textEditFile.setStyleSheet("QTextEdit{\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "color: black;\n"
                                        "}\n"
                                        "QTextEdit:focus {\n"
                                        "    border: 2px solid rgb(255, 207, 0);\n"
                                        "\n"
                                        "    color: black;\n"
                                        "}\n"
                                        "QScrollBar:vertical {\n"
                                        "    border: none;\n"
                                        "    background: rgb(45, 45, 68);\n"
                                        "    width: 14px;\n"
                                        "    margin: 15px 0 15px 0;\n"
                                        "    border-radius: 0px;\n"
                                        " }\n"
                                        "\n"
                                        "/*  HANDLE BAR VERTICAL */\n"
                                        "QScrollBar::handle:vertical {    \n"
                                        "    background-color: rgb(80, 80, 122);\n"
                                        "    min-height: 30px;\n"
                                        "    border-radius: 7px;\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical:hover{    \n"
                                        "    background-color:  rgb(255, 207, 0);\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical:pressed {    \n"
                                        "    background-color:  rgb(255, 207, 0);\n"
                                        "}\n"
                                        "\n"
                                        "/* BTN TOP - SCROLLBAR */\n"
                                        "QScrollBar::sub-line:vertical {\n"
                                        "    border: none;\n"
                                        "    background-color: rgb(59, 59, 90);\n"
                                        "    height: 15px;\n"
                                        "    border-top-left-radius: 7px;\n"
                                        "    border-top-right-radius: 7px;\n"
                                        "    subcontrol-position: top;\n"
                                        "    subcontrol-origin: margin;\n"
                                        "}\n"
                                        "QScrollBar::sub-line:vertical:hover {    \n"
                                        "    background-color:  rgb(255, 207, 0);\n"
                                        "}\n"
                                        "QScrollBar::sub-line:vertical:pressed {    \n"
                                        "    background-color: rgb(185, 0, 92);\n"
                                        "}\n"
                                        "\n"
                                        "/* BTN BOTTOM - SCROLLBAR */\n"
                                        "QScrollBar::add-line:vertical {\n"
                                        "    border: none;\n"
                                        "    background-color: rgb(59, 59, 90);\n"
                                        "    height: 15px;\n"
                                        "    border-bottom-left-radius: 7px;\n"
                                        "    border-bottom-right-radius: 7px;\n"
                                        "    subcontrol-position: bottom;\n"
                                        "    subcontrol-origin: margin;\n"
                                        "}\n"
                                        "QScrollBar::add-line:vertical:hover {    \n"
                                        "    background-color:  rgb(255, 207, 0);\n"
                                        "}\n"
                                        "QScrollBar::add-line:vertical:pressed {    \n"
                                        "    background-color: rgb(185, 0, 92);\n"
                                        "}\n"
                                        "\n"
                                        "/* RESET ARROW */\n"
                                        "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                        "    background: none;\n"
                                        "}\n"
                                        "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                        "    background: none;\n"
                                        "}")
        self.textEditFile.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEditFile.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEditFile.setObjectName("textEditFile")
        self.horizontalLayout_15.addWidget(self.textEditFile)
        self.horizontalLayout_14.addWidget(self.frame_showFile1)
        self.stackedWidget.addWidget(self.page_showFile)
        self.page_showLog = QtWidgets.QWidget()
        self.page_showLog.setObjectName("page_showLog")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.page_showLog)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame_showLog1 = QtWidgets.QFrame(self.page_showLog)
        self.frame_showLog1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_showLog1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_showLog1.setObjectName("frame_showLog1")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_showLog1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_showLog2 = QtWidgets.QFrame(self.frame_showLog1)
        self.frame_showLog2.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_showLog2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_showLog2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_showLog2.setObjectName("frame_showLog2")
        self.label_log = QtWidgets.QLabel(self.frame_showLog2)
        self.label_log.setGeometry(QtCore.QRect(0, 0, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_log.setFont(font)
        self.label_log.setAlignment(QtCore.Qt.AlignCenter)
        self.label_log.setObjectName("label_log")
        self.btn_mostrarLog = QtWidgets.QPushButton(self.frame_showLog2)
        self.btn_mostrarLog.setGeometry(QtCore.QRect(20, 140, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_mostrarLog.setFont(font)
        self.btn_mostrarLog.setStyleSheet("QPushButton {    \n"
                                          "    background-color: rgb(50, 50, 50);\n"
                                          "    border: 2px solid rgb(60, 60, 60);\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "QPushButton:hover {    \n"
                                          "    background-color: rgb(60, 60, 60);\n"
                                          "    border: 2px solid rgb(70, 70, 70);\n"
                                          "}\n"
                                          "QPushButton:pressed {    \n"
                                          "    background-color: rgb(250, 230, 0);\n"
                                          "    border: 2px solid rgb(255, 165, 24);    \n"
                                          "    color: rgb(35, 35, 35);\n"
                                          "}")
        self.btn_mostrarLog.setObjectName("btn_mostrarLog")
        self.horizontalLayout_17.addWidget(self.frame_showLog2)
        self.textEditLog = QtWidgets.QTextEdit(self.frame_showLog1)
        self.textEditLog.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEditLog.setFont(font)
        self.textEditLog.setStyleSheet("QTextEdit{\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "color: black;\n"
                                       "}\n"
                                       "QTextEdit:focus {\n"
                                       "    border: 2px solid rgb(255, 207, 0);\n"
                                       "\n"
                                       "    color: black;\n"
                                       "}\n"
                                       "QScrollBar:vertical {\n"
                                       "    border: none;\n"
                                       "    background: rgb(45, 45, 68);\n"
                                       "    width: 14px;\n"
                                       "    margin: 15px 0 15px 0;\n"
                                       "    border-radius: 0px;\n"
                                       " }\n"
                                       "\n"
                                       "/*  HANDLE BAR VERTICAL */\n"
                                       "QScrollBar::handle:vertical {    \n"
                                       "    background-color: rgb(80, 80, 122);\n"
                                       "    min-height: 30px;\n"
                                       "    border-radius: 7px;\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical:hover{    \n"
                                       "    background-color:  rgb(255, 207, 0);\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical:pressed {    \n"
                                       "    background-color:  rgb(255, 207, 0);\n"
                                       "}\n"
                                       "\n"
                                       "/* BTN TOP - SCROLLBAR */\n"
                                       "QScrollBar::sub-line:vertical {\n"
                                       "    border: none;\n"
                                       "    background-color: rgb(59, 59, 90);\n"
                                       "    height: 15px;\n"
                                       "    border-top-left-radius: 7px;\n"
                                       "    border-top-right-radius: 7px;\n"
                                       "    subcontrol-position: top;\n"
                                       "    subcontrol-origin: margin;\n"
                                       "}\n"
                                       "QScrollBar::sub-line:vertical:hover {    \n"
                                       "    background-color:  rgb(255, 207, 0);\n"
                                       "}\n"
                                       "QScrollBar::sub-line:vertical:pressed {    \n"
                                       "    background-color: rgb(185, 0, 92);\n"
                                       "}\n"
                                       "\n"
                                       "/* BTN BOTTOM - SCROLLBAR */\n"
                                       "QScrollBar::add-line:vertical {\n"
                                       "    border: none;\n"
                                       "    background-color: rgb(59, 59, 90);\n"
                                       "    height: 15px;\n"
                                       "    border-bottom-left-radius: 7px;\n"
                                       "    border-bottom-right-radius: 7px;\n"
                                       "    subcontrol-position: bottom;\n"
                                       "    subcontrol-origin: margin;\n"
                                       "}\n"
                                       "QScrollBar::add-line:vertical:hover {    \n"
                                       "    background-color:  rgb(255, 207, 0);\n"
                                       "}\n"
                                       "QScrollBar::add-line:vertical:pressed {    \n"
                                       "    background-color: rgb(185, 0, 92);\n"
                                       "}\n"
                                       "\n"
                                       "/* RESET ARROW */\n"
                                       "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                       "    background: none;\n"
                                       "}\n"
                                       "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                       "    background: none;\n"
                                       "}")
        self.textEditLog.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEditLog.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEditLog.setObjectName("textEditLog")
        self.horizontalLayout_17.addWidget(self.textEditLog)
        self.horizontalLayout_16.addWidget(self.frame_showLog1)
        self.stackedWidget.addWidget(self.page_showLog)
        self.page_expor = QtWidgets.QWidget()
        self.page_expor.setObjectName("page_expor")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_expor)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_export = QtWidgets.QFrame(self.page_expor)
        self.frame_export.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_export.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_export.setObjectName("frame_export")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_export)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.frame_export2 = QtWidgets.QFrame(self.frame_export)
        self.frame_export2.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_export2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_export2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_export2.setObjectName("frame_export2")
        self.label_export = QtWidgets.QLabel(self.frame_export2)
        self.label_export.setGeometry(QtCore.QRect(0, 0, 301, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_export.setFont(font)
        self.label_export.setAlignment(QtCore.Qt.AlignCenter)
        self.label_export.setObjectName("label_export")
        self.btn_runExport = QtWidgets.QPushButton(self.frame_export2)
        self.btn_runExport.setGeometry(QtCore.QRect(20, 140, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_runExport.setFont(font)
        self.btn_runExport.setStyleSheet("QPushButton {    \n"
                                         "    background-color: rgb(50, 50, 50);\n"
                                         "    border: 2px solid rgb(60, 60, 60);\n"
                                         "    border-radius: 5px;\n"
                                         "}\n"
                                         "QPushButton:hover {    \n"
                                         "    background-color: rgb(60, 60, 60);\n"
                                         "    border: 2px solid rgb(70, 70, 70);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(250, 230, 0);\n"
                                         "    border: 2px solid rgb(255, 165, 24);    \n"
                                         "    color: rgb(35, 35, 35);\n"
                                         "}")
        self.btn_runExport.setObjectName("btn_runExport")
        self.horizontalLayout_18.addWidget(self.frame_export2)
        self.tableWidget_Export = QtWidgets.QTableWidget(self.frame_export)
        self.tableWidget_Export.setStyleSheet("QTableWidget{\n"
                                              "background-color: rgb(255, 255, 255);\n"
                                              "color: black;\n"
                                              "}\n"
                                              "QTableWidget:focus {\n"
                                              "    border: 2px solid rgb(255, 207, 0);\n"
                                              "\n"
                                              "    color: black;\n"
                                              "}\n"
                                              "")
        self.tableWidget_Export.setObjectName("tableWidget_Export")
        self.tableWidget_Export.setColumnCount(0)
        self.tableWidget_Export.setRowCount(0)
        self.horizontalLayout_18.addWidget(self.tableWidget_Export)
        self.verticalLayout_7.addWidget(self.frame_export)
        self.stackedWidget.addWidget(self.page_expor)
        self.verticalLayout_9.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.frame_content)
        self.frame_grip = QtWidgets.QFrame(self.frame_content_right)
        self.frame_grip.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_grip.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_grip.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_label_bottom = QtWidgets.QFrame(self.frame_grip)
        self.frame_label_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_bottom.setObjectName("frame_label_bottom")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_credits = QtWidgets.QLabel(self.frame_label_bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_credits.setText("")
        self.label_credits.setObjectName("label_credits")
        self.horizontalLayout_7.addWidget(self.label_credits)
        self.label_version = QtWidgets.QLabel(self.frame_label_bottom)
        self.label_version.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_7.addWidget(self.label_version)
        self.horizontalLayout_6.addWidget(self.frame_label_bottom)
        self.frame_size_grip = QtWidgets.QFrame(self.frame_grip)
        self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 20))
        self.frame_size_grip.setStyleSheet("QSizeGrip {\n"
                                           "    background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
                                           "    background-position: center;\n"
                                           "    background-repeat: no-reperat;\n"
                                           "}")
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontalLayout_6.addWidget(self.frame_size_grip)
        self.verticalLayout_4.addWidget(self.frame_grip)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout.addWidget(self.frame_center)
        self.horizontalLayout.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_bar_top.setText(_translate("MainWindow", "Process Mining"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize_restore.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        # ========================================================================================================
        self.btn_OPEN.setText(_translate("MainWindow", "Open File"))
        self.btn_OPEN.clicked.connect(self.open_file)

        self.btn_OpenLo.setText(_translate("MainWindow", "Open Log "))
        self.btn_OpenLo.clicked.connect(self.open_log)

        self.btn_SAVE.setText(_translate("MainWindow", "Save File"))
        self.btn_SAVE.clicked.connect(self.save_file)

        self.btn_SAVEEXPORT.setText(_translate("MainWindow", "Save Export"))
        self.btn_SAVEEXPORT.clicked.connect(self.export_ex)
        # ========================================================================================================
        self.label_top_info_2.setText(_translate("MainWindow", "| HOME"))
        self.label_home.setText(_translate("MainWindow", "HOME"))
        self.label_home2.setText(_translate("MainWindow", "Seja Bem-Vindo!"))
        self.textBox.setPlaceholderText(_translate("MainWindow", "Ex: Cable Head"))
        self.textBox2.setPlaceholderText(_translate("MainWindow", "Ex: 40 or 40-41"))
        self.label_insert2.setText(_translate("MainWindow", "Insira um Estado"))
        self.label_Insert.setText(_translate("MainWindow", "Insire um Produto"))
        self.label_TituPrev.setText(_translate("MainWindow", "Prever Estado"))

        # ========================================================================================================
        self.btn_prediction.setText(_translate("MainWindow", "Prever"))
        self.btn_prediction.clicked.connect(self.preverCalculo)

        self.btn_calculate.setText(_translate("MainWindow", "Calcular"))
        self.btn_calculate.clicked.connect(self.calcular)
        # ========================================================================================================
        self.label_calcu.setText(_translate("MainWindow", "Calcule o Log"))
        self.label_file.setText(_translate("MainWindow", "Mostrar dados"))
        # ========================================================================================================
        self.btn_mostrarDados.setText(_translate("MainWindow", "Iniciar"))
        self.btn_mostrarDados.clicked.connect(self.get_text_file)
        # ========================================================================================================
        self.label_log.setText(_translate("MainWindow", "Mostrar dados Log"))
        # =======================================================================================================
        self.btn_mostrarLog.setText(_translate("MainWindow", "Iniciar"))
        self.btn_mostrarLog.clicked.connect(self.get_table_Log)
        # ========================================================================================================
        self.label_export.setText(_translate("MainWindow", "Exportar Dados"))
        # ========================================================================================================
        self.btn_runExport.setText(_translate("MainWindow", "Exportar"))
        self.btn_runExport.clicked.connect(self.excel)
        # ========================================================================================================
        self.label_version.setText(_translate("MainWindow", "v1.0.0"))

    def open_file(self):
        self.file_name = ""
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        try:
            if dialog.exec_():
                self.file_name = dialog.selectedFiles()
            if self.file_name[0] != "":
                self.abrir()
        except:
            pass

    def get_text_file(self):
        LoopGet = True
        while LoopGet:
            try:
                self.abrir()
                if self.file_name[0] == "":
                    break
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Show File Data")
                msg.setText("Nenhum arquivo selecionado!!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                break
            if self.file_name[0].endswith('.txt'):
                with open(self.file_name[0], 'r') as f:
                    data = f.read()
                    self.textEditFile.setPlainText(data)
                    f.close()
            else:
                pass
            LoopGet = False

    def get_table_Log(self):
        LoopGet = True
        while LoopGet:
            try:
                if self.file_nameLog[0] == "":
                    msg = QMessageBox()
                    msg.setWindowTitle("Show File Data")
                    msg.setText("Nenhum arquivo selecionado!!!")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    break
                self.abrirLog()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Show File Data")
                msg.setText("Nenhum arquivo selecionado!!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                break
            if self.file_nameLog[0].endswith('.csv'):
                with open(self.file_nameLog[0], 'r') as f:
                    data = f.read()
                    self.textEditLog.setPlainText(data)
                    f.close()
            elif self.file_nameLog[0].endswith('.xlsx'):
                with open(self.file_nameLog[0], 'r') as f:
                    data = f.read()
                    self.textEditLog.setPlainText(data)
                    f.close()
            else:
                pass
            LoopGet = False

    def save_file(self):
        self.savefile = QFileDialog.getSaveFileName()
        if self.savefile[0] != "":
            self.writer()

    def open_log(self):
        self.file_nameLog = QFileDialog.getOpenFileName()
        if self.file_nameLog[0] != "":
            self.abrirLog()

    def export_ex(self):
        self.saveEx = QFileDialog.getSaveFileName()
        if self.saveEx[0] != "":
            self.save_ex()

    def save_ex(self):
        try:
            print(self.saveEx)
            writer = pd.ExcelWriter(f"{self.saveEx[0]}.xlsx")
            self.DataFrameTable.to_excel(writer, sheet_name="Sheet1")
            writer.save()
            msg = QMessageBox()
            msg.setWindowTitle("Save Excel")
            msg.setText("Arquivo salvo com sucesso!!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Save Excel")
            msg.setText("Ocorreu algum problema na hora de salvar, tente novamente!!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def abrirLog(self):
        logW = True
        while logW:
            try:
                try:
                    self.log = pd.read_excel(f"{self.file_nameLog[0]}", header=0, sep=",")
                    msg = QMessageBox()
                    msg.setWindowTitle("Open Log")
                    msg.setText("Arquivo aberto com Sucesso!!! (xlsx)")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                except:
                    self.log = pd.read_csv(f"{self.file_nameLog[0]}", header=0, sep=",")
                    msg = QMessageBox()
                    msg.setWindowTitle("Open Log")
                    msg.setText("Arquivo aberto com Sucesso!!! (csv)")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()

                self.log = self.log.rename(columns={'Case ID': 'CaseID'})
                self.log = self.log.rename(columns={'Start Timestamp': 'StartTimestamp'})
                self.log = self.log.rename(columns={'Qty Completed': 'QtyCompleted'})

                self.log["Start Timestamp"] = pd.to_datetime(self.log.StartTimestamp)
                self.log.sort_values(["CaseID", "StartTimestamp"], inplace=True)  # ORDENANDO A HORA E O ID

                self.listaLog = self.log["Activity"].unique()
                self.listaLog.sort()

                incre = 0
                for x in self.listaLog:
                    dici[x] = incre
                    incre += 1

                self.log.loc[self.log.QtyCompleted == 0, 'QtyCompleted'] = 1


            except:
                msg = QMessageBox()
                msg.setWindowTitle("Open Log File")
                msg.setText("O log insirido está com problemas, tente novamente!!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

            logW = False

    def abrir(self):
        global listas
        lc = True
        while lc:
            lce = False
            if self.file_name[0] != "":
                try:
                    dadosLog = open(f"{self.file_name[0]}", "r")
                    abrir = dadosLog.read()
                    listas = eval(abrir)
                    dadosLog.close()
                    msg = QMessageBox()
                    msg.setWindowTitle("Open File")
                    msg.setText("Arquivo aberto com sucesso!!")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                except:
                    dadosLog = open(f"{self.file_name[0]}", "w+")
                    dadosLog.write(str(listas))
                    dadosLog.close()
                    lce = True
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Open File")
                msg.setText("Arquivo selecionado não foi encontrado, tente novamente!!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                break
            lc = lce

    def writer(self):
        try:
            dadosLog = open(f"{self.savefile[0]}", "w+")
            dadosLog.write(str(listas))
            dadosLog.close()
            msg = QMessageBox()
            msg.setWindowTitle("Save File")
            msg.setText("Arquivo salvo com sucesso!!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Save File")
            msg.setText("Erro na seleção de um arquivo!! Tente novamente!!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def get_days(self, time_delta):
        return time_delta.days

    def get_seconds(self, time_delta):
        return time_delta.seconds

    def preverCalculo(self):
        global listas, Previ
        LoopPrevi = True
        while LoopPrevi:
            try:
                if self.file_name[0] == "":
                    break
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Prever Erro")
                msg.setText("Nenhum arquivo selecionado!!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                break
            Prod = self.textBox.text()
            State = self.textBox2.text()
            if Prod == "" or State == "":
                msg = QMessageBox()
                msg.setWindowTitle("Prever Erro")
                msg.setText("Entradas Inválidas, verefique suas entradas!!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                break
            try:
                Previ = listas[f'{Prod}'][f'{State}']
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Prever Erro")
                msg.setText("Entradas Inválidas, verefique suas entradas!!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                break
            if len(Previ) == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Prever Erro")
                msg.setText("Este estado está vazio!! Não possue nenhum termo!!!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                break
            Media = (sum(Previ) / len(Previ))
            msg = QMessageBox()
            msg.setWindowTitle("Prever Info")
            msg.setText(f"A media do estado inserido, presente do produto: {Prod} foi de: " + str(Media))
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            LoopPrevi = False

    def calcular(self):
        loop = 0
        LoopPreviCal = True
        while LoopPreviCal:
            try:
                if self.file_nameLog[0] == "":
                    msg = QMessageBox()
                    msg.setWindowTitle("Calculate Erro")
                    msg.setText("Voce não possui um log selecionado!! Selecione um Log no Menu")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    break
                self.abrirLog()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Calculate Erro")
                msg.setText("O arquivo do Log está com algum problema, insere novamente no menu!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                break
            try:
                if self.file_name[0] == "":
                    msg = QMessageBox()
                    msg.setWindowTitle("Calculate Erro")
                    msg.setText("Voce não possui um arquivo selecionado!! Selecione um arquivo no Menu")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    break
                self.abrir()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Calculate Erro")
                msg.setText("Voce não possui um arquivo selecionado!! Selecione um arquivo no Menu")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                break
            try:
                self.log["CaseID"] = pd.to_numeric(self.log["CaseID"].str[5:])
            except:
                print("")

            try:
                casos = self.log["CaseID"].unique()
                inicio = self.log["CaseID"].min()
                fim = self.log["CaseID"].max()
            except:
                break

            LoopID = True
            while LoopID:
                if inicio == fim:
                    break
                elif inicio not in casos:
                    inicio += 1
                    continue
                elif inicio <= fim:
                    logFs = self.log[self.log.CaseID == inicio]
                    lista = logFs["Activity"].unique()
                    listaP = logFs["Part Desc."].unique()

                    timeA = pd.Timestamp(logFs["StartTimestamp"].min())
                    timeB = pd.Timestamp(logFs["Complete Timestamp"].max())
                    timeF = timeB - timeA

                    timestampT = datetime.timestamp(timeA)
                    timestampT2 = datetime.timestamp(timeB)
                    timestampF = timestampT2 - timestampT

                    DataFrameDif = {"Diferença": []}
                    newDataFrame = pd.DataFrame(DataFrameDif)

                    newDataFrame["Diferença"] = (timeB - pd.to_datetime(logFs["StartTimestamp"]))

                    time_delta_series = newDataFrame["Diferença"]

                    converted_seriesD = time_delta_series.apply(self.get_days)
                    converted_seriesD = converted_seriesD * 1440

                    converted_seriesS = time_delta_series.apply(self.get_seconds)
                    converted_seriesS = converted_seriesS / 60

                    converted_seriesF = converted_seriesD + converted_seriesS

                    self.textEdit_calcu.insertPlainText(f"\n{logFs}")
                    self.textEdit_calcu.insertPlainText(
                        "\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                    self.textEdit_calcu.insertPlainText(f"\nTempo inicial: {timeA}")
                    self.textEdit_calcu.insertPlainText(f"\nTempo final: {timeB}")
                    self.textEdit_calcu.insertPlainText(f"\nO tempo total de execução deste produto foi de: {timeF}")
                    self.textEdit_calcu.insertPlainText(f"\nTotal: {timestampF / 60} minutos")

                    result = converted_seriesF / logFs["QtyCompleted"]

                    NumberEstado = ''
                    i = 0

                    for p in listaP:
                        Product = p
                        if Product in listas:
                            pass
                        else:
                            listas[f'{Product}'] = {}
                        for c in lista:
                            NumberEstado += str(dici[c])
                            try:
                                listas[f'{Product}'][f'{NumberEstado}'].append(result.iloc[i])
                            except KeyError:
                                listas[f'{Product}'][f'{NumberEstado}'] = []
                                listas[f'{Product}'][f'{NumberEstado}'].append(result.iloc[i])

                            NumberEstado += "-"
                            i += 1

                else:
                    break
                inicio += 1
            loop += 1
            LoopPreviCal = False
        if loop != 0:
            try:
                self.save_file()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Save")
                msg.setText("Ocorreu algum problema na hora de salvar, tente novamente!!")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()

    def excel(self):
        global listas, novalista

        LoopPreviEx = True
        while LoopPreviEx:
            try:
                if self.file_nameLog[0] == "":
                    msg = QMessageBox()
                    msg.setWindowTitle("Calculate Erro")
                    msg.setText("Voce não possui um log selecionado!! Selecione um Log no Menu")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    break
                self.abrirLog()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Calculate Erro")
                msg.setText("O arquivo do Log está com algum problema, insere novamente no menu!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                break
            try:
                if self.file_name[0] == "":
                    msg = QMessageBox()
                    msg.setWindowTitle("Export Erro")
                    msg.setText("Voce não possui um arquivo selecionado!! Selecione um arquivo no Menu")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    break
                self.abrir()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Export Erro")
                msg.setText("Voce não possui um arquivo selecionado!! Selecione um arquivo no Menu")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                break

            Looptxt = True
            while Looptxt:
                if len(listas) == 0:
                    msg = QMessageBox()
                    msg.setWindowTitle("Export Erro")
                    msg.setText(
                        "O arquivo inserido está vazio!! Insira outro ou tente carregar os dados na opção do Menu!!!")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()

                    break
                else:
                    try:
                        self.log["CaseID"] = pd.to_numeric(self.log["CaseID"].str[5:])
                    except:
                        print("")

                    casos = self.log["CaseID"].unique()

                    colunas = list(self.listaLog) + ['Estado', 'Ocorrido', 'Previsão', 'Resultado']
                    self.DataFrameTable = pd.DataFrame(columns=colunas)

                    inicio = self.log["CaseID"].min()
                    fim = self.log["CaseID"].max()
                    LoopID = True
                    while LoopID:
                        if inicio == fim:
                            break
                        elif inicio not in casos:
                            inicio += 1
                            continue
                        elif inicio <= fim:

                            logFs = self.log[self.log.CaseID == inicio]
                            lista = logFs["Activity"].unique()
                            listaP = logFs["Part Desc."].unique()

                            timeB = pd.Timestamp(logFs["Complete Timestamp"].max())

                            DataFrameDif = {"Diferença": []}
                            newDataFrame = pd.DataFrame(DataFrameDif)

                            newDataFrame["Diferença"] = (timeB - pd.to_datetime(logFs["StartTimestamp"]))

                            time_delta_series = newDataFrame["Diferença"]

                            converted_seriesD = time_delta_series.apply(self.get_days)
                            converted_seriesD = converted_seriesD * 1440

                            converted_seriesS = time_delta_series.apply(self.get_seconds)
                            converted_seriesS = converted_seriesS / 60

                            converted_seriesF = converted_seriesD + converted_seriesS

                            listaPrevi = converted_seriesF.unique()

                            Estado = ''
                            NumberEstado = ''
                            i = 0

                            for p in listaP:
                                Product = p
                                for c in lista:
                                    Estado += c
                                    NumberEstado += str(dici[c])

                                    try:
                                        MediaEx = sum(listas[f'{Product}'][f'{NumberEstado}']) / len(
                                            listas[f'{Product}'][f'{NumberEstado}'])
                                    except:
                                        break

                                    try:
                                        result = ((listaPrevi[i] - MediaEx) / listaPrevi[i])
                                    except:
                                        result = 0

                                    try:
                                        lAtividades = Estado.split("/")
                                    except KeyError:
                                        lAtividades = Estado.split("  ")

                                    l_output = [0 for y in range(0, len(dici))]
                                    for y in lAtividades:
                                        l_output[dici[y]] = l_output[dici[y]] + 1

                                    try:
                                        novalista = [l_output + [NumberEstado, listaPrevi[i], MediaEx, result]]

                                    except:
                                        pass

                                    Df2 = pd.DataFrame(novalista, columns=colunas)
                                    self.DataFrameTable = self.DataFrameTable.append(Df2, ignore_index=True)

                                    Estado += "/"
                                    NumberEstado += '-'

                                    i += 1

                        else:
                            break
                        inicio += 1

                    self.tableWidget_Export.setColumnCount(len(self.DataFrameTable.columns))
                    self.tableWidget_Export.setRowCount(len(self.DataFrameTable.index))
                    for i in range(len(self.DataFrameTable.index)):
                            for j in range(len(self.DataFrameTable.columns)):
                                    self.tableWidget_Export.setItem(i, j, QTableWidgetItem(str(self.DataFrameTable.iloc[i, j])))
                    self.tableWidget_Export.setHorizontalHeaderLabels(self.DataFrameTable.columns)
                    try:
                        self.export_ex()
                    except:
                        msg = QMessageBox()
                        msg.setWindowTitle("Export Erro")
                        msg.setText("Ocorreu algum problema na hora de salvar o log, tente novamente!!")
                        msg.setIcon(QMessageBox.Critical)
                        msg.exec_()
                    Looptxt = False
            LoopPreviEx = False

import files_rc