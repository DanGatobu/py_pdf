# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pypdfUqzjqB.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
import resource_rc
import resource_rc
import resource_rc
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(935, 643)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.gridLayout.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.menubtn = QPushButton(self.widget_4)
        self.menubtn.setObjectName(u"menubtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu-bar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menubtn.setIcon(icon)
        self.menubtn.setIconSize(QSize(30, 30))
        self.menubtn.setCheckable(True)

        self.horizontalLayout.addWidget(self.menubtn)

        self.horizontalSpacer_2 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.mainlogo = QLabel(self.widget_4)
        self.mainlogo.setObjectName(u"mainlogo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainlogo.sizePolicy().hasHeightForWidth())
        self.mainlogo.setSizePolicy(sizePolicy)
        self.mainlogo.setMinimumSize(QSize(50, 50))
        self.mainlogo.setMaximumSize(QSize(100, 71))
        self.mainlogo.setSizeIncrement(QSize(0, 0))
        self.mainlogo.setPixmap(QPixmap(u":/icons/icons/agent-high-resolution-logo.png"))
        self.mainlogo.setScaledContents(True)
        self.mainlogo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.mainlogo)

        self.horizontalSpacer = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.supportbtn = QPushButton(self.widget_4)
        self.supportbtn.setObjectName(u"supportbtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/support.png", QSize(), QIcon.Normal, QIcon.Off)
        self.supportbtn.setIcon(icon1)
        self.supportbtn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.supportbtn)


        self.verticalLayout_54.addWidget(self.widget_4)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 769, 760))
        self.horizontalLayout_57 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.widget_10 = QWidget(self.scrollAreaWidgetContents)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.widget_22 = QWidget(self.widget_10)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_28 = QVBoxLayout(self.widget_22)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.accountbalancelabel = QLabel(self.widget_22)
        self.accountbalancelabel.setObjectName(u"accountbalancelabel")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.accountbalancelabel.setFont(font)
        self.accountbalancelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.accountbalancelabel)


        self.verticalLayout_28.addLayout(self.verticalLayout_26)


        self.horizontalLayout_37.addWidget(self.widget_22)


        self.verticalLayout_61.addWidget(self.widget_10)

        self.widget_23 = QWidget(self.scrollAreaWidgetContents)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.performancelabel_15 = QLabel(self.widget_23)
        self.performancelabel_15.setObjectName(u"performancelabel_15")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.performancelabel_15.setFont(font1)
        self.performancelabel_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.performancelabel_15)

        self.label_9 = QLabel(self.widget_23)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Small Semibol"])
        font2.setBold(True)
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_9)

        self.statsbtn_15 = QPushButton(self.widget_23)
        self.statsbtn_15.setObjectName(u"statsbtn_15")
        font3 = QFont()
        font3.setBold(True)
        self.statsbtn_15.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icons8-merge-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.statsbtn_15.setIcon(icon2)
        self.statsbtn_15.setIconSize(QSize(20, 20))

        self.verticalLayout_31.addWidget(self.statsbtn_15)


        self.horizontalLayout_27.addLayout(self.verticalLayout_31)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.mt5label_14 = QLabel(self.widget_23)
        self.mt5label_14.setObjectName(u"mt5label_14")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.mt5label_14.setFont(font4)
        self.mt5label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.mt5label_14)

        self.label_10 = QLabel(self.widget_23)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_10)

        self.setupbtn_14 = QPushButton(self.widget_23)
        self.setupbtn_14.setObjectName(u"setupbtn_14")
        self.setupbtn_14.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icons8-compress-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setupbtn_14.setIcon(icon3)
        self.setupbtn_14.setIconSize(QSize(20, 20))

        self.verticalLayout_32.addWidget(self.setupbtn_14)


        self.horizontalLayout_27.addLayout(self.verticalLayout_32)


        self.verticalLayout_61.addWidget(self.widget_23)

        self.widget_12 = QWidget(self.scrollAreaWidgetContents)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.performancelabel_10 = QLabel(self.widget_12)
        self.performancelabel_10.setObjectName(u"performancelabel_10")
        self.performancelabel_10.setFont(font1)
        self.performancelabel_10.setAlignment(Qt.AlignCenter)
        self.performancelabel_10.setMargin(2)

        self.verticalLayout_22.addWidget(self.performancelabel_10)

        self.label_3 = QLabel(self.widget_12)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(3)

        self.verticalLayout_22.addWidget(self.label_3)

        self.statsbtn_10 = QPushButton(self.widget_12)
        self.statsbtn_10.setObjectName(u"statsbtn_10")
        self.statsbtn_10.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icons8-extract-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.statsbtn_10.setIcon(icon4)
        self.statsbtn_10.setIconSize(QSize(20, 20))

        self.verticalLayout_22.addWidget(self.statsbtn_10)


        self.horizontalLayout_23.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.mt5label_9 = QLabel(self.widget_12)
        self.mt5label_9.setObjectName(u"mt5label_9")
        self.mt5label_9.setFont(font4)
        self.mt5label_9.setAlignment(Qt.AlignCenter)
        self.mt5label_9.setMargin(2)

        self.verticalLayout_23.addWidget(self.mt5label_9)

        self.label_6 = QLabel(self.widget_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(3)

        self.verticalLayout_23.addWidget(self.label_6)

        self.setupbtn_9 = QPushButton(self.widget_12)
        self.setupbtn_9.setObjectName(u"setupbtn_9")
        self.setupbtn_9.setFont(font3)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icons8-split-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setupbtn_9.setIcon(icon5)
        self.setupbtn_9.setIconSize(QSize(20, 20))

        self.verticalLayout_23.addWidget(self.setupbtn_9)


        self.horizontalLayout_23.addLayout(self.verticalLayout_23)


        self.verticalLayout_61.addWidget(self.widget_12)

        self.widget_45 = QWidget(self.scrollAreaWidgetContents)
        self.widget_45.setObjectName(u"widget_45")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.performancelabel_12 = QLabel(self.widget_45)
        self.performancelabel_12.setObjectName(u"performancelabel_12")
        self.performancelabel_12.setFont(font1)
        self.performancelabel_12.setAlignment(Qt.AlignCenter)
        self.performancelabel_12.setMargin(2)

        self.verticalLayout_59.addWidget(self.performancelabel_12)

        self.label_4 = QLabel(self.widget_45)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(3)

        self.verticalLayout_59.addWidget(self.label_4)

        self.statsbtn_12 = QPushButton(self.widget_45)
        self.statsbtn_12.setObjectName(u"statsbtn_12")
        self.statsbtn_12.setFont(font3)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/icons8-encrypt-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.statsbtn_12.setIcon(icon6)
        self.statsbtn_12.setIconSize(QSize(20, 20))

        self.verticalLayout_59.addWidget(self.statsbtn_12)


        self.horizontalLayout_25.addLayout(self.verticalLayout_59)

        self.verticalLayout_66 = QVBoxLayout()
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.mt5label_11 = QLabel(self.widget_45)
        self.mt5label_11.setObjectName(u"mt5label_11")
        self.mt5label_11.setFont(font4)
        self.mt5label_11.setAlignment(Qt.AlignCenter)
        self.mt5label_11.setMargin(2)

        self.verticalLayout_66.addWidget(self.mt5label_11)

        self.label_7 = QLabel(self.widget_45)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(3)

        self.verticalLayout_66.addWidget(self.label_7)

        self.setupbtn_11 = QPushButton(self.widget_45)
        self.setupbtn_11.setObjectName(u"setupbtn_11")
        self.setupbtn_11.setFont(font3)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/icons8-access-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setupbtn_11.setIcon(icon7)
        self.setupbtn_11.setIconSize(QSize(20, 20))

        self.verticalLayout_66.addWidget(self.setupbtn_11)


        self.horizontalLayout_25.addLayout(self.verticalLayout_66)


        self.verticalLayout_61.addWidget(self.widget_45)

        self.widget_25 = QWidget(self.scrollAreaWidgetContents)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.performancelabel_11 = QLabel(self.widget_25)
        self.performancelabel_11.setObjectName(u"performancelabel_11")
        self.performancelabel_11.setFont(font1)
        self.performancelabel_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.performancelabel_11)

        self.label_5 = QLabel(self.widget_25)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setMargin(3)

        self.verticalLayout_24.addWidget(self.label_5)

        self.statsbtn_11 = QPushButton(self.widget_25)
        self.statsbtn_11.setObjectName(u"statsbtn_11")
        self.statsbtn_11.setFont(font3)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/development.png", QSize(), QIcon.Normal, QIcon.Off)
        self.statsbtn_11.setIcon(icon8)
        self.statsbtn_11.setIconSize(QSize(20, 20))

        self.verticalLayout_24.addWidget(self.statsbtn_11)


        self.horizontalLayout_24.addLayout(self.verticalLayout_24)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.mt5label_10 = QLabel(self.widget_25)
        self.mt5label_10.setObjectName(u"mt5label_10")
        self.mt5label_10.setFont(font4)
        self.mt5label_10.setAlignment(Qt.AlignCenter)
        self.mt5label_10.setMargin(2)

        self.verticalLayout_27.addWidget(self.mt5label_10)

        self.label_8 = QLabel(self.widget_25)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setMargin(3)

        self.verticalLayout_27.addWidget(self.label_8)

        self.setupbtn_10 = QPushButton(self.widget_25)
        self.setupbtn_10.setObjectName(u"setupbtn_10")
        self.setupbtn_10.setFont(font3)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/user (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.setupbtn_10.setIcon(icon9)
        self.setupbtn_10.setIconSize(QSize(20, 20))

        self.verticalLayout_27.addWidget(self.setupbtn_10)


        self.horizontalLayout_24.addLayout(self.verticalLayout_27)


        self.verticalLayout_61.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.scrollAreaWidgetContents)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.performancelabel_13 = QLabel(self.widget_26)
        self.performancelabel_13.setObjectName(u"performancelabel_13")
        self.performancelabel_13.setFont(font1)
        self.performancelabel_13.setAlignment(Qt.AlignCenter)
        self.performancelabel_13.setMargin(2)

        self.verticalLayout_29.addWidget(self.performancelabel_13)

        self.label_13 = QLabel(self.widget_26)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setMargin(3)

        self.verticalLayout_29.addWidget(self.label_13)

        self.statsbtn_13 = QPushButton(self.widget_26)
        self.statsbtn_13.setObjectName(u"statsbtn_13")
        self.statsbtn_13.setFont(font3)
        self.statsbtn_13.setIcon(icon8)
        self.statsbtn_13.setIconSize(QSize(20, 20))

        self.verticalLayout_29.addWidget(self.statsbtn_13)


        self.horizontalLayout_26.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.mt5label_12 = QLabel(self.widget_26)
        self.mt5label_12.setObjectName(u"mt5label_12")
        self.mt5label_12.setFont(font4)
        self.mt5label_12.setAlignment(Qt.AlignCenter)
        self.mt5label_12.setMargin(2)

        self.verticalLayout_30.addWidget(self.mt5label_12)

        self.label_11 = QLabel(self.widget_26)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setMargin(3)

        self.verticalLayout_30.addWidget(self.label_11)

        self.setupbtn_12 = QPushButton(self.widget_26)
        self.setupbtn_12.setObjectName(u"setupbtn_12")
        self.setupbtn_12.setFont(font3)
        self.setupbtn_12.setIcon(icon9)
        self.setupbtn_12.setIconSize(QSize(20, 20))

        self.verticalLayout_30.addWidget(self.setupbtn_12)


        self.horizontalLayout_26.addLayout(self.verticalLayout_30)


        self.verticalLayout_61.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.scrollAreaWidgetContents)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_85 = QVBoxLayout(self.widget_27)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.widget_36 = QWidget(self.widget_27)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.performancelabel_14 = QLabel(self.widget_36)
        self.performancelabel_14.setObjectName(u"performancelabel_14")
        self.performancelabel_14.setFont(font1)
        self.performancelabel_14.setAlignment(Qt.AlignCenter)
        self.performancelabel_14.setMargin(2)

        self.verticalLayout_56.addWidget(self.performancelabel_14)

        self.label_14 = QLabel(self.widget_36)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setMargin(3)

        self.verticalLayout_56.addWidget(self.label_14)

        self.statsbtn_14 = QPushButton(self.widget_36)
        self.statsbtn_14.setObjectName(u"statsbtn_14")
        self.statsbtn_14.setFont(font3)
        self.statsbtn_14.setIcon(icon8)
        self.statsbtn_14.setIconSize(QSize(20, 20))

        self.verticalLayout_56.addWidget(self.statsbtn_14)


        self.horizontalLayout_14.addLayout(self.verticalLayout_56)

        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.mt5label_13 = QLabel(self.widget_36)
        self.mt5label_13.setObjectName(u"mt5label_13")
        self.mt5label_13.setFont(font4)
        self.mt5label_13.setAlignment(Qt.AlignCenter)
        self.mt5label_13.setMargin(2)

        self.verticalLayout_60.addWidget(self.mt5label_13)

        self.label_12 = QLabel(self.widget_36)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setMargin(3)

        self.verticalLayout_60.addWidget(self.label_12)

        self.setupbtn_13 = QPushButton(self.widget_36)
        self.setupbtn_13.setObjectName(u"setupbtn_13")
        self.setupbtn_13.setFont(font3)
        self.setupbtn_13.setIcon(icon9)
        self.setupbtn_13.setIconSize(QSize(20, 20))

        self.verticalLayout_60.addWidget(self.setupbtn_13)


        self.horizontalLayout_14.addLayout(self.verticalLayout_60)


        self.verticalLayout_85.addWidget(self.widget_36)


        self.verticalLayout_61.addWidget(self.widget_27)


        self.horizontalLayout_57.addLayout(self.verticalLayout_61)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_3)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_81 = QVBoxLayout(self.page_6)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.splitter = QSplitter(self.page_6)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_16 = QVBoxLayout(self.widget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_38 = QWidget(self.widget)
        self.widget_38.setObjectName(u"widget_38")
        self.verticalLayout_80 = QVBoxLayout(self.widget_38)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer_5 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_3 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_15 = QLabel(self.widget_38)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(QPixmap(u":/icons/icons/icons8-upload-50.png"))
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_15)

        self.label_16 = QLabel(self.widget_38)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_4.addWidget(self.label_16)


        self.horizontalLayout_13.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_5 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)


        self.verticalLayout_15.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_4 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_4)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_4 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)

        self.pushButton_2 = QPushButton(self.widget_38)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_15.addWidget(self.pushButton_2)

        self.horizontalSpacer_6 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)


        self.verticalLayout_15.addLayout(self.horizontalLayout_15)


        self.verticalLayout_80.addLayout(self.verticalLayout_15)


        self.verticalLayout_16.addWidget(self.widget_38)

        self.widget_37 = QWidget(self.widget)
        self.widget_37.setObjectName(u"widget_37")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_44 = QLabel(self.widget_37)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_44)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.lineEdit_8 = QLineEdit(self.widget_37)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_43.addWidget(self.lineEdit_8)


        self.verticalLayout_20.addLayout(self.horizontalLayout_43)


        self.horizontalLayout_42.addLayout(self.verticalLayout_20)


        self.verticalLayout_16.addWidget(self.widget_37)

        self.splitter.addWidget(self.widget)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_18 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.layoutWidget2)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_17 = QVBoxLayout(self.widget_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.tableWidget = QTableWidget(self.widget_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_17.addWidget(self.tableWidget)

        self.pushButton_11 = QPushButton(self.widget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_17.addWidget(self.pushButton_11)


        self.verticalLayout_18.addWidget(self.widget_2)

        self.pushButton_3 = QPushButton(self.layoutWidget2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_18.addWidget(self.pushButton_3)

        self.splitter.addWidget(self.layoutWidget2)

        self.verticalLayout_81.addWidget(self.splitter)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.horizontalLayout_44 = QHBoxLayout(self.page_7)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.splitter_3 = QSplitter(self.page_7)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.widget_8 = QWidget(self.splitter_3)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_33 = QVBoxLayout(self.widget_8)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.widget_39 = QWidget(self.widget_8)
        self.widget_39.setObjectName(u"widget_39")
        self.verticalLayout_82 = QVBoxLayout(self.widget_39)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalSpacer_6 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_6)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_7 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_19 = QLabel(self.widget_39)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setPixmap(QPixmap(u":/icons/icons/icons8-upload-50.png"))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_19)

        self.label_20 = QLabel(self.widget_39)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_36.addWidget(self.label_20)


        self.horizontalLayout_16.addLayout(self.verticalLayout_36)

        self.horizontalSpacer_8 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)


        self.verticalLayout_35.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_7 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_7)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_9 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_9)

        self.pushButton_5 = QPushButton(self.widget_39)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_17.addWidget(self.pushButton_5)

        self.horizontalSpacer_10 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_10)


        self.verticalLayout_35.addLayout(self.horizontalLayout_17)


        self.verticalLayout_82.addLayout(self.verticalLayout_35)


        self.verticalLayout_33.addWidget(self.widget_39)

        self.widget_35 = QWidget(self.widget_8)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_43 = QLabel(self.widget_35)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_43)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.lineEdit_7 = QLineEdit(self.widget_35)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_41.addWidget(self.lineEdit_7)


        self.verticalLayout_39.addLayout(self.horizontalLayout_41)


        self.horizontalLayout_40.addLayout(self.verticalLayout_39)


        self.verticalLayout_33.addWidget(self.widget_35)

        self.splitter_3.addWidget(self.widget_8)
        self.layoutWidget3 = QWidget(self.splitter_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.verticalLayout_37 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.layoutWidget3)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_38 = QVBoxLayout(self.widget_9)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.tableWidget_2 = QTableWidget(self.widget_9)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_38.addWidget(self.tableWidget_2)

        self.pushButton_12 = QPushButton(self.widget_9)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_38.addWidget(self.pushButton_12)


        self.verticalLayout_37.addWidget(self.widget_9)

        self.splitter_2 = QSplitter(self.layoutWidget3)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_21 = QLabel(self.splitter_2)
        self.label_21.setObjectName(u"label_21")
        self.splitter_2.addWidget(self.label_21)
        self.lineEdit = QLineEdit(self.splitter_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.splitter_2.addWidget(self.lineEdit)

        self.verticalLayout_37.addWidget(self.splitter_2)

        self.pushButton_6 = QPushButton(self.layoutWidget3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_37.addWidget(self.pushButton_6)

        self.splitter_3.addWidget(self.layoutWidget3)

        self.horizontalLayout_44.addWidget(self.splitter_3)

        self.stackedWidget.addWidget(self.page_7)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.pdf_display = QWidget(self.page_9)
        self.pdf_display.setObjectName(u"pdf_display")
        self.pdf_display.setGeometry(QRect(470, 190, 208, 71))
        self.horizontalLayout_10 = QHBoxLayout(self.pdf_display)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.pdf_display)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setPixmap(QPixmap(u":/icons/icons/icons8-pdf-50.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.label = QLabel(self.pdf_display)
        self.label.setObjectName(u"label")

        self.horizontalLayout_10.addWidget(self.label)

        self.pushButton = QPushButton(self.pdf_display)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon10)

        self.horizontalLayout_10.addWidget(self.pushButton)

        self.layoutWidget_2 = QWidget(self.page_9)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(410, 350, 77, 82))
        self.verticalLayout_21 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.layoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setPixmap(QPixmap(u":/icons/icons/icons8-upload-50.png"))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_17)

        self.label_18 = QLabel(self.layoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_21.addWidget(self.label_18)

        self.pushButton_4 = QPushButton(self.page_9)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(240, 260, 75, 24))
        self.splitter_4 = QSplitter(self.page_9)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(-70, 20, 561, 351))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.widget_11 = QWidget(self.splitter_4)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_40 = QVBoxLayout(self.widget_11)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalSpacer_8 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_8)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_11 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_11)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_22 = QLabel(self.widget_11)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setPixmap(QPixmap(u":/icons/icons/icons8-upload-50.png"))
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.label_22)

        self.label_23 = QLabel(self.widget_11)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_42.addWidget(self.label_23)


        self.horizontalLayout_18.addLayout(self.verticalLayout_42)

        self.horizontalSpacer_12 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_12)


        self.verticalLayout_41.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_9 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_9)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_13 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_13)

        self.pushButton_7 = QPushButton(self.widget_11)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_19.addWidget(self.pushButton_7)

        self.horizontalSpacer_14 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_14)


        self.verticalLayout_41.addLayout(self.horizontalLayout_19)


        self.verticalLayout_40.addLayout(self.verticalLayout_41)

        self.splitter_4.addWidget(self.widget_11)
        self.layoutWidget_3 = QWidget(self.splitter_4)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.verticalLayout_43 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.layoutWidget_3)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_44 = QVBoxLayout(self.widget_13)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.listWidget_3 = QListWidget(self.widget_13)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.verticalLayout_44.addWidget(self.listWidget_3)


        self.verticalLayout_43.addWidget(self.widget_13)

        self.pushButton_8 = QPushButton(self.layoutWidget_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_43.addWidget(self.pushButton_8)

        self.splitter_4.addWidget(self.layoutWidget_3)
        self.widget_30 = QWidget(self.page_9)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setGeometry(QRect(150, 460, 236, 68))
        self.horizontalLayout_34 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_40 = QLabel(self.widget_30)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_40)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.lineEdit_4 = QLineEdit(self.widget_30)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_33.addWidget(self.lineEdit_4)

        self.pushButton_16 = QPushButton(self.widget_30)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_33.addWidget(self.pushButton_16)


        self.verticalLayout_8.addLayout(self.horizontalLayout_33)


        self.horizontalLayout_34.addLayout(self.verticalLayout_8)

        self.widget_43 = QWidget(self.page_9)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setGeometry(QRect(640, 410, 464, 431))
        self.verticalLayout_87 = QVBoxLayout(self.widget_43)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_65 = QVBoxLayout()
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalSpacer_18 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_18)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalSpacer_39 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_39)

        self.verticalLayout_67 = QVBoxLayout()
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_45 = QLabel(self.widget_43)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setPixmap(QPixmap(u":/icons/icons/icons8-upload-50.png"))
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.label_45)

        self.label_46 = QLabel(self.widget_43)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_67.addWidget(self.label_46)


        self.horizontalLayout_47.addLayout(self.verticalLayout_67)

        self.horizontalSpacer_40 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_40)


        self.verticalLayout_65.addLayout(self.horizontalLayout_47)

        self.verticalSpacer_19 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_19)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalSpacer_41 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_41)

        self.pushButton_21 = QPushButton(self.widget_43)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.horizontalLayout_48.addWidget(self.pushButton_21)

        self.horizontalSpacer_42 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_42)


        self.verticalLayout_65.addLayout(self.horizontalLayout_48)


        self.verticalLayout_87.addLayout(self.verticalLayout_65)

        self.stackedWidget.addWidget(self.page_9)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_45 = QHBoxLayout(self.page_5)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.splitter_5 = QSplitter(self.page_5)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.widget_14 = QWidget(self.splitter_5)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_45 = QVBoxLayout(self.widget_14)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.widget_40 = QWidget(self.widget_14)
        self.widget_40.setObjectName(u"widget_40")
        self.verticalLayout_83 = QVBoxLayout(self.widget_40)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalSpacer_10 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_10)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_15 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_15)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_24 = QLabel(self.widget_40)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setPixmap(QPixmap(u":/icons/icons/icons8-upload-50.png"))
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_48.addWidget(self.label_24)

        self.label_25 = QLabel(self.widget_40)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_48.addWidget(self.label_25)


        self.horizontalLayout_20.addLayout(self.verticalLayout_48)

        self.horizontalSpacer_16 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_16)


        self.verticalLayout_46.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_11 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_11)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_17 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_17)

        self.pushButton_9 = QPushButton(self.widget_40)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_21.addWidget(self.pushButton_9)

        self.horizontalSpacer_18 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_18)


        self.verticalLayout_46.addLayout(self.horizontalLayout_21)


        self.verticalLayout_83.addLayout(self.verticalLayout_46)


        self.verticalLayout_45.addWidget(self.widget_40)

        self.widget_33 = QWidget(self.widget_14)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_42 = QLabel(self.widget_33)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.label_42)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.lineEdit_6 = QLineEdit(self.widget_33)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_39.addWidget(self.lineEdit_6)


        self.verticalLayout_51.addLayout(self.horizontalLayout_39)


        self.horizontalLayout_38.addLayout(self.verticalLayout_51)


        self.verticalLayout_45.addWidget(self.widget_33)

        self.splitter_5.addWidget(self.widget_14)
        self.layoutWidget_4 = QWidget(self.splitter_5)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.verticalLayout_49 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.layoutWidget_4)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_50 = QVBoxLayout(self.widget_15)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.tableWidget_3 = QTableWidget(self.widget_15)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_50.addWidget(self.tableWidget_3)

        self.pushButton_23 = QPushButton(self.widget_15)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.verticalLayout_50.addWidget(self.pushButton_23)


        self.verticalLayout_49.addWidget(self.widget_15)

        self.splitter_6 = QSplitter(self.layoutWidget_4)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.label_26 = QLabel(self.splitter_6)
        self.label_26.setObjectName(u"label_26")
        self.splitter_6.addWidget(self.label_26)
        self.lineEdit_2 = QLineEdit(self.splitter_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.splitter_6.addWidget(self.lineEdit_2)

        self.verticalLayout_49.addWidget(self.splitter_6)

        self.pushButton_10 = QPushButton(self.layoutWidget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_49.addWidget(self.pushButton_10)

        self.splitter_5.addWidget(self.layoutWidget_4)

        self.horizontalLayout_45.addWidget(self.splitter_5)

        self.stackedWidget.addWidget(self.page_5)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.horizontalLayout_46 = QHBoxLayout(self.page_11)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.splitter_7 = QSplitter(self.page_11)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Horizontal)
        self.widget_24 = QWidget(self.splitter_7)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_72 = QVBoxLayout(self.widget_24)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.widget_41 = QWidget(self.widget_24)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_84 = QVBoxLayout(self.widget_41)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_73 = QVBoxLayout()
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalSpacer_16 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_73.addItem(self.verticalSpacer_16)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_35 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_35)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_36 = QLabel(self.widget_41)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setPixmap(QPixmap(u":/icons/icons/icons8-upload-50.png"))
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_36)

        self.label_37 = QLabel(self.widget_41)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_7.addWidget(self.label_37)


        self.horizontalLayout_31.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_36 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_36)


        self.verticalLayout_73.addLayout(self.horizontalLayout_31)

        self.verticalSpacer_17 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_73.addItem(self.verticalSpacer_17)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_37 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_37)

        self.pushButton_14 = QPushButton(self.widget_41)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_32.addWidget(self.pushButton_14)

        self.horizontalSpacer_38 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_38)


        self.verticalLayout_73.addLayout(self.horizontalLayout_32)


        self.verticalLayout_84.addLayout(self.verticalLayout_73)


        self.verticalLayout_72.addWidget(self.widget_41)

        self.widget_32 = QWidget(self.widget_24)
        self.widget_32.setObjectName(u"widget_32")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.verticalLayout_77 = QVBoxLayout()
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.label_41 = QLabel(self.widget_32)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_77.addWidget(self.label_41)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.lineEdit_5 = QLineEdit(self.widget_32)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_36.addWidget(self.lineEdit_5)


        self.verticalLayout_77.addLayout(self.horizontalLayout_36)


        self.horizontalLayout_35.addLayout(self.verticalLayout_77)


        self.verticalLayout_72.addWidget(self.widget_32)

        self.splitter_7.addWidget(self.widget_24)
        self.layoutWidget_10 = QWidget(self.splitter_7)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.verticalLayout_75 = QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.widget_29 = QWidget(self.layoutWidget_10)
        self.widget_29.setObjectName(u"widget_29")
        self.verticalLayout_76 = QVBoxLayout(self.widget_29)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.label_38 = QLabel(self.widget_29)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.label_38)

        self.tableWidget_4 = QTableWidget(self.widget_29)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.verticalLayout_76.addWidget(self.tableWidget_4)

        self.pushButton_24 = QPushButton(self.widget_29)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.verticalLayout_76.addWidget(self.pushButton_24)


        self.verticalLayout_75.addWidget(self.widget_29)

        self.pushButton_15 = QPushButton(self.layoutWidget_10)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_75.addWidget(self.pushButton_15)

        self.label_39 = QLabel(self.layoutWidget_10)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.verticalLayout_75.addWidget(self.label_39)

        self.textEdit = QTextEdit(self.layoutWidget_10)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_75.addWidget(self.textEdit)

        self.splitter_7.addWidget(self.layoutWidget_10)

        self.horizontalLayout_46.addWidget(self.splitter_7)

        self.stackedWidget.addWidget(self.page_11)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_78 = QVBoxLayout(self.page)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_7 = QWidget(self.page)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_42 = QWidget(self.widget_7)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_86 = QVBoxLayout(self.widget_42)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalSpacer_14 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_64.addItem(self.verticalSpacer_14)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_23 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_23)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_30 = QLabel(self.widget_42)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setPixmap(QPixmap(u":/icons/icons/icons8-upload-50.png"))
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_30)

        self.label_31 = QLabel(self.widget_42)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_6.addWidget(self.label_31)


        self.horizontalLayout_29.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_24 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_24)


        self.verticalLayout_64.addLayout(self.horizontalLayout_29)

        self.verticalSpacer_15 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_64.addItem(self.verticalSpacer_15)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_25 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_25)

        self.pushButton_13 = QPushButton(self.widget_42)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_30.addWidget(self.pushButton_13)

        self.horizontalSpacer_26 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_26)


        self.verticalLayout_64.addLayout(self.horizontalLayout_30)


        self.verticalLayout_86.addLayout(self.verticalLayout_64)


        self.horizontalLayout_6.addWidget(self.widget_42)

        self.tableWidget_5 = QTableWidget(self.widget_7)
        self.tableWidget_5.setObjectName(u"tableWidget_5")

        self.horizontalLayout_6.addWidget(self.tableWidget_5)

        self.widget_21 = QWidget(self.widget_7)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_68 = QVBoxLayout(self.widget_21)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")

        self.horizontalLayout_6.addWidget(self.widget_21)


        self.verticalLayout_10.addWidget(self.widget_7)

        self.pushButton_25 = QPushButton(self.page)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.verticalLayout_10.addWidget(self.pushButton_25)

        self.widget_44 = QWidget(self.page)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.verticalLayout_74 = QVBoxLayout()
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.label_47 = QLabel(self.widget_44)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_74.addWidget(self.label_47)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.lineEdit_9 = QLineEdit(self.widget_44)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_50.addWidget(self.lineEdit_9)


        self.verticalLayout_74.addLayout(self.horizontalLayout_50)


        self.horizontalLayout_49.addLayout(self.verticalLayout_74)


        self.verticalLayout_10.addWidget(self.widget_44)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_5 = QWidget(self.page)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_69 = QVBoxLayout()
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.performancelabel_17 = QLabel(self.widget_5)
        self.performancelabel_17.setObjectName(u"performancelabel_17")
        self.performancelabel_17.setFont(font1)
        self.performancelabel_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.performancelabel_17)

        self.label_33 = QLabel(self.widget_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)
        self.label_33.setAlignment(Qt.AlignCenter)
        self.label_33.setWordWrap(True)
        self.label_33.setMargin(5)

        self.verticalLayout_69.addWidget(self.label_33)

        self.statsbtn_17 = QPushButton(self.widget_5)
        self.statsbtn_17.setObjectName(u"statsbtn_17")
        self.statsbtn_17.setFont(font3)
        self.statsbtn_17.setIcon(icon3)
        self.statsbtn_17.setIconSize(QSize(20, 20))

        self.verticalLayout_69.addWidget(self.statsbtn_17)


        self.horizontalLayout_4.addLayout(self.verticalLayout_69)

        self.verticalLayout_70 = QVBoxLayout()
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.performancelabel_18 = QLabel(self.widget_5)
        self.performancelabel_18.setObjectName(u"performancelabel_18")
        self.performancelabel_18.setFont(font1)
        self.performancelabel_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_70.addWidget(self.performancelabel_18)

        self.label_34 = QLabel(self.widget_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)
        self.label_34.setAlignment(Qt.AlignCenter)
        self.label_34.setWordWrap(True)
        self.label_34.setMargin(5)

        self.verticalLayout_70.addWidget(self.label_34)

        self.label_27 = QLabel(self.widget_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.verticalLayout_70.addWidget(self.label_27)

        self.lineEdit_3 = QLineEdit(self.widget_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_70.addWidget(self.lineEdit_3)

        self.statsbtn_18 = QPushButton(self.widget_5)
        self.statsbtn_18.setObjectName(u"statsbtn_18")
        self.statsbtn_18.setFont(font3)
        self.statsbtn_18.setIcon(icon3)
        self.statsbtn_18.setIconSize(QSize(20, 20))

        self.verticalLayout_70.addWidget(self.statsbtn_18)


        self.horizontalLayout_4.addLayout(self.verticalLayout_70)


        self.horizontalLayout_5.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.page)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_71 = QVBoxLayout()
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.performancelabel_19 = QLabel(self.widget_6)
        self.performancelabel_19.setObjectName(u"performancelabel_19")
        self.performancelabel_19.setFont(font1)
        self.performancelabel_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.performancelabel_19)

        self.label_35 = QLabel(self.widget_6)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)
        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_35.setWordWrap(True)
        self.label_35.setMargin(5)

        self.verticalLayout_71.addWidget(self.label_35)

        self.statsbtn_19 = QPushButton(self.widget_6)
        self.statsbtn_19.setObjectName(u"statsbtn_19")
        self.statsbtn_19.setFont(font3)
        self.statsbtn_19.setIcon(icon3)
        self.statsbtn_19.setIconSize(QSize(20, 20))

        self.verticalLayout_71.addWidget(self.statsbtn_19)


        self.horizontalLayout_3.addLayout(self.verticalLayout_71)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.performancelabel_16 = QLabel(self.widget_6)
        self.performancelabel_16.setObjectName(u"performancelabel_16")
        self.performancelabel_16.setFont(font1)
        self.performancelabel_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.performancelabel_16)

        self.label_32 = QLabel(self.widget_6)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_32.setWordWrap(True)
        self.label_32.setMargin(5)

        self.verticalLayout_47.addWidget(self.label_32)

        self.statsbtn_16 = QPushButton(self.widget_6)
        self.statsbtn_16.setObjectName(u"statsbtn_16")
        self.statsbtn_16.setFont(font3)
        self.statsbtn_16.setIcon(icon3)
        self.statsbtn_16.setIconSize(QSize(20, 20))

        self.verticalLayout_47.addWidget(self.statsbtn_16)


        self.horizontalLayout_3.addLayout(self.verticalLayout_47)


        self.horizontalLayout_5.addWidget(self.widget_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)


        self.verticalLayout_78.addLayout(self.verticalLayout_10)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_54.addWidget(self.stackedWidget)


        self.gridLayout.addLayout(self.verticalLayout_54, 1, 2, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logosub = QLabel(self.widget_3)
        self.logosub.setObjectName(u"logosub")
        self.logosub.setMinimumSize(QSize(50, 50))
        self.logosub.setMaximumSize(QSize(70, 70))
        self.logosub.setPixmap(QPixmap(u":/icons/icons/agent-high-resolution-logo.png"))
        self.logosub.setScaledContents(True)
        self.logosub.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.logosub)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 128, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.homesub = QPushButton(self.widget_3)
        self.homesub.setObjectName(u"homesub")
        font5 = QFont()
        font5.setBold(True)
        font5.setItalic(False)
        self.homesub.setFont(font5)
        self.homesub.setMouseTracking(True)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homesub.setIcon(icon11)
        self.homesub.setIconSize(QSize(20, 16))
        self.homesub.setCheckable(True)
        self.homesub.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.homesub)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 158, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.closesub = QPushButton(self.widget_3)
        self.closesub.setObjectName(u"closesub")
        self.closesub.setFont(font3)
        self.closesub.setIcon(icon10)
        self.closesub.setCheckable(True)
        self.closesub.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.closesub)

        self.verticalSpacer_3 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout.addWidget(self.widget_3, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menubtn.toggled.connect(self.widget_3.setHidden)
        self.menubtn.toggled.connect(self.widget_3.setVisible)
        self.closesub.toggled.connect(self.widget_3.setHidden)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menubtn.setText("")
        self.mainlogo.setText("")
        self.supportbtn.setText("")
        self.accountbalancelabel.setText(QCoreApplication.translate("MainWindow", u"Pypdf", None))
        self.performancelabel_15.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u" Combines multiple PDF files into a single PDF document.", None))
        self.statsbtn_15.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
        self.mt5label_14.setText(QCoreApplication.translate("MainWindow", u"Compress Pdf", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u" Reduces the file size of a PDF document", None))
        self.setupbtn_14.setText(QCoreApplication.translate("MainWindow", u"Compress", None))
        self.performancelabel_10.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Extracts text content from a PDF document", None))
        self.statsbtn_10.setText(QCoreApplication.translate("MainWindow", u"Etract", None))
        self.mt5label_9.setText(QCoreApplication.translate("MainWindow", u"Split", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Divides a PDF document into multiple smaller PDFs", None))
        self.setupbtn_9.setText(QCoreApplication.translate("MainWindow", u"Split", None))
        self.performancelabel_12.setText(QCoreApplication.translate("MainWindow", u"Encrypt Pdf", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" Encrypts PDF files to add password protection", None))
        self.statsbtn_12.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.mt5label_11.setText(QCoreApplication.translate("MainWindow", u"Decrypt Pdf", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u" Decrypts encrypted PDF files to remove password protection,", None))
        self.setupbtn_11.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.performancelabel_11.setText(QCoreApplication.translate("MainWindow", u"Pdf to word", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u" Converts PDF documents to Microsoft Word format", None))
        self.statsbtn_11.setText(QCoreApplication.translate("MainWindow", u"pdf2word", None))
        self.mt5label_10.setText(QCoreApplication.translate("MainWindow", u"Word to Pdf", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u" Converts Word documents to pdf format", None))
        self.setupbtn_10.setText(QCoreApplication.translate("MainWindow", u"word2pdf", None))
        self.performancelabel_13.setText(QCoreApplication.translate("MainWindow", u"WaterMark", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u" Places a watermark on each page of a PDF document", None))
        self.statsbtn_13.setText(QCoreApplication.translate("MainWindow", u"Watermark", None))
        self.mt5label_12.setText(QCoreApplication.translate("MainWindow", u"Rotate Pdf", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u" Rotates the pages of a PDF document", None))
        self.setupbtn_12.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.performancelabel_14.setText(QCoreApplication.translate("MainWindow", u"Organize Pdf", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Reorders the pages of a PDF document", None))
        self.statsbtn_14.setText(QCoreApplication.translate("MainWindow", u"Organize", None))
        self.mt5label_13.setText(QCoreApplication.translate("MainWindow", u"Page Numbers", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u" Adds page numbers to the pages of a PDF document", None))
        self.setupbtn_13.setText(QCoreApplication.translate("MainWindow", u"Add pages", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Upload files", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Selcet File", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Enter output Name", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Upload files", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Selcet File", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Enter output Name", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.pushButton.setText("")
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Upload files", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Upload files", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Selcet File", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Enter output Name", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.label_45.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Upload files", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Selcet File", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Upload files", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Selcet File", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Enter output Name", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Upload files", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Selcet File", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Enter output Name", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Selected File", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_30.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Upload files", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Selcet File", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Enter output Name", None))
        self.performancelabel_17.setText(QCoreApplication.translate("MainWindow", u"Remove Duplicates", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u" identifies and eliminates redundant objects within the PDF file", None))
#if QT_CONFIG(whatsthis)
        self.statsbtn_17.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The &quot;Removing Duplication&quot; function in our PDF software identifies and eliminates redundant objects within the PDF file. This includes instances where the same content, such as images or text, is repeated across multiple pages. By removing these duplicates, the function optimizes the file size without compromising the document's integrity, resulting in more efficient storage and transmission of PDF documents.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.statsbtn_17.setText(QCoreApplication.translate("MainWindow", u"Compress", None))
        self.performancelabel_18.setText(QCoreApplication.translate("MainWindow", u"Reduce Image Quality", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u" decrease the resolution and quality of images embedded within a PDF document", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Compression Rate", None))
#if QT_CONFIG(whatsthis)
        self.statsbtn_18.setWhatsThis(QCoreApplication.translate("MainWindow", u"Our software's \"Reducing Image Quality\" function allows users to decrease the resolution and quality of images embedded within a PDF document. By adjusting image quality parameters, users can achieve significant reductions in file size while retaining sufficient visual clarity for their intended use. This feature is beneficial when file size optimization is crucial, such as when sharing or storing PDFs with embedded images, without sacrificing essential visual content.", None))
#endif // QT_CONFIG(whatsthis)
        self.statsbtn_18.setText(QCoreApplication.translate("MainWindow", u"Compress", None))
        self.performancelabel_19.setText(QCoreApplication.translate("MainWindow", u"Remove Images", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u" removes all images from the PDF document", None))
#if QT_CONFIG(whatsthis)
        self.statsbtn_19.setWhatsThis(QCoreApplication.translate("MainWindow", u"The \"Removing Images\" function selectively removes all images from the PDF document, reducing its file size. This feature is particularly useful when images are not essential for the document's purpose or when minimizing file size is a priority. By eliminating images, users can create more compact PDF files suitable for various applications, including online sharing, archiving, and printing.", None))
#endif // QT_CONFIG(whatsthis)
        self.statsbtn_19.setText(QCoreApplication.translate("MainWindow", u"Compress", None))
        self.performancelabel_16.setText(QCoreApplication.translate("MainWindow", u"Lossless Compression", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u" reduce the size of PDF files without compromising the integrity or quality of the document's contents", None))
#if QT_CONFIG(whatsthis)
        self.statsbtn_16.setWhatsThis(QCoreApplication.translate("MainWindow", u"The \"Lossless Compression\" function employs advanced compression algorithms to reduce the size of PDF files without compromising the integrity or quality of the document's contents. Unlike traditional compression methods that may result in data loss or degradation, this function ensures that the PDF retains its original formatting, text, and images while achieving substantial file size reduction. By preserving document fidelity, users can efficiently manage and distribute PDF files without sacrificing quality.", None))
#endif // QT_CONFIG(whatsthis)
        self.statsbtn_16.setText(QCoreApplication.translate("MainWindow", u"Compress", None))
        self.logosub.setText("")
        self.homesub.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.closesub.setText(QCoreApplication.translate("MainWindow", u"Close", None))
    # retranslateUi

