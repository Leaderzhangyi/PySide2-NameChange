# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customize.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(493, 312)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 441, 271))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setPointSize(11)
        self.lineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy1)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8bf4\u660e\uff1a\n"
"1.\u53ef\u9009\u53c2\u6570(\u5b66\u53f7\u3001\u59d3\u540d\u3001\u6587\u4ef6\u540d\u79f0\u3001\u73ed\u7ea7)\n"
"2. \u4ee5'-'\u7b26\u53f7\u9694\u5f00\uff08\u6bd4\u5982\uff1a\u73ed\u7ea7-\u59d3\u540d-\u6587\u4ef6\u540d\u79f0\uff09\n"
"3. \u73ed\u4e0a\u6709\u540c\u540d\u540c\u59d3\u7684\u540c\u5b66\uff0c\u5fc5\u987b\u5e26\u6709\u5b66\u53f7\uff01", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8bf7\u586b\u5199\u76f8\u5e94\u683c\u5f0f...", None))
    # retranslateUi

