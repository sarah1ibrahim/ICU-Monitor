# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\user\Desktop\root\my life\SBME 2025\3rd_year\DSP\tasks\task1\task1-signal-viewer-dsp_fall23_task1_team17\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1859, 1015)
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 1px solid darkgray;*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/dark_orange/img/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    border: 1px solid darkgray;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/dark_orange/img/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid darkgray;\n"
"\n"
"    border-radius: 2px;\n"
"    min-width: 50px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_18.setObjectName("gridLayout_18")
        spacerItem = QtWidgets.QSpacerItem(20, 691, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_18.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setVerticalSpacing(20)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.browse = QtWidgets.QPushButton(self.widget)
        self.browse.setMinimumSize(QtCore.QSize(52, 30))
        self.browse.setShortcut("")
        self.browse.setObjectName("browse")
        self.gridLayout_17.addWidget(self.browse, 0, 0, 1, 1)
        self.export_button = QtWidgets.QPushButton(self.widget)
        self.export_button.setMinimumSize(QtCore.QSize(52, 30))
        self.export_button.setObjectName("export_button")
        self.gridLayout_17.addWidget(self.export_button, 2, 0, 1, 1)
        self.choose_graph = QtWidgets.QComboBox(self.widget)
        self.choose_graph.setMinimumSize(QtCore.QSize(0, 30))
        self.choose_graph.setObjectName("choose_graph")
        self.choose_graph.addItem("")
        self.choose_graph.addItem("")
        self.gridLayout_17.addWidget(self.choose_graph, 1, 0, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_17, 0, 0, 1, 1)
        self.gridLayout_20.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_8.setContentsMargins(9, 19, -1, -1)
        self.gridLayout_8.setHorizontalSpacing(7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.widget_4 = PlotWidget(self.groupBox)
        self.widget_4.setMinimumSize(QtCore.QSize(600, 350))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 0, 0, 1, 1)
        self.verticalScrollBar1 = QtWidgets.QScrollBar(self.groupBox)
        self.verticalScrollBar1.setMinimumSize(QtCore.QSize(15, 0))
        self.verticalScrollBar1.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar1.setObjectName("verticalScrollBar1")
        self.gridLayout.addWidget(self.verticalScrollBar1, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalScrollBar1 = QtWidgets.QScrollBar(self.groupBox)
        self.horizontalScrollBar1.setMinimumSize(QtCore.QSize(0, 15))
        self.horizontalScrollBar1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar1.setObjectName("horizontalScrollBar1")
        self.gridLayout_6.addWidget(self.horizontalScrollBar1, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.channels1 = QtWidgets.QComboBox(self.groupBox)
        self.channels1.setObjectName("channels1")
        self.gridLayout_9.addWidget(self.channels1, 0, 0, 1, 1)
        self.play_pause = QtWidgets.QPushButton(self.groupBox)
        self.play_pause.setObjectName("play_pause")
        self.gridLayout_9.addWidget(self.play_pause, 0, 1, 1, 1)
        self.zoom_in_1 = QtWidgets.QPushButton(self.groupBox)
        self.zoom_in_1.setObjectName("zoom_in_1")
        self.gridLayout_9.addWidget(self.zoom_in_1, 0, 2, 1, 1)
        self.zoom_out_1 = QtWidgets.QPushButton(self.groupBox)
        self.zoom_out_1.setObjectName("zoom_out_1")
        self.gridLayout_9.addWidget(self.zoom_out_1, 0, 3, 1, 1)
        self.reset = QtWidgets.QPushButton(self.groupBox)
        self.reset.setObjectName("reset")
        self.gridLayout_9.addWidget(self.reset, 0, 4, 1, 1)
        self.hide_checkbox1 = QtWidgets.QCheckBox(self.groupBox)
        self.hide_checkbox1.setObjectName("hide_checkbox1")
        self.gridLayout_9.addWidget(self.hide_checkbox1, 0, 5, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_9, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(7)
        self.gridLayout_3.setVerticalSpacing(25)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setHorizontalSpacing(15)
        self.formLayout_2.setObjectName("formLayout_2")
        self.CineSpeed = QtWidgets.QLabel(self.widget_2)
        self.CineSpeed.setObjectName("CineSpeed")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.CineSpeed)
        self.speed_slider1 = QtWidgets.QSlider(self.widget_2)
        self.speed_slider1.setMinimumSize(QtCore.QSize(50, 0))
        self.speed_slider1.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider1.setObjectName("speed_slider1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.speed_slider1)
        self.gridLayout_3.addLayout(self.formLayout_2, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label1 = QtWidgets.QLabel(self.widget_2)
        self.label1.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.edit_label1 = QtWidgets.QLineEdit(self.widget_2)
        self.edit_label1.setMaximumSize(QtCore.QSize(300, 16777215))
        self.edit_label1.setObjectName("edit_label1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_label1)
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)
        self.move1 = QtWidgets.QPushButton(self.widget_2)
        self.move1.setObjectName("move1")
        self.gridLayout_3.addWidget(self.move1, 3, 0, 1, 1)
        self.color_button1 = QtWidgets.QPushButton(self.widget_2)
        self.color_button1.setObjectName("color_button1")
        self.gridLayout_3.addWidget(self.color_button1, 2, 0, 1, 1)
        self.snapshot_button1 = QtWidgets.QPushButton(self.widget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/snapshot_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snapshot_button1.setIcon(icon)
        self.snapshot_button1.setObjectName("snapshot_button1")
        self.gridLayout_3.addWidget(self.snapshot_button1, 4, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.widget_2, 0, 1, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_13.setContentsMargins(-1, 19, -1, -1)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(self.groupBox_2)
        self.horizontalScrollBar_2.setMinimumSize(QtCore.QSize(0, 15))
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")
        self.gridLayout_12.addWidget(self.horizontalScrollBar_2, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_5 = PlotWidget(self.groupBox_2)
        self.widget_5.setMinimumSize(QtCore.QSize(600, 350))
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.groupBox_2)
        self.verticalScrollBar_2.setMinimumSize(QtCore.QSize(15, 0))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.gridLayout_2.addWidget(self.verticalScrollBar_2, 0, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.channels_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.channels_2.setObjectName("channels_2")
        self.horizontalLayout.addWidget(self.channels_2)
        self.play_pause_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.play_pause_2.setObjectName("play_pause_2")
        self.horizontalLayout.addWidget(self.play_pause_2)
        self.zoom_in_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.zoom_in_2.setObjectName("zoom_in_2")
        self.horizontalLayout.addWidget(self.zoom_in_2)
        self.zoom_out_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.zoom_out_2.setObjectName("zoom_out_2")
        self.horizontalLayout.addWidget(self.zoom_out_2)
        self.reset_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.reset_2.setObjectName("reset_2")
        self.horizontalLayout.addWidget(self.reset_2)
        self.hide_checkbox2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.hide_checkbox2.setObjectName("hide_checkbox2")
        self.horizontalLayout.addWidget(self.hide_checkbox2)
        self.gridLayout_11.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setVerticalSpacing(25)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.color_button2 = QtWidgets.QPushButton(self.widget_3)
        self.color_button2.setObjectName("color_button2")
        self.gridLayout_4.addWidget(self.color_button2, 2, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setHorizontalSpacing(15)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label2 = QtWidgets.QLabel(self.widget_3)
        self.label2.setObjectName("label2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.edit_label2 = QtWidgets.QLineEdit(self.widget_3)
        self.edit_label2.setObjectName("edit_label2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_label2)
        self.gridLayout_4.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setHorizontalSpacing(15)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.speed_slider2 = QtWidgets.QSlider(self.widget_3)
        self.speed_slider2.setMinimumSize(QtCore.QSize(50, 0))
        self.speed_slider2.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider2.setObjectName("speed_slider2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.speed_slider2)
        self.gridLayout_4.addLayout(self.formLayout_4, 1, 0, 1, 1)
        self.move2 = QtWidgets.QPushButton(self.widget_3)
        self.move2.setObjectName("move2")
        self.gridLayout_4.addWidget(self.move2, 3, 0, 1, 1)
        self.snapshot_button2 = QtWidgets.QPushButton(self.widget_3)
        self.snapshot_button2.setIcon(icon)
        self.snapshot_button2.setObjectName("snapshot_button2")
        self.gridLayout_4.addWidget(self.snapshot_button2, 4, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_15.addWidget(self.widget_3, 0, 1, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.link_graphs_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.link_graphs_checkbox.setObjectName("link_graphs_checkbox")
        self.gridLayout_19.addWidget(self.link_graphs_checkbox, 1, 0, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_19, 0, 1, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1859, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse.setText(_translate("MainWindow", "Import"))
        self.export_button.setText(_translate("MainWindow", "Export"))
        self.export_button.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.choose_graph.setCurrentText(_translate("MainWindow", "     Graph1  "))
        self.choose_graph.setItemText(0, _translate("MainWindow", "     Graph1  "))
        self.choose_graph.setItemText(1, _translate("MainWindow", "     Graph2   "))
        self.groupBox.setTitle(_translate("MainWindow", "Graph1"))
        self.play_pause.setText(_translate("MainWindow", "play/pause"))
        self.play_pause.setShortcut(_translate("MainWindow", "Space"))
        self.zoom_in_1.setText(_translate("MainWindow", "zoom in"))
        self.zoom_in_1.setShortcut(_translate("MainWindow", "+"))
        self.zoom_out_1.setText(_translate("MainWindow", "zoom out"))
        self.zoom_out_1.setShortcut(_translate("MainWindow", "-"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.reset.setShortcut(_translate("MainWindow", "Left"))
        self.hide_checkbox1.setText(_translate("MainWindow", "hide"))
        self.CineSpeed.setText(_translate("MainWindow", "Cine Speed"))
        self.label1.setText(_translate("MainWindow", "Label"))
        self.move1.setText(_translate("MainWindow", "Move Down"))
        self.move1.setShortcut(_translate("MainWindow", "Down"))
        self.color_button1.setText(_translate("MainWindow", "Color "))
        self.snapshot_button1.setToolTip(_translate("MainWindow", "Take snapshot of Graph1"))
        self.snapshot_button1.setText(_translate("MainWindow", "SnapShot"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Graph2"))
        self.play_pause_2.setText(_translate("MainWindow", "play/pause"))
        self.zoom_in_2.setText(_translate("MainWindow", "zoom in"))
        self.zoom_out_2.setText(_translate("MainWindow", "zoom out"))
        self.reset_2.setText(_translate("MainWindow", "Reset"))
        self.reset_2.setShortcut(_translate("MainWindow", "-"))
        self.hide_checkbox2.setText(_translate("MainWindow", "hide"))
        self.color_button2.setText(_translate("MainWindow", "Color "))
        self.label2.setText(_translate("MainWindow", "Label"))
        self.label_4.setText(_translate("MainWindow", "Cine Speed"))
        self.move2.setText(_translate("MainWindow", "Move Up"))
        self.move2.setShortcut(_translate("MainWindow", "Up"))
        self.snapshot_button2.setText(_translate("MainWindow", "SnapShot"))
        self.link_graphs_checkbox.setText(_translate("MainWindow", "Link Signals"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

from pyqtgraph import PlotWidget
