# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sun Mar 18 22:10:49 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(765, 635)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.typesLineEdit = QtGui.QLineEdit(self.widget)
        self.typesLineEdit.setObjectName(_fromUtf8("typesLineEdit"))
        self.horizontalLayout_2.addWidget(self.typesLineEdit)
        self.typesPushButton = QtGui.QPushButton(self.widget)
        self.typesPushButton.setObjectName(_fromUtf8("typesPushButton"))
        self.horizontalLayout_2.addWidget(self.typesPushButton)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.namesLineEdit = QtGui.QLineEdit(self.widget_2)
        self.namesLineEdit.setObjectName(_fromUtf8("namesLineEdit"))
        self.horizontalLayout.addWidget(self.namesLineEdit)
        self.namesPushButton = QtGui.QPushButton(self.widget_2)
        self.namesPushButton.setObjectName(_fromUtf8("namesPushButton"))
        self.horizontalLayout.addWidget(self.namesPushButton)
        self.verticalLayout.addWidget(self.widget_2)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(186, 186, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 186, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 186, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.treeWidget.setPalette(palette)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setDefaultSectionSize(90)
        self.treeWidget.header().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.treeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuFile.sizePolicy().hasHeightForWidth())
        self.menuFile.setSizePolicy(sizePolicy)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuData = QtGui.QMenu(self.menubar)
        self.menuData.setObjectName(_fromUtf8("menuData"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAdd_Row = QtGui.QAction(MainWindow)
        self.actionAdd_Row.setObjectName(_fromUtf8("actionAdd_Row"))
        self.actionAdd_Col = QtGui.QAction(MainWindow)
        self.actionAdd_Col.setObjectName(_fromUtf8("actionAdd_Col"))
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionDelete_Row = QtGui.QAction(MainWindow)
        self.actionDelete_Row.setObjectName(_fromUtf8("actionDelete_Row"))
        self.actionDelete_Col = QtGui.QAction(MainWindow)
        self.actionDelete_Col.setObjectName(_fromUtf8("actionDelete_Col"))
        self.actionPopulate_from_set = QtGui.QAction(MainWindow)
        self.actionPopulate_from_set.setObjectName(_fromUtf8("actionPopulate_from_set"))
        self.actionDEBUG = QtGui.QAction(MainWindow)
        self.actionDEBUG.setObjectName(_fromUtf8("actionDEBUG"))
        self.actionEdit_Column_Types = QtGui.QAction(MainWindow)
        self.actionEdit_Column_Types.setObjectName(_fromUtf8("actionEdit_Column_Types"))
        self.menuData.addAction(self.actionAdd_Row)
        self.menuData.addAction(self.actionAdd_Col)
        self.menuData.addAction(self.actionEdit_Column_Types)
        self.menuData.addAction(self.actionClear)
        self.menuData.addAction(self.actionDelete_Row)
        self.menuData.addAction(self.actionDelete_Col)
        self.menuData.addAction(self.actionPopulate_from_set)
        self.menuData.addAction(self.actionDEBUG)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuData.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Systemy Wspomagania Decyzji", None, QtGui.QApplication.UnicodeUTF8))
        self.typesPushButton.setText(QtGui.QApplication.translate("MainWindow", "Cast Types", None, QtGui.QApplication.UnicodeUTF8))
        self.namesPushButton.setText(QtGui.QApplication.translate("MainWindow", "Change Names", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData.setTitle(QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Row.setText(QtGui.QApplication.translate("MainWindow", "Add Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Col.setText(QtGui.QApplication.translate("MainWindow", "Add Col", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Row.setText(QtGui.QApplication.translate("MainWindow", "Delete Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Col.setText(QtGui.QApplication.translate("MainWindow", "Delete Col", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPopulate_from_set.setText(QtGui.QApplication.translate("MainWindow", "Populate from set", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDEBUG.setText(QtGui.QApplication.translate("MainWindow", "DEBUG", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Column_Types.setText(QtGui.QApplication.translate("MainWindow", "Edit Column Types", None, QtGui.QApplication.UnicodeUTF8))
