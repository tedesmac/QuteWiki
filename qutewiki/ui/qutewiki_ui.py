# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qutewiki.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tagView = QtWidgets.QTreeView(self.splitter)
        self.tagView.setMaximumSize(QtCore.QSize(100, 16777215))
        self.tagView.setObjectName("tagView")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.addPageButton = QtWidgets.QPushButton(self.widget)
        self.addPageButton.setObjectName("addPageButton")
        self.verticalLayout.addWidget(self.addPageButton)
        self.pagesView = QtWidgets.QListWidget(self.widget)
        self.pagesView.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pagesView.setObjectName("pagesView")
        self.verticalLayout.addWidget(self.pagesView)
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = Editor(self.widget_2)
        self.textEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.modeButtton = QtWidgets.QPushButton(self.widget_3)
        self.modeButtton.setObjectName("modeButtton")
        self.verticalLayout_2.addWidget(self.modeButtton)
        spacerItem = QtWidgets.QSpacerItem(20, 516, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.showTagsButton = QtWidgets.QPushButton(self.widget_3)
        self.showTagsButton.setObjectName("showTagsButton")
        self.verticalLayout_2.addWidget(self.showTagsButton)
        self.horizontalLayout.addWidget(self.widget_3)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QuteWiki"))
        self.addPageButton.setText(_translate("MainWindow", "New Note"))
        self.modeButtton.setText(_translate("MainWindow", "V"))
        self.showTagsButton.setText(_translate("MainWindow", "T"))

from qutewiki.editor import Editor
