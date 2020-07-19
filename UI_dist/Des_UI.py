# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Des_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1113, 802)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.actionYea = QAction(MainWindow)
        self.actionYea.setObjectName(u"actionYea")
        self.actiond = QAction(MainWindow)
        self.actiond.setObjectName(u"actiond")
        self.actionda = QAction(MainWindow)
        self.actionda.setObjectName(u"actionda")
        self.action132 = QAction(MainWindow)
        self.action132.setObjectName(u"action132")
        self.action654 = QAction(MainWindow)
        self.action654.setObjectName(u"action654")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"\u817e\u8baf\u4f53")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.Download = QPushButton(self.centralwidget)
        self.Download.setObjectName(u"Download")
        self.Download.setEnabled(True)
        self.Download.setMaximumSize(QSize(500, 16777215))
        font2 = QFont()
        font2.setFamily(u"Microsoft YaHei UI")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.Download.setFont(font2)

        self.horizontalLayout.addWidget(self.Download)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.select1 = QPushButton(self.centralwidget)
        self.select1.setObjectName(u"select1")
        font3 = QFont()
        font3.setFamily(u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53 B")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.select1.setFont(font3)

        self.verticalLayout_2.addWidget(self.select1)

        self.GetData = QPushButton(self.centralwidget)
        self.GetData.setObjectName(u"GetData")
        self.GetData.setFont(font3)
        self.GetData.setStyleSheet(u"color: rgb(255, 112, 29);\n"
"\n"
"")
        self.GetData.setAutoRepeat(False)

        self.verticalLayout_2.addWidget(self.GetData)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        palette = QPalette()
        brush = QBrush(QColor(197, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.groupBox.setPalette(palette)
        font4 = QFont()
        font4.setFamily(u"Microsoft YaHei UI")
        font4.setPointSize(12)
        self.groupBox.setFont(font4)
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 15, -1, -1)
        self.select2 = QPushButton(self.groupBox)
        self.select2.setObjectName(u"select2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.select2.sizePolicy().hasHeightForWidth())
        self.select2.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamily(u"Microsoft YaHei UI")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.select2.setFont(font5)
        self.select2.setCheckable(False)

        self.horizontalLayout_8.addWidget(self.select2)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(5)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.comboBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setFamily(u"Microsoft YaHei UI")
        font6.setPointSize(10)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 195);")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.number = QLineEdit(self.groupBox)
        self.number.setObjectName(u"number")
        font7 = QFont()
        font7.setFamily(u"Microsoft YaHei UI")
        font7.setPointSize(9)
        self.number.setFont(font7)

        self.horizontalLayout_2.addWidget(self.number)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        palette1 = QPalette()
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_5.setPalette(palette1)
        self.label_5.setFont(font6)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.charsplit = QLineEdit(self.groupBox)
        self.charsplit.setObjectName(u"charsplit")
        self.charsplit.setFont(font7)

        self.horizontalLayout_2.addWidget(self.charsplit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_4.setPalette(palette2)
        self.label_4.setFont(font6)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.FileNames = QLineEdit(self.groupBox)
        self.FileNames.setObjectName(u"FileNames")
        self.FileNames.setFont(font7)

        self.horizontalLayout_3.addWidget(self.FileNames)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_6.setPalette(palette3)
        self.label_6.setFont(font6)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.ClassName = QLineEdit(self.groupBox)
        self.ClassName.setObjectName(u"ClassName")
        self.ClassName.setFont(font7)

        self.horizontalLayout_3.addWidget(self.ClassName)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.label_7.setPalette(palette4)
        self.label_7.setFont(font6)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.btn_delete = QPushButton(self.groupBox)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy3)
        self.btn_delete.setMaximumSize(QSize(40, 16777215))
        font8 = QFont()
        font8.setFamily(u"Microsoft YaHei UI")
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setWeight(75)
        self.btn_delete.setFont(font8)
        self.btn_delete.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.btn_delete)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")
        palette5 = QPalette()
        brush3 = QBrush(QColor(0, 0, 195, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        brush4 = QBrush(QColor(0, 0, 195, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        brush5 = QBrush(QColor(0, 0, 195, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        brush6 = QBrush(QColor(0, 0, 195, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBox_2.setPalette(palette5)
        font9 = QFont()
        font9.setFamily(u"Microsoft YaHei UI")
        font9.setPointSize(11)
        self.comboBox_2.setFont(font9)
        self.comboBox_2.setStyleSheet(u"color: rgb(0, 0, 195);")

        self.horizontalLayout_4.addWidget(self.comboBox_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 10, -1, 10)
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy3.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy3)
        self.radioButton.setFont(font8)
        self.radioButton.setStyleSheet(u"color: rgb(255, 2, 2);")

        self.horizontalLayout_12.addWidget(self.radioButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 20)
        self.Change = QPushButton(self.groupBox)
        self.Change.setObjectName(u"Change")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(6)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Change.sizePolicy().hasHeightForWidth())
        self.Change.setSizePolicy(sizePolicy4)
        self.Change.setMinimumSize(QSize(60, 30))
        self.Change.setMaximumSize(QSize(160, 80))
        palette6 = QPalette()
        gradient = QLinearGradient(0, 0, 1, 1)
        gradient.setSpread(QConicalGradient.RepeatSpread)
        gradient.setCoordinateMode(QConicalGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(255, 0, 0, 255))
        gradient.setColorAt(0.492537, QColor(255, 170, 170, 255))
        gradient.setColorAt(0.955224, QColor(255, 0, 0, 255))
        brush7 = QBrush(gradient)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush7)
        gradient1 = QLinearGradient(0, 0, 1, 1)
        gradient1.setSpread(QConicalGradient.RepeatSpread)
        gradient1.setCoordinateMode(QConicalGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(255, 0, 0, 255))
        gradient1.setColorAt(0.492537, QColor(255, 170, 170, 255))
        gradient1.setColorAt(0.955224, QColor(255, 0, 0, 255))
        brush8 = QBrush(gradient1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush8)
        gradient2 = QLinearGradient(0, 0, 1, 1)
        gradient2.setSpread(QConicalGradient.RepeatSpread)
        gradient2.setCoordinateMode(QConicalGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(255, 0, 0, 255))
        gradient2.setColorAt(0.492537, QColor(255, 170, 170, 255))
        gradient2.setColorAt(0.955224, QColor(255, 0, 0, 255))
        brush9 = QBrush(gradient2)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush9)
        gradient3 = QLinearGradient(0, 0, 1, 1)
        gradient3.setSpread(QConicalGradient.RepeatSpread)
        gradient3.setCoordinateMode(QConicalGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(255, 0, 0, 255))
        gradient3.setColorAt(0.492537, QColor(255, 170, 170, 255))
        gradient3.setColorAt(0.955224, QColor(255, 0, 0, 255))
        brush10 = QBrush(gradient3)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        gradient4 = QLinearGradient(0, 0, 1, 1)
        gradient4.setSpread(QConicalGradient.RepeatSpread)
        gradient4.setCoordinateMode(QConicalGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(255, 0, 0, 255))
        gradient4.setColorAt(0.492537, QColor(255, 170, 170, 255))
        gradient4.setColorAt(0.955224, QColor(255, 0, 0, 255))
        brush11 = QBrush(gradient4)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        gradient5 = QLinearGradient(0, 0, 1, 1)
        gradient5.setSpread(QConicalGradient.RepeatSpread)
        gradient5.setCoordinateMode(QConicalGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(255, 0, 0, 255))
        gradient5.setColorAt(0.492537, QColor(255, 170, 170, 255))
        gradient5.setColorAt(0.955224, QColor(255, 0, 0, 255))
        brush12 = QBrush(gradient5)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        gradient6 = QLinearGradient(0, 0, 1, 1)
        gradient6.setSpread(QConicalGradient.RepeatSpread)
        gradient6.setCoordinateMode(QConicalGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(255, 0, 0, 255))
        gradient6.setColorAt(0.492537, QColor(255, 170, 170, 255))
        gradient6.setColorAt(0.955224, QColor(255, 0, 0, 255))
        brush13 = QBrush(gradient6)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        gradient7 = QLinearGradient(0, 0, 1, 1)
        gradient7.setSpread(QConicalGradient.RepeatSpread)
        gradient7.setCoordinateMode(QConicalGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(255, 0, 0, 255))
        gradient7.setColorAt(0.492537, QColor(255, 170, 170, 255))
        gradient7.setColorAt(0.955224, QColor(255, 0, 0, 255))
        brush14 = QBrush(gradient7)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        gradient8 = QLinearGradient(0, 0, 1, 1)
        gradient8.setSpread(QConicalGradient.RepeatSpread)
        gradient8.setCoordinateMode(QConicalGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(255, 0, 0, 255))
        gradient8.setColorAt(0.492537, QColor(255, 170, 170, 255))
        gradient8.setColorAt(0.955224, QColor(255, 0, 0, 255))
        brush15 = QBrush(gradient8)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        self.Change.setPalette(palette6)
        font10 = QFont()
        font10.setFamily(u"\u65b9\u6b63\u59da\u4f53")
        font10.setPointSize(12)
        self.Change.setFont(font10)
        self.Change.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.492537 rgba(255, 170, 170, 255), stop:0.955224 rgba(255, 0, 0, 255));\n"
"border-radius:10px\n"
"")

        self.horizontalLayout_13.addWidget(self.Change)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.groupBox_2.setPalette(palette7)
        font11 = QFont()
        font11.setFamily(u"\u9ed1\u4f53")
        font11.setPointSize(9)
        font11.setBold(False)
        font11.setItalic(False)
        font11.setWeight(50)
        self.groupBox_2.setFont(font11)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.progressBar = QProgressBar(self.groupBox_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFont(font11)
        self.progressBar.setValue(24)

        self.verticalLayout_4.addWidget(self.progressBar)

        self.textBrowser = QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"\n"
"background-color: rgb(231, 231, 231);")

        self.verticalLayout_4.addWidget(self.textBrowser)


        self.horizontalLayout_5.addWidget(self.groupBox_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line)

        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        font12 = QFont()
        font12.setFamily(u"\u65b9\u6b63\u59da\u4f53")
        font12.setPointSize(9)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setWeight(50)
        self.calendarWidget.setFont(font12)
        self.calendarWidget.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.calendarWidget)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_9)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1113, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionYea)
        self.menu.addSeparator()
        self.menu.addAction(self.action132)
        self.menu.addSeparator()
        self.menu_2.addAction(self.actiond)
        self.menu_2.addAction(self.actionda)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5b66\u59d4\u52a9\u624bv1.0\u6d4b\u8bd5\u7248", None))
        self.actionYea.setText(QCoreApplication.translate("MainWindow", u"\u50ac\u4f5c\u4e1a\u8f70\u70b8\u5668", None))
        self.actiond.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.actionda.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.action132.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u4f5c\u4e1a\u5012\u8ba1\u65f6", None))
        self.action654.setText(QCoreApplication.translate("MainWindow", u"\u6ca1\u60f3\u597d2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4ec5\u5c55\u793a\u524d50\u6761\u6570\u636e", None))
        self.Download.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        self.select1.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5b66\u53f7\u59d3\u540d\u6587\u4ef6", None))
        self.GetData.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u6570\u636e", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6761\u4ef6\u9009\u62e9", None))
        self.select2.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u88ab\u4fee\u6539\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5b66\u53f7\u524d4\u4f4d\uff1a", None))
        self.number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5fc5\u586b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u586b\u5199\u5206\u9694\u7b26\uff1a", None))
        self.charsplit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u4e3a\"-\"", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u586b\u5199\u4fee\u6539\u6587\u4ef6\u540d\uff1a", None))
        self.FileNames.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9009\u586b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u586b\u5199\u73ed\u7ea7\uff1a", None))
        self.ClassName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9009\u586b", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6392\u7248\u987a\u5e8f\uff1a", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u5f00\u542f\u68c0\u6d4b\u672a\u4ea4\u529f\u80fd\uff1f", None))
        self.Change.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4fee\u6539", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u60c5\u51b5\u4e0e\u9519\u8bef\u68c0\u6d4b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u5de5\u5177", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

